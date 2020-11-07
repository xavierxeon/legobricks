#!/usr/bin/env python3

from .helper import Device
from .version import Version

class Direction:

   Shortest = 'shortest path'
   Clockwise = 'clockwise'
   CounterClockwise = 'counterclockwise'
   
class MotorSingle(Device):

   def __init__(self, brick, port):

      Device.__init__(self, brick, port)
      self.storeName('motor')
      
      self.sendCode("{0} = Motor('{1}')".format(self._name, port))

   @staticmethod
   def header(version):

      if Version.RobotInventor == version:
         return ["from mindstorms import Motor"]
      elif Version.SpikePrime == version:
         return ["from spike import Motor"]
      else:
         return None


   def runDegrees(self, degrees, speed = None):

      self.sendCode("{0}.run_for_degrees({1}, {2})".format(self._name, degrees, speed))

   def runToPosition(self, degrees, direction = Direction.Shortest, speed = None):

      self.sendCode("{0}.run_to_position({1}, '{2}', {3})".format(self._name, degrees, direction, speed))

   def runSeconds(self, seconds, speed = None):

      self.sendCode("{0}.run_for_seconds({1}, {2})".format(self._name, seconds, speed))

   def start(self, speed = None):

      self.sendCode("{0}.start({1})".format(self._name, speed))

   def startAtPower(self, power):

      self.sendCode("{0}.start_at_power({1})".format(self._name, power))

   def stop(self):

      self.sendCode("{0}.stop()".format(self._name))

   def getSpeed(self):

      self.sendCode("speed_{0} = {1}.get_speed()".format(self._name, self._name))
      result = self.sendCode("print(speed_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getDefaultSpeed(self):

      self.sendCode("speed_{0} = {1}.get_default_speed()".format(self._name, self._name))
      result = self.sendCode("print(speed_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getPosition(self):

      self.sendCode("position_{0} = {1}.get_position()".format(self._name, self._name))
      result = self.sendCode("print(position_{0})".format(self._name))
      return Device.valueFromArray(result)

   def wasInterrupted(self):

      self.sendCode("interrupt_{0} = {1}.was_interrupted()".format(self._name, self._name))
      result = self.sendCode("print(interrupt_{0})". format(self._name))
      return Device.valueFromArray(result, bool)

   def setDefaultSpeed(self, speed):

      self.sendCode('{0}.set_default_speed({1})'.format(self._name, speed))


