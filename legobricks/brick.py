#!/usr/bin/env python3

import sys
from time import sleep

from PySide2.QtCore import QCoreApplication
from PySide2.QtNetwork import QTcpSocket

from helper import Console, Device

"""
Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
  CTRL-F        -- on a blank line, enter filetransfer mode
"""

class Firmware:

   RobotInventor = 1
   SpikePrime = 2

class Brick(QTcpSocket):


   def __init__(self, host = '127.0.0.1', port = 51515, firmware = Firmware.RobotInvetor, verbose = False):

      QTcpSocket.__init__(self)
      self._verbose = verbose
      self._recvBuffer = None

      self.readyRead.connect(self._readTcp)
      self.error.connect(self._handleError)
      self.connected.connect(self._connected)
      self.connectToHost(host, port)
      self.waitForConnected()

      Device.setAllHeaders(self, firmware)

   def sendCode(self, code):

      if isinstance(code, str):
         code = [ code ]

      result = '>>> '
      def sendLineOfCode(line):

         nonlocal result
         self._recvBuffer = None

         if not line.endswith('\r'):
            line = line + '\r'

         if self._verbose and line.strip():
            print(Console.grey(line))

         byteCode = line.encode()
         self.write(byteCode)

         while not self._recvBuffer:
            QCoreApplication.processEvents()

         while not line in result:
            result += bytes(self._recvBuffer).decode()
            QCoreApplication.processEvents()

      for line in code:
         sendLineOfCode(line)

      resultList = result.split('\r\n')    
      resultList = [ line for line in resultList if not line.startswith('>>> ')]

      if self._verbose:
         for line in resultList:
            if not line:
               continue
            print(Console.white(line, True))

      return resultList

   def _readTcp(self):

      data = self.readAll()
      if not self._recvBuffer:
         self._recvBuffer = data
      else:
         self._recvBuffer += data

   def _connected(self):

      self.write(b'\x03') # send ctrl+c

   def _handleError(self,  error):

      print(Console.red('TCP connection error:'), self.errorString())
      QCoreApplication.quit()
      sys.exit(1)
      