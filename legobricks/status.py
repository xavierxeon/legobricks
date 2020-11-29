#!/usr/bin/env puython3

class Status:

   class Vector:

      def __init__(self, data):

         self.x = data[0]
         self.y = data[1]
         self.z = data[2]

      def __str__(self):

         return '[{0}, {1}, {2}]'.format(self.x, self.y, self.z)

   def __init__(self, data):

      self.gyroscope = Status.Vector(data['gyroscope'])   
      self.position = Status.Vector(data['position'])   
      self.accelerometer = Status.Vector(data['accelerometer'])   
