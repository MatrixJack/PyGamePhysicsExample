EVENT_KNAME = { 1: "ActiveEvent", 2: "KeyDown", 3: "KeyUp", 4: "MouseMovement", 5: "MouseButtonDown", 6: "MouseButtonUp", 12: "Quit" } # Key-Name
EVENT_INAME = { "ActiveEvent": 1, "KeyDown": 2, "KeyUp": 3, "MouseMovement": 4, "MouseButtonDown": 5, "MouseButtonUp": 6, "Quit": 12 } # Int-Name

GAME_CAPTION = "A cool game"
BACKGROUND_COLOR = (100, 100, 150)

SET_SCREEN_FPS = 60

X_AXIS_BOUND = 600
Y_AXIS_BOUND = 400

PLAYER_COLOR = (255, 0, 0)
PLAYER_SIZE = (30, 40)
PLAYER_FRICTION = -.25

GROUND_COLOR = (210,105,30)

PLAYER_STATES = {
    "IDLE": {
        "value" : 0,
        "name" : "idle",
    },

     "ACTIVE": {
        "value" : 1,
        "name" : "active",
    },

     "DEAD": {
        "value" : 2,
        "name" : "dead",
    }
}