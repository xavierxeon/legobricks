#!/usr/bin/env python3

from ..device import Device

class Hub(Device):

   class Button:

      Left = 'left_button'
      Right = 'right_button'

      class Color:

         Azure = 'azure'
         Black = 'black'
         Blue = 'blue'
         Cyan = 'cyan'
         Green = 'green'
         Orange = 'orange'
         Pink = 'pink'
         Red = 'red'
         Violet = 'violet'
         Yellow = 'yellow'
         White = 'white'


   def __init__(self, brick):

      Device.__init__(self, brick, None)
      self.storeName('mshub')

      self.sendCode("{0} = MSHub()".format(self._name))

   @staticmethod
   def header():

      return ["from mindstorms import MSHub"]

   def waitUntilPressed(self, button):

      self.sendCode("{0}.{1}.wait_until_pressed()".format(self._name, button))

   def waitUntilReleased(self, button):

      self.sendCode("{0}.{1}.wait_until_released()".format(self._name, button))

   def wasPressed(self, button):

      self.sendCode("press_test_{0}_{1} = {2}.{3}.was_pressed()".format(self._name, button, self._name, button))
      result = self.sendCode("print(press_test_{0}_{1})".format(self._name, button))
      return Device.valueFromArray(result, bool)

   def statusLightOn(self, color):

      self.sendCode("{0}.status_light.on('{1}')".format(self._name, color))

   def statusLightOff(self):

      self.sendCode("{0}.status_light.off()")
         