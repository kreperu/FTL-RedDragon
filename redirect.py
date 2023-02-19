import json

def getmap():
    keymap = {}
    with open("keymap.json", 'r') as f:
        keymap = json.load(f)
    return keymap
