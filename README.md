# Control LEGO microopython brick from a pc or mac

The python version on a LEGO micropython brick, such as currently 
shipped with Robot Inventor or Spike Prime does not feature great library support.

This project therefore aims to make a robot program run on a pc or mac, using a full desktop python.
This gives a programmer more flexebility (e.g install packages with pip), at the cost of more latnecy.

## HOWTO

* (once) connect your brick to your compuiter using the provided LEGO app
+ (once) close your LEGO app
* (once) start the bridge app with the "--create" command paramter
* (once) edit the created settings file
* as a super user start the bridge with the settings file
   * it is possible to start the bridge with several bricks connected
* run a program ;-)

## NOT TESTED

* windows serial paths (in bridge)
* spike prime support

## NOT YET IMPLEMENTED

* linux support
* force sensor
* motor pairs
