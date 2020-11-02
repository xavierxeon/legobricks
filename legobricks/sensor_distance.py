#!/usr/env/bin python3

from ..device import Device

class SensorDistance(Device):

   def __init__(self, brick, port):

      Device.__init__(self, brick, port)
      self.storeName('distance_sensor')

      self.sendCode("{0} = DistanceSensor('{1}')".format(self._name, port))

   @staticmethod
   def header():

      return ["from mindstorms import DistanceSensor"]

   def lightOff(self):

      self.lightAll(0)

   def lightAll(self, brightness = 100):

      self.sendCode("{0}.light_up_all({1})".format(self._name, brightness))

   def light(self, topRight, topLeft, bottomRight, bottomLeft):

      self.sendCode("{0}.light_up({1}, {2}, {3}, {4})".format(self._name, topRight, topLeft, bottomRight, bottomLeft))

   def getDistance(self, shortRange = False):

      self.sendCode("distance_{0} = {1}.get_distance_cm({2})".format(self._name, self._name, shortRange))
      result = self.sendCode("print(distance_{0})".format(self._name))
      distanceInCentimeter = Device.valueFromArray(result)
      if not distanceInCentimeter:
         return -1
      return 10 * distanceInCentimeter

   def waitUntilDistanceOver(self, distance, shotRange = False):

      self.sendCode("{0}.wait_for_distance_farther_than({1}, 'cm', {2})".format(self._name, 0.1 * distance, shotRange))
      result = self.sendCode("print('OK')")
      Device.valueFromArray(result, str)

   def waitUntilDistanceUnder(self, distance, shotRange = False):

      self.sendCode("{0}.wait_for_distance_closer_than({1}, 'cm', {2})".format(self._name, 0.1 * distance, shotRange))
      result = self.sendCode("print('OK')")
      Device.valueFromArray(result, str)
