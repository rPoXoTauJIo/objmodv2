# objmodv2
A python module for live-tweaking objects in bf2 engine through host.rcon_invoke.  

Installing:  
1. Clone repo to ``<mod_root>/python/game``  
2. Add ``import objmodv2`` to ``<mod_root>/python/game/__init__.py``  

Usage:
1. Launch server\game
2. Uncomment some values in ``constants.py``, like in example
```python
TWEAKS = {
    'AIX_F16' : {
        'AIX_F16_RWinglet' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            'ObjectTemplate.setPositionOffset 0/0.0/0',
            'ObjectTemplate.setWingLift -0.75',
            'ObjectTemplate.setFlapLift 1.5',
            ],
        'AIX_F16_LWinglet' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/150/0',
            'ObjectTemplate.setPositionOffset 0/0.0/0',
            'ObjectTemplate.setWingLift -0.75',
            'ObjectTemplate.setFlapLift 1.5',
            ],
        },
```
3. Type ``!obj reload`` in game chat.  
This will reload ``constants`` module with our values, and will loop over objects and tweak calls
F.e. in our case, i've changed wings offset and lift values which will affect flight physics.

## NOTE:
This module initially only were intended to change wings lift values, and their offsets. Its confirmed than it wont change anything regarding visual part, f.e. ``.maxRotation`` on **visible** ``RotationalBundle``.  
In PR mod i have only non-visible **networkable** wings affecting flight physics so it didn't bother me, but for other mods like *fh2* or *aix2* it may matter.  
Test other commands on your own.
