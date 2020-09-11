#!/usr/bin/env python3.7

from btlewrap import BluepyBackend
from miflora import miflora_scanner 

backend = BluepyBackend
devices = miflora_scanner.scan(backend, 10)
print('Found {} devices:'.format(len(devices)))
for device in devices:
    print('{}'.format(device))