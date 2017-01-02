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
LOGFILENAME = '/logs/objmod.log'


# setting debug level, uncomment required debug
DEBUGS = [
    'file',  # debugging in files, set log path first
    'udp',  # UDP debug, sending
    'echo',  # printing debug to server console
    'ingame'  # printing debug ingame
]

DEBUGS_DEFAULT = [
    #'file', # debugging in files, set log path first
    #'udp', # UDP debug, sending
    'echo',  # printing debug to server console
    #'ingame' # printing debug ingame
]

TEMPLATE_PROPERTIES = {
    3: {
        'minrot': 'setMinRotation',
        'maxrot': 'setMaxRotation',
        'setpivot': 'setPivotPosition',
        'maxspeed': 'setMaxSpeed',
        'acc': 'setAcceleration',
        'deacc': 'setDeAcceleration',
        'modinertia': 'inertiaModifier',
        'moddrag': 'dragModifier',
        'inertwreck': 'InertiaModifierForWreck',
        'posoffset': 'setPositionOffset',
        'setpos': 'setPosition',
        'setrot': 'setRotation',
        'chaseoffset': 'chaseOffset',
        'centermassoffset': 'centerOfMassOffset',

    },
    1: {
        'drag': 'drag',
        'mass': 'mass',
        'torque': 'setTorque',
        'diff': 'setDifferential',
        'gearup': 'setGearUp',
        'geardown': 'setGearDown',
        'strength': 'setStrength',
        'damping': 'setDamping',
        'autoreset': 'setAutomaticReset',
        'pitchoffset': 'setPitchOffset',
        'winglift': 'setWingLift',
        'flaplift': 'setFlapLift',
        'nopropeffectspeed': 'noPropellerEffectAtSpeed',
        'noeffectspeed': 'noEffectAtPerpSpeed',
        'angledefault': 'defaultAngleOfAttack',
        'anglemax': 'maxAngleOfAttack',
        'attackspeed': 'attackSpeed',
        'force': 'constantForce',
        'startdelay': 'startDelay',
        'ammo': 'ammo.magSize',
        'camera_flyby': 'CVMFlyBy',
        'camera_chase': 'CVMChase',
        'modgravity': 'gravityModifier',
        'reminput': 'rememberExcessInput',
        'grip': 'grip',
        'devmin': 'deviation.minDev',
        'firerate': 'fire.roundsPerMinute',

    },

}

DEFAULT_QUERIES = {
    # those are settings for modified stuff, use them as example
    'us_jet_f15': [
        ['us_jet_f15_WingVertical', 'winglift', '0.1'],
        ['us_jet_f15_WingVertical', 'flaplift', '0.0'],

        ['us_jet_f15_Rudder', 'winglift', '0.0'],
        ['us_jet_f15_Rudder', 'flaplift', '0.2'],
        
        ['us_jet_f15_Winglet_Back', 'winglift', '1.0'],
        ['us_jet_f15_Winglet_Back', 'flaplift', '1.0'],
        
        ['us_jet_f15_Camera', 'camera_flyby', '1'],
        ['us_jet_f15_Camera', 'camera_chase', '1'],
        
    ],
}
