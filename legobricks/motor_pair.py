#!/usr/bin/env python3

from helper import Device

from .brick import Firmware


class MotorPair(Device):

   def __init__(self, brick, portA, portB):

      Device.__init__(self, brick)
      self.storeName('motorpair' + portA + portB)
      
      self.sendCode("{0} = MotorPair('{1}, {2}')".format(self._name, portA, portB))

   @staticmethod
   def header(firmware):

      if Firmware.RobotInventor == firmware:
         return ["from mindstorms import MotorPair"]
      elif Firmware.SpikePrime == firmware:
         return ["from spike import MotorPair"]
      else:
         return None

