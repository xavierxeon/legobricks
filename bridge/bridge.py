#!/usr/bin/env python3

import signal, sys, os, argparse
from PySide2.QtCore import QTimer, QCoreApplication, QCommandLineParser, QCommandLineOption

from lib import Settings, Console, Server

def signit_handler(*args):

    QCoreApplication.quit()

def banner():

   print(Console.green(' ---------------------', True))
   print(' ' + Console.green('|', True) + '  ' + Console.blue('O', True) + '                ' + Console.green('|', True) + '')
   print(' ' + Console.green('|', True) + '         ' + Console.yellow('X', True) + '         ' + Console.green('|', True) + '')
   print(' ' + Console.green('|', True) + '       ' + Console.yellow('X X X', True) + '       ' + Console.green('|', True) + '')
   print(' ' + Console.green('|', True) + '     ' + Console.yellow('X X X X X', True) + '     ' + Console.green('|', True) + '')
   print(' ' + Console.green('|', True) + ' ' + Console.grey('MINDSTORMS BRIDGE') + ' ' + Console.green('|', True) + '')
   print(Console.green(' ---------------------', True))

def main():

   app = QCoreApplication([])
   signal.signal(signal.SIGINT, signit_handler)

   timer = QTimer()
   timer.start(500)  
   timer.timeout.connect(lambda: None)

   parser = argparse.ArgumentParser(description = 'Map a LEG Mindstorms serial port onto a tcp port.')
   parser.add_argument('--create', help = 'Create a new settings file.', action = 'store_true')
   parser.add_argument('--load', help = 'Load existing settings file.', nargs = 1, action = 'store')

   args = parser.parse_args()

   if args.create:
      fileName =  os.getcwd() + "/Settings.json"
      if not Settings.create(fileName):
         print(Console.red('unable to create settings file: ') + fileName)
         sys.exit(1)
      else:
         print(Console.magenta('check and/or edut values in settings file: ') + fileName)
         sys.exit(0)

   settingsFileName = args.load
   if not settingsFileName:
      parser.print_help()
      sys.exit(1)

   settingsFileName = settingsFileName[0]   

   try:
      print()
      banner()
      
      serverList = list() # to keep server in scope
      settings = Settings(settingsFileName)
      for entry in settings.iterate():
         server = Server(entry)
         serverList.append(server)
      
      print()
      return app.exec_()
   except Exception as e:
      print(Console.red(str(e)))
      sys.exit(1)


if __name__ == '__main__':
   main()
