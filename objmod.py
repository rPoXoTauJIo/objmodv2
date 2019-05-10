# --------------------------------------------------------------------------
# objmod by rpoxo
#
# Description:
#
# module for changing various object templates properties on flight
#
# Credits:
#   alon&mats&pr sources for various code help
# -------------------------------------------------------------------------

# importing python system modules
import sys
import time
import math

# importing modules from standart bf2 package
import bf2
import host

# importing custom modules
import constants as C

G_TWEAKER = None

class Tweaker:

    def __init__(self):
        self.__queries = []

    def setupDefaultTweaks(self):
        del self.__queries
        self.__queries = []

        for vehicle in C.TWEAKS:
            debugMessage('Tweaker::parsing %s' % (vehicle))
            for vehicle_part in C.TWEAKS[vehicle]:
                invoke_string = ('ObjectTemplate.active %s' % (str(vehicle_part)))
                host.rcon_invoke(invoke_string)
                debugMessage(invoke_string)
                for param in C.TWEAKS[vehicle][vehicle_part]:
                    host.rcon_invoke(param)
                    debugMessage(param)
    

# ------------------------------------------------------------------------
# Init
# ------------------------------------------------------------------------


def init():
    global G_TWEAKER

    G_TWEAKER = Tweaker()
    G_TWEAKER.setupDefaultTweaks()

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
        
        if G_TWEAKER is not None:
            G_TWEAKER.setupDefaultTweaks()

        debugMessage('===== FINISHED OBJMOD INIT =====')


# ------------------------------------------------------------------------
# onChatMessage
# Callback that managing chat messages.
##########################################################################
# !NEVER call any messages directly from onChatMessage handler
# It causing inifite loop and game hangs
##########################################################################
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
        del args[0]
        if len(args) == 0:
            debugMessage('NO ARGS IN CHAT MSG')
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

    if args[0] == C.KEYWORD_RELOAD:
        reload(C)  # reloading constant file
        return G_TWEAKER.setupDefaultTweaks()


# Debug
def debugMessage(msg):
    host.rcon_invoke('echo "%s"' % (str(msg)))

def debugIngame(msg):
    #debugMessage(msg)
    try:
        host.rcon_invoke('game.sayAll "%s"' % (str(msg)))
    except:
        host.rcon_invoke('echo "debugIngame(FAIL): %s"' % (str(msg)))
