from adafruit_hid.keyboard import *
import usb_hid

kbd = Keyboard(usb_hid.devices)

pkeys = []

keys = {"a":0x04,"b":0x05,"c":0x06,"d":0x07,"e":0x08,"f":0x09,"g":0x0A,"h":0x0B,"i":0x0C,"j":0x0D,"k":0x0E,"l":0x0F,"m":0x10,"n":0x11,"o":0x12,"p":0x13,"q":0x14,"r":0x15,"s":0x16,"t":0x17,"u":0x18,"v":0x19,"w":0x1A,"x":0x1B,"y":0x1C,"z":0x1D,"1":0x1E,"2":0x1F,"3":0x20,"4":0x21,"5":0x22,"6":0x23,"7":0x24,"8":0x25,"9":0x26,"0":0x27,"enter":0x28,"esc":0x29,"backspace":0x2A,"tab":0x2B,"space":0x2C,"-":0x2D,"=":0x2E,"[":0x2F,"]":0x30,"backslash":0x31,"#":0x32,";":0x33,"quote":0x34,"accent":0x35,",":0x36,".":0x37,"/":0x38,"caps":0x39,"f1":0x3A,"f2":0x3B,"f3":0x3C,"f4":0x3D,"f5":0x3E,"f6":0x3F,"f7":0x40,"f8":0x41,"f9":0x42,"f10":0x43,"f11":0x44,"f12":0x45,"ptscr":0x46,"scrl":0x47,"pause":0x48,"insert":0x49,"home":0x4A,"pgup":0x4B,"del":0x4C,"end":0x4D,"pgdn":0x4E,"rarrow":0x4F,"larrow":0x50,"dnarrow":0x51,"uparrow":0x52,"key_num":0x53,"key_/":0x54,"key_*":0x55,"key_-":0x56,"key_+":0x57,"key_enter":0x58,"key_1":0x59,"key_2":0x5A,"key_3":0x5B,"key_4":0x5C,"key_5":0x5D,"key_6":0x5E,"key_7":0x5F,"key_8":0x60,"key_9":0x61,"key_0":0x62,"key_.":0x63,"key_backslash":0x64,"app":0x65,"power":0x66,"key_=":0x67,"f13":0x68,"f14":0x69,"f15":0x6A,"f16":0x6B,"f17":0x6C,"f18":0x6D,"f19":0x6E,"f20":0x6F,"f21":0x70,"f22":0x71,"f23":0x72,"f24":0x73,"lctrl":0xE0,"lshift":0xE1,"lalt":0xE2,"lgui":0xE3,"rctrl":0xE4,"rshift":0xE5,"ralt":0xE6,"rgui":0xE7}

pressed = []

def passkey(presses, keymap, layer):
    ckeys = []
    if len(presses) == 1:
        kbd.press(keys[(keymap["layer"+str(layer)])[str(presses[0])]])
        #ckeys = [keys[keymap["layer"+str(layer)][str(presses[0])]]]
        ckeys = presses
        if presses[0] not in pressed:
            pressed.append(presses[0])
    elif len(presses) == 2:
        kbd.press(keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]])
        #ckeys = [keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]]]
        ckeys = presses
        if presses[0] not in pressed:
            pressed.append(presses[0])
    elif len(presses) == 3:
        kbd.press(keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]])
        #ckeys = [keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]]]
        ckeys = presses
        if presses[0] not in pressed:
            pressed.append(presses[0])
    elif len(presses) == 4:
        kbd.press(keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]],keys[keymap["layer"+str(layer)][str(presses[3])]])
        #ckeys = [keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]],keys[keymap["layer"+str(layer)][str(presses[3])]]]
        ckeys = presses
        if presses[0] not in pressed:
            pressed.append(presses[0])
    elif len(presses) == 5:
        kbd.press(keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]],keys[keymap["layer"+str(layer)][str(presses[3])]],keys[keymap["layer"+str(layer)][str(presses[4])]])
        #ckeys = [keys[keymap["layer"+str(layer)][str(presses[0])]],keys[keymap["layer"+str(layer)][str(presses[1])]],keys[keymap["layer"+str(layer)][str(presses[2])]],keys[keymap["layer"+str(layer)][str(presses[3])]],keys[keymap["layer"+str(layer)][str(presses[4])]]]
        ckeys = presses
        if presses[0] not in pressed:
            pressed.append(presses[0])
    return ckeys
    pkeys = ckeys

c = 0
def release(old, current, keymap, layer):
    print(pressed)
    if not current:
        kbd.release_all()
    if pressed:
        for i in pressed:
            if i not in current:
                kbd.release(keys[(keymap["layer"+str(layer)])[str(i)]])
                pressed.remove(i)
    pkeys = keys
