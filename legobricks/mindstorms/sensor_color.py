#!/usr/bin/env python3

from ..device import Device

class SensorColor(Device):

   class Predefined:

      Black = 'black'
      Violet = 'violet'
      Blue = 'blue'
      Cyan = 'cyan'
      Green = 'green'
      Yellow = 'yellow'
      Red = 'red'
      White = 'white'

   def __init__(self, brick, port):

      Device.__init__(self, brick, port)
      self.storeName('color_sensor')

      self.sendCode("{0} = ColorSensor('{1}')".format(self._name, port))

   @staticmethod
   def header():

      return ["from mindstorms import ColorSensor"]

   def lightOff(self):

      self.lightAll(0)

   def lightAll(self, brightness = 100):

      self.sendCode("{0}.light_up_all({1})".format(self._name, brightness))

   def light(self, lightOne, lightTwo, lightThree):

      self.sendCode("{0}.light_up({1}, {2}, {3})".format(self._name, lightOne, lightTwo, lightThree))

   def getColor(self):

      self.sendCode("color_{0} = {1}.get_color()".format(self._name, self._name))
      result = self.sendCode("print(color_{0})".format(self._name))
      text = Device.valueFromArray(result, str)

      color = SensorColor._fromString(text)
      return color

   def getAmbientLight(self):

      self.sendCode("ambient_light_{0} = {1}.get_ambient_light()".format(self._name, self._name))
      result = self.sendCode("print(ambient_light_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getReflectedLight(self):

      self.sendCode("refelected_light_{0} = {1}.get_reflected_light()".format(self._name, self._name))
      result = self.sendCode("print(refelected_light_{0})".format(self._name))
      return Device.valueFromArray(result)
      
   def getRgbIntensity(self):

      self.sendCode("rgb_intensity_{0} = {1}.get_rgb_intensity()".format(self._name, self._name))
      result = self.sendCode("print(rgb_intensity_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getRed(self):

      self.sendCode("red_{0} = {1}.get_red()".format(self._name, self._name))
      result = self.sendCode("print(red_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getGreen(self):

      self.sendCode("green_{0} = {1}.get_green()".format(self._name, self._name))
      result = self.sendCode("print(green_{0})".format(self._name))
      return Device.valueFromArray(result)

   def getBlue(self):

      self.sendCode("blue_{0} = {1}.get_blue()".format(self._name, self._name))
      result = self.sendCode("print(blue_{0})".format(self._name))
      return Device.valueFromArray(result)

   def waitUntilColor(self, color):

      self.sendCode("{0}.wait_until_color('{1}')".format(self._name, color))
      result = self.sendCode("print('OK')")
      Device.valueFromArray(result, str)

   def waitForNewColor(self):

      self.sendCode("wait_color_{0} = {1}.wait_for_new_color()".format(self._name, self._name))
      result = self.sendCode("print(wait_color_{0})".format(self._name))
      text = Device.valueFromArray(result, str)

      color = SensorColor._fromString(text)
      return color

   @staticmethod
   def _fromString(text):

      available = {
         'black': SensorColor.Predefined.Black,
         'violet': SensorColor.Predefined.Violet,
         'blue': SensorColor.Predefined.Blue,
         'cyan': SensorColor.Predefined.Cyan,
         'green': SensorColor.Predefined.Green,
         'yellow': SensorColor.Predefined.Yellow,
         'red': SensorColor.Predefined.Red,
         'white': SensorColor.Predefined.White
      }

      if not text in available:
         return None

      return available[text]
