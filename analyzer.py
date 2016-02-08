# --------------------------------------------------------------------------
# udp_server.py
#
# Description:
#
#   Simple udp socket server for testing
#   Listening for udp messages
#
# Credits:
#   Simple udp socket server
#   Silver Moon (m00n.silv3r@gmail.com)
#
# -------------------------------------------------------------------------
import socket
import sys
import time
import pickle
import constants as C
from datetime import datetime

G_TIME_START = 0
CURRENTCLIENT = None
SOCK = None
LOGFILENAME = None


class MessageDebug:

    def __init__(self, data):
        self.message = data['msg']

    def writeOutput(self, display=False):
        debugFile(self.message)
        if display:
            print(self.message)


class MessageUpdate:

    def __init__(self, data):
        self.position = data['msg']['position']
        self.rotation = data['msg']['rotation']
        self.time_wall = data['msg']['time_wall']
        self.time_delta = data['msg']['time_delta']
        self.time_epoch = data['msg']['time_epoch']
        self.time_ping = time.time() - self.time_epoch

    def writeOutput(self, display=False):
        debugFile(
            'Delta: {3}\nPing: {5}\nPosition: {0}\nRotation: {1}\n'.format(
                self.position,
                self.rotation,
                self.time_wall,
                self.time_delta,
                self.time_epoch,
                self.time_ping))
        if display:
            print(
                'Delta: {3}\nPing: {5}\nPosition: {0}\nRotation: {1}\n'.format(
                    self.position,
                    self.rotation,
                    self.time_wall,
                    self.time_delta,
                    self.time_epoch,
                    self.time_ping))


def processMessage(data):
    global LOGBUFFER

    if data['type'] == 1:
        data_container = MessageDebug(data)
    elif data['type'] == 2:
        data_container = MessageUpdate(data)

    data_container.writeOutput(True)

# ------------------------------------------------------------------------
# debugFile
# debug in file
# ------------------------------------------------------------------------


def debugFile(msg):

    try:
        # fileName = host.sgl_getModDirectory() + C.spawnerLogPath
        logFile = open(LOGFILENAME, 'a', 512)
        logFile.write(str(msg) + '\n')
        logFile.close()
    except:
        print('{}: failed to write logmessage'.format(getTimeNow()))
        debugFile(msg)


def socketCreate():
    global SOCK

    # Datagram (udp) socket
    try:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Socket created')
    except (socket.error, msg):
        print('Failed to create socket. Error Code : ' +
              str(msg[0]) + ' Message ' + msg[1])
        sys.exit()


def socketBind():
    global SOCK

    # Bind socket to local host and port
    try:
        SOCK.bind((C.SERVERHOST, C.SERVERPORT))
    except (socket.error, msg):
        print('Bind failed. Error Code : ' +
              str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    print('Socket bind on {}:{} complete'.format(C.SERVERHOST, C.SERVERPORT))


def socketReceive():
    global CURRENTCLIENT

    while True:
        # receive data from client (data, addr)
        d = SOCK.recvfrom(1024)
        # data = d[0] # data
        data = pickle.loads(d[0])
        addr = d[1]  # ip and port

        if CURRENTCLIENT != (addr[0]):
            CURRENTCLIENT = (addr[0])
            print('Message from[%s:%s] at %s' % (
                addr[0], addr[1], "{0:.7f}".format(getTimeNow())))

        processMessage(data)


def socketClose():
    global SOCK

    SOCK.close()


def setStartTime():
    global G_TIME_START

    try:
        G_TIME_START = time.time()
        print(
            'setStartTime(): successfully set start time at ' +
            str(G_TIME_START))
    except:
        print('setStartTime(): failed to reset start time')


def setLogFilename():
    global LOGFILENAME

    print('setting filename')
    LOGFILENAME = 'listener_%s_%s_%s.log' % (
        datetime.now().hour, datetime.now().minute, datetime.now().second)
    print('filename set to %s' % (LOGFILENAME))


def getTimeNow():
    timeNow = time.time() - G_TIME_START
    return timeNow


def main():

    setStartTime()
    setLogFilename()

    socketCreate()
    socketBind()
    socketReceive()
    socketClose()


if __name__ == '__main__':
    main()
