# -------------------------------------------
# constants file
#
# ~ constants.py
#
# -------------------------------------------

# command key for chat commands
COMMANDKEY = '!obj'

# keyword for reloading constants file
KEYWORD_RELOAD = 'reload'

# will get applied on round start
TWEAKS = {
    'ger_ahe_tiger' : {
        'ger_ahe_tiger_WingL' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-1.0',
            #'ObjectTemplate.setWingLift 0.5',
            #'ObjectTemplate.setFlapLift 0.1',
            ],
        'ger_ahe_tiger_WingR' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-1.0',
            #'ObjectTemplate.setWingLift 0.5',
            #'ObjectTemplate.setFlapLift 0.1',
            ],
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
        'ger_ahe_tiger_BodyWing' : [
            #'ObjectTemplate.setMinRotation 0/-5/0',
            #'ObjectTemplate.setMaxRotation 0/5/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-50/0',
            #'ObjectTemplate.setPositionOffset -5.0/0.0/0.0',
            #'ObjectTemplate.setWingLift 1.0',
            #'ObjectTemplate.setFlapLift 0.35'
            ],
        'ger_ahe_tiger_Rudder' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/50/0',
            #'ObjectTemplate.setAcceleration 0/-50/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.5/-3.0',
            #'ObjectTemplate.setWingLift 3.5',
            #'ObjectTemplate.setFlapLift 0.15'
            ],
        },
    
    'us_jet_a10a' : {
        'us_jet_a10a_Wing_Front' : [
            #'ObjectTemplate.setPositionOffset 0.0/0.0/10.5',
            #'ObjectTemplate.setWingLift 0.65',
            #'ObjectTemplate.setFlapLift 0.0',
            ],
        'us_jet_a10a_Winglet_Back' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-10.0',
            #'ObjectTemplate.setWingLift 0.4',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_FlapsL' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset -7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'us_jet_a10a_FlapsR' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 7.0/0.0/2.5',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'us_jet_a10a_Wing_Vertical' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/5.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_Wing_Rudder' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/0.0',
            #'ObjectTemplate.setWingLift 0.1',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'us_jet_a10a_EngineMain' : [
            #'ObjectTemplate.setMaxSpeed 0/0/500',
            #'ObjectTemplate.setAcceleration 0/0/120',
            #'ObjectTemplate.setTorque 140',
            #'ObjectTemplate.setDifferential 140',
            ],
        },

    'ru_jet_su39' : {
        'ru_jet_su39_Wing_Front' : [
            #'ObjectTemplate.setPositionOffset 0.0/0.0/20.0',
            #'ObjectTemplate.setWingLift 0.4',
            #'ObjectTemplate.setFlapLift 0.0',
            ],
        'ru_jet_su39_Winglet' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-10.0',
            #'ObjectTemplate.setWingLift 0.145',
            #'ObjectTemplate.setFlapLift 0.35',
            ],
        'ru_jet_su39_Flaps_L' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset -5.0/0.0/-1.5',
            #'ObjectTemplate.setWingLift 0.2',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'ru_jet_su39_Flaps_R' : [
            #'ObjectTemplate.setMinRotation 0/-10/0',
            #'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 5.0/0.0/-1.5',
            #'ObjectTemplate.setWingLift 0.2',
            #'ObjectTemplate.setFlapLift 0.2',
            ],
        'ru_jet_su39_BodyWingVertical' : [
            #'ObjectTemplate.setMinRotation 0/-20/0',
            #'ObjectTemplate.setMaxRotation 0/15/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/-750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/5.0',
            #'ObjectTemplate.setWingLift 0.5',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'ru_jet_su39_RudderYaw' : [
            #'ObjectTemplate.setMinRotation 0/-2/0',
            #'ObjectTemplate.setMaxRotation 0/2/0',
            #'ObjectTemplate.setMaxSpeed 0/1000/0',
            #'ObjectTemplate.setAcceleration 0/750/0',
            #'ObjectTemplate.setPositionOffset 0.0/0.0/-10.0',
            #'ObjectTemplate.setWingLift 0.3',
            #'ObjectTemplate.setFlapLift 0.4',
            ],
        'ru_jet_su39_EngineMain' : [
            #'ObjectTemplate.setMinRotation 0/0/0',
            #'ObjectTemplate.setMaxRotation 0/0/1500',
            #'ObjectTemplate.setMaxSpeed 0/0/100',
            #'ObjectTemplate.setAcceleration 0/0/60',
            #'ObjectTemplate.setTorque 90',
            #'ObjectTemplate.setDifferential 160',
            ],
        ### TESTING ###
        'ru_jet_su39_GearRotator' : [
            #'ObjectTemplate.setGearUpHeight 10',
            #'ObjectTemplate.setGearUpSpeed 70',
            #'ObjectTemplate.setGearUpDelay 0.0',
            #'ObjectTemplate.setGearDownDelay 0.8', # rotator, should be longer than Lgear delay but not longer than rotation itself
            ],
        'ru_jet_su39_R_LGear' : [
            #'ObjectTemplate.setGearUpHeight 10',
            #'ObjectTemplate.setGearUpSpeed 70',
            #'ObjectTemplate.setGearUpDelay 0.4', # turn right delay
            #'ObjectTemplate.setGearDownDelay 0.4',
            ],
        'ru_jet_su39_9A4172_Launcher' : [
            #'ObjectTemplate.postProcess.tvDistortionScale 0.0',
            #'ObjectTemplate.postProcess.tvDistortionFreq 0.0',
            #'ObjectTemplate.postProcess.tvDistortionRoll 0.0',
            #'ObjectTemplate.postProcess.tvInterference 0.2',
            ],
        },
    
    }