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
#### TODO MAKE PROPER PARSER&SERIALISER
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
            D.debug('QueryParser::querySet(): failed to parse settings! original string:\n%s' % (text))

        self.settings[command] = args

    def queryRun(self):
        for command in self.settings.keys():
            args = self.settings[command]
            args = '/'.join(args)
            host.rcon_invoke("""
                ObjectTemplate.active %s
                ObjectTemplate.%s %s
                """ % (self.template, attribute, args))
            #D.debug('InvokeCommand:: host.rcon_invoke()')
            D.debug('ObjectTemplate.active %s\nObjectTemplate.%s %s' % (self.template, command, args))
    
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
        host.registerHandler('ChatMessage', onChatMessage, 1) #registering chatMessage handler
        D.init()
        
        # test stuff
        #timer = bf2.Timer(setTestVehicle, 10, 1, 'ch_jet_su30')

        # test stuff2
        host.registerHandler('EnterVehicle', onEnterVehicle)
        host.registerHandler('ExitVehicle', onExitVehicle)
        
        setupDefaults()
        #resetUpdateTimer()
        D.debug('===== FINISHED OBJMOD INIT =====')

def resetUpdateTimer():
    global G_UPDATE_TIMER
    
    if G_UPDATE_TIMER != None:
        G_UPDATE_TIMER.destroy()
        G_UPDATE_TIMER = None
        G_UPDATE_TIMER = bf2.Timer(onUpdate, 1, 1)
        G_UPDATE_TIMER.setRecurring(0.01)# 30+-5fps = ~0.33...ms is server frame, no need to speed up things a lot
    else:
        G_UPDATE_TIMER = bf2.Timer(onUpdate, 1, 1)
        G_UPDATE_TIMER.setRecurring(0.01)# 30+-5fps = ~0.33...ms is server frame, no need to speed up things a lot

# offloading debug
# tnx pie&mats for idea, althorugh my implementation is worse
def onUpdate(data = ''):
    global G_UPDATE_LAST

    #D.debugUDP('U_TIME: %s' % (D.time_now()))
    delta = host.timer_getWallTime() - G_UPDATE_LAST
    G_UPDATE_LAST = host.timer_getWallTime()
    if G_TRACKED_OBJECT != None:
        position = G_TRACKED_OBJECT.getPosition()
        rotation = G_TRACKED_OBJECT.getRotation()
        D.debug('POSROT: P%sP|R%sR|T(%s)T|D(%s)D' % (position, rotation, host.timer_getWallTime(), delta), ['udp', 'echo'])
        #D.debug('Delta: %s' % (delta), ['echo'])

def onEnterVehicle(player, vehicle, freeSoldier = False):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = vehicle
    D.debug('Player entered %s' % (G_TRACKED_OBJECT.templateName))
    resetUpdateTimer()

def onExitVehicle(player, vehicle):
    global G_TRACKED_OBJECT

    G_TRACKED_OBJECT = None
    D.debug('Player left %s' % (vehicle.templateName))
    resetUpdateTimer()

def setTestVehicle(template, data = ''):
    global G_TRACKED_OBJECT

    objects = bf2.objectManager.getObjectsOfTemplate(template)
    G_TRACKED_OBJECT = objects[0]
    D.debug('Selected object of template %s at %s' % (G_TRACKED_OBJECT.templateName, str(G_TRACKED_OBJECT.getPosition())))

def setupDefaults():
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
                D.debugEcho('NO ARGS IN CHAT MSG')
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
    
    if args[0].isdigit():
        selectQuery(args[0])
        return
    
    if args[0] in C.templateProperties[1].keys() or args[0] in C.templateProperties[3].keys():
        updateQuery(args)
        return
    
    if args[0] == 'run':
        runQuery()
        return
    
    if args[0] == 'round':
        return D.debug('Current round: %s' % (realitycore.currentRound()))
    
    if args[0] == 'reload':
        reload(C)
        return setupDefaults()
    
    if args[0] == 'upload':
        resetUpdateTimer()
        return

    if args[0] == 'sge1':
        templateName = 'ch_officer'
        templateAlias = templateName + '_127' # should be random
        team = 1
        teamOnVehicle = 1
        position = realitycore.getPositionFromPlayer(player, 4)
        rotation = player.getDefaultVehicle().getRotation()
        D.debug('kit position %s' % (str(position)))
        D.debug('kit rotation %s' % (str(rotation)))

        host.rcon_invoke("""
ObjectTemplate.create ObjectSpawner %s
ObjectTemplate.activeSafe ObjectSpawner %s
ObjectTemplate.isNotSaveable 1
ObjectTemplate.hasMobilePhysics 0
ObjectTemplate.setObjectTemplate %s %s
ObjectTemplate.TimeToLive 12000
ObjectTemplate.Distance 100
ObjectTemplate.team %s
ObjectTemplate.teamOnVehicle %s
Object.create %s
Object.absolutePosition %s/%s/%s
Object.rotation %s/%s%s
Object.setControlPointId 101
Object.team %s
Object.delete
""" % (templateAlias,\
        templateAlias,\
        team, templateName,\
        team,\
        teamOnVehicle,\
        templateAlias,\
        position[0], position[1], position[2],\
        rotation[0], rotation[1], rotation[2],\
        team))
        return
        
    createQuery(args)

def selectQuery(index = '0'):
    global G_SELECTED_QUERY

    if index == '0': # because parsing str(chat)
        for query in G_QUERIES.keys():
            D.debug('selectQuery(): %s' % (G_QUERIES[query].template))
            for setting in G_QUERIES[query].settings.keys():
                D.debug('selectQuery(): %s %s' % (setting, G_QUERIES[query].settings[setting]))
        D.debug('selectQuery(): finished displaying %s queries' % (len(G_QUERIES)))
    else:
        G_SELECTED_QUERY = G_QUERIES[int(index)]
        D.debug('selectQuery(): selected query #%s' % (index))
    
def updateQuery(args):
    global G_SELECTED_QUERY

    G_SELECTED_QUERY.updateCommand(args)

def runQuery():
    global G_SELECTED_QUERY

    G_SELECTED_QUERY.run()

def createQuery(args):
    global G_SELECTED_QUERY

    G_SELECTED_QUERY = InvokeCommand(args)

def clearQueries():
    global G_QUERIES
    global G_SELECTED_QUERY
    
    del G_QUERIES
    G_QUERIES = {}
    
    del G_SELECTED_QUERY
    G_SELECTED_QUERY = None

    
# EOF