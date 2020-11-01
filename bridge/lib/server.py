#!/usr/bin/env python3

import os
from os import SCHED_OTHER

from PySide2.QtNetwork import QHostAddress, QTcpServer, QTcpSocket
from PySide2.QtSerialPort import QSerialPort
from PySide2.QtCore import QIODevice

from .console import Console

class Server(QTcpServer):

   def __init__(self, settings):

      QTcpServer.__init__(self)
      self.settings = settings

      self.serial = QSerialPort()
      self.serial.setBaudRate(115200)
      self.serial.setParity(QSerialPort.NoParity)
      self.serial.setDataBits(QSerialPort.Data8)
      self.serial.setStopBits(QSerialPort.OneStop)
      self.serial.readyRead.connect(self._serialRead)
      self.serial.errorOccurred.connect(self._serialError)

      self.socket = None
      self.newConnection.connect(self._newTcpConnection)
      self.acceptError.connect(self._serverError)

      if self.listen(QHostAddress.Any, settings.serverPort):
         print(Console.green('server started'), 'at port:', settings.serverPort)
      else:
         message = Console.red('unable to start tcp server') + ' at port: ' + str(settings.serverPort) + ' -> ' +  self.errorString()
         raise Exception(message)

   def __del__(self):

      if self.serial.isOpen():
         print()
         print(Console.yellow('closing serial connection'), 'for port', self.settings.serverPort)
         self.serial.close()

   def _serialRead(self):

      data = self.serial.readAll()
      
      if not self.socket:
         return

      self.socket.write(data)

   def _serialError(self, error):

      if error == QSerialPort.NoError:
         return

      print(Console.red(self.serial.errorString()))

   def _tcpRead(self):

      if not self.socket:
         return

      data = self.socket.readAll()
      self.serial.write(data)

   def _newTcpConnection(self):

      if self.socket:
         self.socket.close()
         self.socket.readyRead.disconnect()
         self.socket.deleteLater()
         self.socket = None

      self.socket = self.nextPendingConnection()
      self.socket.readyRead.connect(self._tcpRead)
      self.socket.disconnected.connect(self._tcpDisconneted)

      if not self.serial.isOpen():

         device = self.settings.bluetoothDevice
         if os.path.exists(self.settings.usbDevice):
            device = self.settings.usbDevice
         
         self.serial.setPortName(device)
         print(Console.green('open serial connection'), 'for tcp port', self.settings.serverPort, ' to device:', device)
         self.serial.open(QIODevice.ReadWrite)
         print()
            
      print(Console.blue('tcp socket conneted'), 'at port:', self.settings.serverPort)

   def _serverError(self, socketError):

      print(Console.red(socketError))

   def _tcpDisconneted(self):

      self.socket.readyRead.disconnect()
      self.socket.deleteLater()
      self.socket = None

      print(Console.blue('tcp socket disconneted'), 'at port:', self.settings.serverPort)

      