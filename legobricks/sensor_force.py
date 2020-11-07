#!/usr/bin/env python3

from .helper import Device
from .version import Version

class SensorForce:

   def __init__(self, brick, port):

      Device.__init__(self, brick, port)
      self.storeName('force_sensor')

      self.sendCode("{0} = ForceSensor('{1}')".format(self._name, port))

   @staticmethod
   def header(version):

      if Version.RobotInventor == version:
         return ["from mindstorms import ForceSensor"]
      elif Version.SpikePrime == version:
         return ["from spike import ForceSensor"]
      else:
         return None      

   def isPressed(self):

      self.sendCode("pressed_{0} = {1}.is_pressed()".format(self._name, self._name))
      result = self.sendCode("print(pressed_{0})". format(self._name))
      return Device.valueFromArray(result, bool)
      
   def getForce(self):

      self.sendCode("force_newton_{0} = {1}.get_force_newton()".format(self._name, self._name))
      result = self.sendCode("print(force_newton_{0})".format(self._name))
      return Device.valueFromArray(result)      

   def getPercentage(self):

      self.sendCode("force_percentage_{0} = {1}.get_force_percentage()".format(self._name, self._name))
      result = self.sendCode("print(force_percentage_{0})".format(self._name))
      return Device.valueFromArray(result)      

   def waitUntilPressed(self):

      self.sendCode("{0}.wait_until_pressed()".format(self._name))

   def waitUntilReleased(self):

      self.sendCode("{0}.wait_until_released()".format(self._name))
