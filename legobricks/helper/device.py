#!/usr/bin/env python3

import json

from ..version import Version

class Device:

   def __init__(self, brick, port = None):

      self._name = None

      self._brick = brick
      self._port = port

   def sendCode(self, code):

      return self._brick.sendCode(code)

   def storeName(self, prefix):
      
      if self._port:
         self._name = prefix + self._port
      else:
         self._name = prefix

   @staticmethod
   def valueFromArray(result, valueType = int):

      if not isinstance(result, list) or len(result) < 1:
         return None

      value = result[0]
      if valueType == bool:
         value = (result[0] == 'True')
      elif value == 'None':
         return None
         
      return valueType(value)

   @staticmethod
   def dictFromArray(result):

      if not isinstance(result, list) or len(result) < 1:
         return None

      text = result[0]
      text = text.replace("'", '"')
      data = json.loads(text)
      return data

   @classmethod
   def iterSubclasses(cls):

      for subclass in cls.__subclasses__():
         yield from subclass.iterSubclasses() #recurse for further inheritance
         yield subclass 

   @staticmethod
   def header(version):

      return None         

   @staticmethod
   def setAllHeaders(brick, version):

      for subClass in Device.iterSubclasses():
         header = subClass.header(version)
         if not header:
            continue
         if not isinstance(header, list):
            header = [ header ]
         for code in header:
            brick.sendCode(code)
