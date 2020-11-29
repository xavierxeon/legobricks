#!/usr/bin/env python3

from .helper import Device
from .version import Version
from .status import Status

# from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair

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
      self.storeName('lego_hub')

      self.sendCode("{0} = Hub()".format(self._name))

   @staticmethod
   def header(version):

      if Version.RobotInventor == version:
         return ["import hub", "import ujson as json", "from mindstorms import MSHub as Hub"]
      elif Version.SpikePrime == version:
         return ["import hub", "import ujson as json", "from spike import PrimeHub as Hub"]
      else:
         return None

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
         
   def powerOff(self):

      self.sendCode("hub.power_off()")

   def info(self):      

      self.sendCode("hub_info  = hub.info()")
      result = self.sendCode("print(json.dumps(hub_info))")
      data = Device.dictFromArray(result)
      return data

   def status(self, raw = False):

      self.sendCode("hub_status = hub.status()")
      result = self.sendCode("print(json.dumps(hub_status))")
      data = Device.dictFromArray(result)
      if raw:
         return data
      else:
         return Status(data)

   def batteryInfo(self, raw = False):

      self.sendCode("hub_battery = hub.battery.info()")
      result = self.sendCode("print(json.dumps(hub_battery))")
      data = Device.dictFromArray(result)
      if raw:
         return data
      else:
         return int(data['battery_capacity_left'])

   def bluetoothInfo(self):

      self.sendCode("hub_bluetooth = hub.bluetooth.info()")         
      result = self.sendCode("print(json.dumps(hub_bluetooth))")
      data = Device.dictFromArray(result)
      return data
