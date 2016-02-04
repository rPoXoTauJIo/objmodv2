# ------------------------------------------------------------------------
# Project Reality debug module by rPoXo
#   wofdebug.py
#
# Description:
#
#   Provides various debug for wofspawner
#
# ------------------------------------------------------------------------
global G_TIME_START # global time, being set at start of round

import bf2
import host
import time
import os
import socket

import constants as C

G_TIME_START = 0
SOCK = None

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------
def init():
    global SOCK
    
    # create dgram udp socket
    try:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        debugEcho('Created socket')
    except socket.error:
        debugEcho('Failed to create socket')

    setStartTime()

# ------------------------------------------------------------------------
# setStartTime
# setting round start time
# ------------------------------------------------------------------------
def setStartTime():
    global G_TIME_START

    try:
        G_TIME_START = host.timer_getWallTime()
        debug('setStartTime(): successfully set start time at ' + str(G_TIME_START), 'time')
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
    timenow = round((host.timer_getWallTime() - G_TIME_START), 5)
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
def debugMessage(msg, types = None):
    debugs = {
        'file' : debugFile,  # debugging in files, set log path first
        'udp' : debugUDP,  # UDP debug, sending
        'echo' : debugEcho,  # printing debug to server console
        'ingame' : debugIngame
        }
    if types == None:
        for default_debug in C.DEBUGS_DEFAULT:
            debugs[default_debug](msg)
    else:
        for debug in types:
            debugs[debug](msg)

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
# debugUDP
# debug to UDP server
# ------------------------------------------------------------------------  
def debugUDP(msg):

    try:
        SOCK.sendto(msg, (C.CLIENTHOST, C.CLIENTPORT))
    except:
        debugEcho('debugUDP(): failed to send debug message')


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

# ------------------------------------------------------------------------
# debugFile
# debug in file
# ------------------------------------------------------------------------ 
def updateMessage(message):
    position = message['position']
    rotation = message['rotation']
    wall_time_now = message['time_wall']
    delta_time = message['time_delta']
    debugMessage('%s' % ())