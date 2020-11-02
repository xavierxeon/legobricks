#!/usr/bin/env python3

import json, os, platform
from PySide2.QtSerialPort import QSerialPortInfo

from .console import Console

class Settings:

   class Server:

      def __init__(self, dataDict):

         self.name = dataDict['Name']
         self.usbDevice = dataDict['UsbDevice']
         self.bluetoothDevice = dataDict['BluetoothDevice']
         self.serverPort = int(dataDict['ServerPort'])

   def __init__(self, fileName):

      if not os.path.exists(fileName):
         raise Exception(Console.red('unalbe to open settings file: ') + fileName)

      with open(fileName, 'r') as infile:
         data = json.load(infile)

      self.serverList = list()
      for entry in data:
         server = Settings.Server(entry)
         self.serverList.append(server)   

   @staticmethod
   def create(fileName):

      channelData = {
         'Name': str(),
         'UsbDevice': str(),
         'BluetoothDevice': str(),
         'ServerPort': 51515
      }

      operatingSystem = platform.system()
      if 'Darwin' == operatingSystem:
         channelData['BluetoothDevice'] = '/dev/tty.LEGOHubRobo-SerialPortP'
      elif 'Windows' == operatingSystem:
         channelData['BluetoothDevice'] = '\\\\.\\COM1'

      for info in QSerialPortInfo.availablePorts():
         if not info.portName().startswith('tty.'):
            continue
         if info.manufacturer() != 'LEGO System A/S':
            continue 
         channelData['UsbDevice'] = info.systemLocation()
         break

      data = [channelData]

      with open(fileName, 'w') as outfile:
         json.dump(data, outfile, indent = 3)

      return True

   def iterate(self):

      for entry in self.serverList:
         yield entry

      return None
