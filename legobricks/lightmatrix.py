#!/usr/bin/env python3

from .hub import Hub

class LightMatrix:

   def __init__(self, hub):

      self._name = 'lightmatrix'
      self._hub = hub

      self._hub.sendCode("{0} = {1}.light_matrix".format(self._name, self._hub._name))

   def write(self, text):

      self._hub.sendCode("{0}.write('{1}')".format(self._name, text))

   def setPixel(self, x, y, brightness = 100):

      self._hub.sendCode("{0}.setPixel({1}, {2}, {3})".format(self._name, x, y, brightness))

   def off(self):

      self._hub.sendCode("{0}.off()".format(self._name))

   def showImage(self, image, brightness = 100):

      self._hub.sendCode("{0}.sendImage({1}, {2})".format(self._name, image, brightness))
