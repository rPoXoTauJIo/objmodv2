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
    'ger_ahe_tiger_rotor' : [
        #'ObjectTemplate.setMaxRotation 0/0/1400',
        #'ObjectTemplate.setMaxSpeed 0/0/1',
        #'ObjectTemplate.setAcceleration 0/0/20',
        #'ObjectTemplate.setDeAcceleration 0/0/200',
        #'ObjectTemplate.setUseDeAcceleration 1',
        #'ObjectTemplate.maxAngleOfAttack 12',
        #'ObjectTemplate.attackSpeed 60',
        #'ObjectTemplate.setTorque 70',
        #'ObjectTemplate.setDifferential 200',
        #'ObjectTemplate.defaultAngleOfAttack -20',
        #'ObjectTemplate.horizontalSpeedMagnifier 3.0',
        #'ObjectTemplate.decreaseAngleToZeroVerticalVel 0.01',
        #'ObjectTemplate.defaultAngleOfAttack 0.0',
        #'ObjectTemplate.horizontalDampAngle 0.1',
        #'ObjectTemplate.horizontalDampAngleFactor 0.001',
        ],
    'ru_jet_su39_9A4172_Launcher' : [
        #'ObjectTemplate.postProcess.tvDistortionScale 0.0',
        #'ObjectTemplate.postProcess.tvDistortionFreq 0.0',
        #'ObjectTemplate.postProcess.tvDistortionRoll 0.0',
        #'ObjectTemplate.postProcess.tvInterference 0.2',
        ],
    'ru_ahe_mi24_Camera' : [
        'ObjectTemplate.CVMChase 1',
        'ObjectTemplate.CVMFrontChase 1',
        'ObjectTemplate.CVMFlyBy 1',
        'ObjectTemplate.nosePos 0/0/2.25',
        ],
    }
```
3. Type ``!obj reload`` in game chat.  
This will reload ``constants`` module with our values, and will loop over objects and tweak calls
F.e. in our case, i've changed wings offset and lift values which will affect flight physics.

## NOTE:

This module initially only were intended to change wings lift values, and their offsets. Its confirmed than it wont change anything regarding visual part, f.e. ``.maxRotation`` on **visible** ``RotationalBundle``.  
In PR mod i have only non-visible **networkable** wings affecting flight physics so it didn't bother me, but for other mods like *fh2* or *aix2* it may matter.  
Test other commands on your own.
