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

   def stop(self):

      self.sendCode("{0}.stop()".format(self._name))

   def move(self, distanceInCentimeter, steering = 0, speed = None):

      self.sendCode("{0}.move({1}, 'cm', {2}, {3})".format(self._name, distanceInCentimeter, steering, speed))

   def start(self, steering = 0, speed = None):

      self.sendCode("{0}.start({1}, {2})".format(self._name, steering, speed))

   def startAtPower(self, power, steering = 0):

      self.sendCode("{0}.start_at_power({1}, {2})".format(self._name, power, steering))

   def moveTank(self, distanceInCentimeter, leftSpeed = None, rightSpeed = None):

      self.sendCode("{0}.move_tank({1}, 'cm', {2}, {3})".format(self._name, distanceInCentimeter, leftSpeed, rightSpeed))

   def startTank(self, leftSpeed, rightSpeed):

      self.sendCode("{0}.start_tank({1}, {2})".format(self._name, leftSpeed, rightSpeed))

   def startTankAtPower(self, leftPower, rightPower):

      self.sendCode("{0}.start_tank_at_power({1}, {2})".format(self._name, leftPower, rightPower))

   def getDefaultSpeed(self):

      self.sendCode("speed_{0} = {1}.get_default_speed()".format(self._name, self._name))
      result = self.sendCode("print(speed_{0})".format(self._name))
      return Device.valueFromArray(result)


   def setDefaultSpeed(self, speed):

      self.sendCode('{0}.set_default_speed({1})'.format(self._name, speed))

   def setMotorRotation(self, distanceInCentimeter):

      self.sendCode("{0}.set_motor_rotation({1}, 'cm')".format(self._name, distanceInCentimeter))
