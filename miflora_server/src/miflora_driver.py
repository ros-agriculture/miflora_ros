#!/usr/bin/env python3.7

'''
HACK:  This driver requires python >= 3.6.

It is called from a ROS script to allow using a different version
  of python than what ROS is using.
'''

import sys
from miflora.miflora_poller import *
from btlewrap import BluepyBackend
from miflora import miflora_scanner 


def main(arg):
    ''' Connects to BL and reads measurements from sensor. 
        Returns measurements or exception error.           '''

    readings = {
        "soil-temperature": MI_TEMPERATURE,
        "soil-moisture": MI_MOISTURE,
        "light": MI_LIGHT,
        "soil-ec": MI_CONDUCTIVITY,
        "battery": MI_BATTERY,
    }

    measurements = {}

    try:
        poller = MiFloraPoller(arg, BluepyBackend, cache_timeout=900)
        for key, code in readings.items():
            value = poller.parameter_value(code)
            if value is not None:
                measurements[key] = value
        print(measurements)
    except Exception as e:
        print("No device found.  " + str(e))


if __name__ == "__main__":
    main(sys.argv[1])