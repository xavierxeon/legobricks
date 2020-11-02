#!/usr/bin/env python3

from .helper import Device, MidiNote
from .hub import Hub

class Speaker:

   def __init__(self, hub):

      self._name = 'speaker'
      self._hub = hub

      self._hub.sendCode("{0} = {1}.speaker".format(self._name, self._hub._name))

   def beep(self, note, duration):

      if isinstance(note, str):
         note = MidiNote.convert(note)

      if note < 44 or note > 123:
         raise ValueError('note is not within the allowed range of 44-123.')

      self._hub.sendCode("{0}.beep({1}, {2})".format(self._name, note, duration))

   def startBeep(self, note):

      if isinstance(note, str):
         note = MidiNote.convert(note)

      if note < 44 or note > 123:
         raise ValueError('note is not within the allowed range of 44-123.')

      self._hub.sendCode("{0}.start_beep({1})".format(self._name, note))

   def stop(self):

      self._hub.sendCode("{0}.stop()".format(self._name))

   def getVolume(self):

      self._hub.sendCode("volume = {0}.get_volume()".format(self._name))
      result = self._hub.sendCode("print(volume)")
      return Device.valueFromArray(result)

   def setVolume(self, volume):

      self._hub.sendCode("{0}.set_volume({1})".format(self._name, volume))
