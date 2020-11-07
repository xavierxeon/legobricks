#!/usr/bin/env python3

from .helper import Device
from .version import Version


class MotorPair(Device):

   def __init__(self, brick, portA, portB):

      Device.__init__(self, brick)
      self.storeName('motorpair' + portA + portB)
      
      self.sendCode("{0} = MotorPair('{1}, {2}')".format(self._name, portA, portB))

   @staticmethod
   def header(version):

      if Version.RobotInventor == version:
         return ["from mindstorms import MotorPair"]
      elif Version.SpikePrime == version:
         return ["from spike import MotorPair"]
      else:
         return None

