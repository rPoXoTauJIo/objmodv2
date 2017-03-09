# -------------------------------------------
# constants file
#
# ~ constants.py
#
# -------------------------------------------

# command key for chat commands
COMMANDKEY = '!obj'

# address and port for listening UDP server
SERVERHOST = 'localhost'  # Symbolic name meaning all available interfaces
SERVERPORT = 8888  # Arbitrary non-privileged port

# address and port for streaming client
CLIENTHOST = 'localhost'  # Symbolic name meaning all available interfaces
CLIENTPORT = 8888  # Arbitrary non-privileged port

# path to expor file
# keep in mind that if path does not exist - log file won't be created
LOGFILENAME = '/objmodv2.log'


# setting debug level, uncomment required debug
DEBUGS = [
    'file',  # debugging in files, set log path first
    'udp',  # UDP debug, sending
    'echo',  # printing debug to server console
    'ingame'  # printing debug ingame
    ]

DEBUGS_DEFAULT = [
    'file', # debugging in files, set log path first
    'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
    ]



DEFAULT_QUERIES = {
    'us_jet_f16' : {
        'us_jet_f16_Wing_Front' : [
            'ObjectTemplate.setWingLift 0.5',
            'ObjectTemplate.setFlapLift 0.0',
            ],
        'us_jet_f16_Winglet' : [
            'ObjectTemplate.setMinRotation 0/-15/0',
            'ObjectTemplate.setMaxRotation 0/20/0',
            'ObjectTemplate.setMaxSpeed 0/1000/0',
            'ObjectTemplate.setAcceleration 0/-150/0',
            'ObjectTemplate.setWingLift 0.5',
            'ObjectTemplate.setFlapLift 0.15',
            ],
        'us_jet_f16_Flaps_L' : [
            'ObjectTemplate.setMinRotation 0/-5/0',
            'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/300/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            ],
        'us_jet_f16_Flaps_R' : [
            'ObjectTemplate.setMinRotation 0/-5/0',
            'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/300/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            ],
        },
    'ru_jet_su27' : {
        'ru_jet_su27_Wing_Front' : [
            'ObjectTemplate.setWingLift 0.7',
            'ObjectTemplate.setFlapLift 0.0',
            ],
        'ru_jet_su27_Winglet' : [
            'ObjectTemplate.setMinRotation 0/-5/0',
            'ObjectTemplate.setMaxRotation 0/10/0',
            'ObjectTemplate.setMaxSpeed 0/300/0',
            'ObjectTemplate.setAcceleration 0/-150/0',
            'ObjectTemplate.setWingLift 0.6',
            'ObjectTemplate.setFlapLift 0.35',
            ],
        'ru_jet_su27_Flaps_L' : [
            'ObjectTemplate.setMinRotation 0/-5/0',
            'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/300/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            ],
        'ru_jet_su27_Flaps_R' : [
            'ObjectTemplate.setMinRotation 0/-5/0',
            'ObjectTemplate.setMaxRotation 0/10/0',
            #'ObjectTemplate.setMaxSpeed 0/300/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            ],
        'ru_jet_su27_EngineMain' : [
            'ObjectTemplate.setMaxRotation 0/0/5000',
            'ObjectTemplate.setMaxSpeed 0/0/500',
            'ObjectTemplate.setAcceleration 0/0/100',
            #'ObjectTemplate.setMaxSpeed 0/300/0',
            #'ObjectTemplate.setAcceleration 0/-150/0',
            ],
        },
    'us_the_mv22' : {
        'us_the_mv22_Wing_Front' : [
            'ObjectTemplate.setPositionOffset 0/0/10',
            'ObjectTemplate.setWingLift 0.8',
            'ObjectTemplate.setFlapLift 0.0',
            ],
        'us_the_mv22_Winglet' : [
            'ObjectTemplate.setAcceleration 0/-150/0',
            'ObjectTemplate.setWingLift 0.8',
            'ObjectTemplate.setFlapLift 0.45',
            ],
        'us_the_mv22_LFrontFlaps01' : [
            'ObjectTemplate.setWingLift 0.35',
            'ObjectTemplate.setFlapLift 0.15',
            ],
        'us_the_mv22_RFrontFlaps01' : [
            'ObjectTemplate.setWingLift 0.35',
            'ObjectTemplate.setFlapLift 0.15',
            ],
        'us_the_mv22_RudderYaw' : [
            'ObjectTemplate.setWingLift 0.6',
            'ObjectTemplate.setFlapLift 0.1',
            ],
        }
    }