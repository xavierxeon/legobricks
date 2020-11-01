#!/usr/bin/env python3

import signal, sys
from PySide2.QtCore import QTimer, QCoreApplication


def signit_handler(*args):

    QCoreApplication.quit()

def mainLoopConsole(setupFunction, runEventLoop = True):

   app = QCoreApplication([])
   signal.signal(signal.SIGINT, signit_handler)

   timer = QTimer()
   timer.start(500)  
   timer.timeout.connect(lambda: None)

   setupFunction()

   if runEventLoop:
      result = app.exec_()
      sys.exit(result)      
