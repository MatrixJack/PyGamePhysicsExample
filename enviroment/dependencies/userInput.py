#> Imports
import threading

from coreScripts.gameConstants import EVENT_INAME
from coreScripts.gameConstants import EVENT_KNAME

class ioConnection():
    def __init__(self, IOSelf, eventValue, eventCallback):
        self.callback = eventCallback
        self.value = eventValue
        self.IOSelf = IOSelf

    #> Properties
    connected = True

    #> Methods
    def getCallback(self):
        return self.callback

    def disconnect(self):
        connected = False
        
        self.IOSelf._listners.remove(self.callback)
        
class newIOClass():
    def __init__(self, classObject, pygameModule):
        self.classObject = classObject
        self.pygameModule = pygameModule

        self._keysDown = []
        self._unicodes = {}

        self._listners = {}
        self._yielders = {}

        self.connect("KeyUp", self.handleKeyUp)
        self.connect("KeyDown", self.handleKeyDown)
    
    def distribute(self, event):
        if not self.classObject.gameStatus: return
        
        if self._listners.get(event.type):
            for callback in self._listners.get(event.type):
                currentThread = threading.Thread(target=callback, args=(event,))

                currentThread.start()

        if self._yielders.get(event.type):
            for callback in self._yielders.get(event.type):
                currentThread = threading.Thread(target=callback, args=(event,))

                currentThread.start()

        self._yielders.clear()
        self.pygameModule.event.pump()

    def isKeyDown(self, keyName : str):
        pyGameKeyName = str.lower(keyName)

        return pyGameKeyName in self._keysDown

    def handleKeyDown(self, keyObject):
        if not self._unicodes.get(keyObject.key): self._unicodes[keyObject.key] = keyObject.unicode

        self._keysDown.append(keyObject.unicode)

    def handleKeyUp(self, keyObject):
        self._keysDown.remove(self._unicodes[keyObject.key])

    def connect(self, eventName, eventCallback):
        eventValue = EVENT_INAME[eventName]
        connection = ioConnection(self, eventValue, eventCallback)

        if self._listners.get(eventValue):
            self._listners[eventValue].append(eventCallback)
        else:
            self._listners[eventValue] = [eventCallback]

        return connection

    def wait(self, eventName):
        eventValue = EVENT_INAME[eventName]

        eventFired = False
        gotValue = None
        
        def onWaitFired(valueRecieved):
            gotValue = valueRecieved
            eventFired = True

        if self._yielders.get(eventValue):
            self._yielders[eventValue].append(onWaitFired)
        else:
            self._yielders[eventValue] = [onWaitFired]

        while True:
            if eventFired: 
                break

        return gotValue