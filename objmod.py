# --------------------------------------------------------------------------
# Project Reality x by rpoxo
# x
#
# ~ objmodv2.py
#
# Description:
#
# x
#
# Credits:
#   x
# -------------------------------------------------------------------------


# importing python system modules
import sys
import time

# importing modules from standart bf2 package
import bf2
import host

# importing project reality packages
import game.realitycore as realitycore
import game.realitydebug as realitydebug
import game.realityspawner as realityspawner

# importing custom modules
import advdebug as D
import constants as C

G_QUERY_MANAGER = None
G_SELECTED_QUERY = None
G_TRACKED_OBJECT = None
G_UPDATE_TIMER = None
G_UPDATE_LAST = 0.0


####
# TODO MAKE PROPER PARSER&SERIALISER
####


class Query:
    """
        representing single query object for template
    """

    def __init__(self, text):
        self.template = None
        self.settings = {}
        self.setQuery(text)

    def querySet(self, text):
        query_parts = text.split(' ')

        try:
            template = query_parts[0]
            command_key = query_parts[1]
            args = query_parts[2:]

            # selecting command by measuring args lenght
            cmd_type = {
                1: 1,
                3: 3
            }[len(args)]
            command = C.TEMPLATE_PROPERTIES[cmd_type][command_key]
        except:
            D.debugMessage(
                'QueryParser::querySet(): failed to parse settings! original string:\n%s' % (text))

        self.settings[command] = args

    def queryRun(self):
        for command in self.settings.keys():
            args = self.settings[command]
            args = '/'.join(args)
            host.rcon_invoke("""
                ObjectTemplate.active %s
                ObjectTemplate.%s %s
                """ % (self.template, attribute, args))
            D.debugMessage('ObjectTemplate.active %s\nObjectTemplate.%s %s' % (
                self.template, command, args))

    def queryUpdate(self, queryObject):
        for setting in queryObject.settings:
            self.settings[setting] = queryObject.settings[setting]


class QueryManager:

    def __init__(self):
        global G_QUERY_MANAGER

        self.queries = {}
        G_QUERY_MANAGER = self

    def addQuery(self, queryObject):
        queryTemplate = queryObject.template
        if queryTemplate not in self.queries:
            self.queries[queryTemplate] = queryObject
        else:
            self.queries[queryTemplate].queryUpdate(queryObject)

    def setupDefaultQueries():
        clearQueries()

        for objectKey in C.defaultQueries.keys():
            for query in C.defaultQueries[objectKey]:
                text = '!obj %s' % (query[0])
                args = text.split(' ')
                del args[0]
                commandHandler(None, args)

                text = '!obj %s %s' % (query[1], query[2])
                args = text.split(' ')
                del args[0]
                commandHandler(None, args)

                commandHandler(None, ['run'])

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------


def init():
    host.registerGameStatusHandler(onGameStatusChanged)

# ------------------------------------------------------------------------
# DeInit
# ------------------------------------------------------------------------


def deinit():
    host.unregisterGameStatusHandler(onGameStatusChanged)


# ------------------------------------------------------------------------
# onGameStatusChanged
# ------------------------------------------------------------------------
def onGameStatusChanged(status):

    if status == bf2.GameStatus.Playing:
        # registering chatMessage handler
        host.registerHandler('ChatMessage', onChatMessage, 1)
        D.init()

        # test stuff
        #timer = bf2.Timer(setTestVehicle, 10, 1, 'ch_jet_su30')

        # test stuff2
        host.registerHandler('EnterVehicle', onEnterVehicle)
        host.registerHandler('ExitVehicle', onExitVehicle)

        # creating query manager
        QueryManager()
        G_QUERY_MANAGER.setupDefaultQueries()

        setupDefaults()
        # resetUpdateTimer()
        D.debugMessage('===== FINISHED OBJMOD INIT =====')


def resetUpdateTimer():
    global G_UPDATE_TIMER

    if G_UPDATE_TIMER != None:
        G_UPDATE_TIMER.destroy()
        G_UPDATE_TIMER = None
        G_UPDATE_TIMER = bf2.Timer(onUpdate, 1, 1)
        # 30+-5fps = ~0.33...ms is server frame, no need to speed up things a
        # lot
        G_UPDATE_TIMER.setRecurring(0.01)
    else:
        G_UPDATE_TIMER = bf2.Timer(onUpdate, 1, 1)
        # 30+-5fps = ~0.33...ms is server frame, no need to speed up things a
        # lot
        G_UPDATE_TIMER.setRecurring(0.01)

# offloading debug
# tnx pie&mats for idea, althorugh my implementation is worse
def onUpdate(data=''):
    global G_UPDATE_LAST

    wall_time_now = host.timer_getWallTime()
    delta_time = wall_time - G_UPDATE_LAST
    G_UPDATE_LAST = host.timer_getWallTime()
    if G_TRACKED_OBJECT != None:
        position = G_TRACKED_OBJECT.getPosition()
        rotation = G_TRACKED_OBJECT.getRotation()
        message = {
            'position': position,
            'rotation': rotation,
            'time_wall': wall_time_now,
            'time_delta': delta_time
        }
        D.updateMessage(message, ['udp', 'echo'])


def onEnterVehicle(player, vehicle, freeSoldier=False):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = vehicle
    D.debugMessage('Player entered %s' % (G_TRACKED_OBJECT.templateName))
    resetUpdateTimer()


def onExitVehicle(player, vehicle):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = None
    D.debugMessage('Player left %s' % (vehicle.templateName))
    resetUpdateTimer()


def setTestVehicle(template, data=''):
    global G_TRACKED_OBJECT

    objects = bf2.objectManager.getObjectsOfTemplate(template)
    G_TRACKED_OBJECT = objects[0]
    D.debugMessage('Selected object of template %s at %s' % (
        G_TRACKED_OBJECT.templateName, str(G_TRACKED_OBJECT.getPosition())))


# ------------------------------------------------------------------------
# onChatMessage
# Callback that managing chat messages.
# !NEVER call any messages directly from onChatMessage handler as it causing inifite loop
# ------------------------------------------------------------------------
def onChatMessage(playerId, text, channel, flags):

    # fix for local non-dedicated servers
    if playerId == -1:
        playerId = 255

    # getting player object by player index
    player = bf2.playerManager.getPlayerByIndex(playerId)

    # standart check for invalid players
    if player is None or player.isValid() is False:
        return

    # common way to filter chat message
    # clearing text as any channel except Global are prefixed
    text = text.replace('HUD_TEXT_CHAT_COMMANDER', '')
    text = text.replace('HUD_TEXT_CHAT_TEAM', '')
    text = text.replace('HUD_TEXT_CHAT_SQUAD', '')
    text = text.replace('HUD_CHAT_DEADPREFIX', '')
    text = text.replace('* ', '')
    text = text.strip()

    # splitting filtered message text to arguments
    args = text.split(' ')

    if args[0] == C.COMMANDKEY:
        # COMMANDKEY is allowed to use if debug enabled
        if realitydebug.PRDEBUG != None:
            del args[0]
            if len(args) == 0:
                D.debugMessage('NO ARGS IN CHAT MSG', ['echo'])
                return
            commandHandler(player, args)
        else:
            pass


# ------------------------------------------------------------------------
# commandHandler
# wrapper around function calls
# ------------------------------------------------------------------------
def commandHandler(player, args):
    """
        commandHandler
            handling functions calls for ingame debug
    """

    if args[0] == 'reload':
        reload(C)  # reloading constant file
        return G_QUERY_MANAGER.setupDefaultQueries()

    if args[0] == 'upload':
        return resetUpdateTimer()

    #createQuery(args)
    D.debugMessage('commandHandler::args = %s' % (str(args)))


# EOF
