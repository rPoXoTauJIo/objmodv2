# ------------------------------------------------------------------------
# Project Reality debug module by rPoXo
#   wofdebug.py
#
# Description:
#
#   Provides various debug for wofspawner
#
# ------------------------------------------------------------------------
global g_startTime # global time, being set at start of round

import bf2
import host
import time
import os

import constants as C

g_startTime = 0
socket = None

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    global socket

    setStartTime()

# ------------------------------------------------------------------------
# setStartTime
# setting round start time
# ------------------------------------------------------------------------
def setStartTime():
    global g_startTime

    try:
        g_startTime = host.timer_getWallTime()
        debug('setStartTime(): successfully set start time at ' + str(g_startTime), 'time')
    except:
        debug('setStartTime(): failed to reset start time', 'time' )


# ------------------------------------------------------------------------
# sendMessageToAll
# send message to all ingame
# ------------------------------------------------------------------------          
def sendMessageToAll(msg):
    try:
        host.rcon_invoke("game.sayAll \"" + str(msg) + "\"")
    except:
        host.rcon_invoke("game.sayAll \"" + 'sendMessageToAll(): failed to display message' + "\"")


# ------------------------------------------------------------------------
# echoMessage
# send message to server console
# ------------------------------------------------------------------------  
def echoMessage(msg):
    try:
        host.rcon_invoke("echo \"" + str(msg) + "\"")
    except:
        host.rcon_invoke("echo \"" + 'sendMessageToAll(): failed to display message' + "\"")


# ------------------------------------------------------------------------
# time_now
# returning time spent from start
# ------------------------------------------------------------------------  
def time_now():
    timenow = round((host.timer_getWallTime() - g_startTime), 5)
    return timenow


# ------------------------------------------------------------------------
# time_string_now
# returning formatted time string spent from start
# ------------------------------------------------------------------------  
def time_string_now(length = 8):
    timestring = str(time_now())
    while len(timestring) < length:
        timestring +='0'
    return timestring

# ------------------------------------------------------------------------
# debug
# simple func to create debug output
# ------------------------------------------------------------------------  
def debug(msg, types = None):

    debugTypes = {
        'file': debugFile,
        'echo': debugEcho,
        'ingame': debugIngame
        }

    # debug type specified, using filtered debug
    if types != None:
        # no debug types in C module, using hardcoded defaults
        if len(C.debugLevel) == 0:
            for type in types:
                debugTypes[type](msg)
        # debug type are in C module, using enabled only
        elif len(C.debugLevel) != 0:
            for type in types:
                if type in C.debugLevel and type in debugTypes:
                    debugTypes[type](msg)
    # no debug type specified, using default from C module
    elif types == None:
        for debugType in debugTypes.keys():
            if debugType in C.debugLevel:
                debugTypes[debugType](msg)
    else:
        # sending ingame sessage if debug enabled
        debugEcho(msg)


# ------------------------------------------------------------------------
# debugPublic
# debug ingame
# ------------------------------------------------------------------------  
def debugIngame(msg):
    sendMessageToAll(msg)


# ------------------------------------------------------------------------
# debugEcho
# debug in server console
# ------------------------------------------------------------------------  
def debugEcho(msg):
    echoMessage(msg)


# ------------------------------------------------------------------------
# debugFile
# debug in file
# ------------------------------------------------------------------------  
def debugFile(msg):

    try:
        fileName = host.sgl_getModDirectory() + C.spawnerLogPath
        logFile = open(fileName, 'a')
        logTime = time_string_now()
        logFile.write('t: ' + str(logTime) + ' ' + str(msg) + '\n')
        logFile.close()
    except:
        pass
