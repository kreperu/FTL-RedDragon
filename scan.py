import digitalio
import board

rList = [digitalio.DigitalInOut(board.GP4),digitalio.DigitalInOut(board.GP5),digitalio.DigitalInOut(board.GP7),digitalio.DigitalInOut(board.GP8),digitalio.DigitalInOut(board.GP22),digitalio.DigitalInOut(board.GP21),digitalio.DigitalInOut(board.GP20),digitalio.DigitalInOut(board.GP19)]

cList = [digitalio.DigitalInOut(board.GP0),digitalio.DigitalInOut(board.GP1),digitalio.DigitalInOut(board.GP2),digitalio.DigitalInOut(board.GP3),digitalio.DigitalInOut(board.GP6),digitalio.DigitalInOut(board.GP9),digitalio.DigitalInOut(board.GP10),digitalio.DigitalInOut(board.GP11),digitalio.DigitalInOut(board.GP12),digitalio.DigitalInOut(board.GP13),digitalio.DigitalInOut(board.GP14),digitalio.DigitalInOut(board.GP15),digitalio.DigitalInOut(board.GP16),digitalio.DigitalInOut(board.GP17),digitalio.DigitalInOut(board.GP18),digitalio.DigitalInOut(board.GP26)]

buffer = []

def scan():
    buffer = []
    for i in rList:
        i.direction = digitalio.Direction.INPUT
        i.pull = digitalio.Pull.UP
    for i in cList:
        i.direction = digitalio.Direction.OUTPUT
        i.value = True

    for i in cList:
        i.value = False
        for n in rList:
            if not n.value:
                buffer.append([cList.index(i), rList.index(n)])
        i.value = True

    for i in cList:
        i.direction = digitalio.Direction.INPUT
        i.pull = digitalio.Pull.UP
    for i in rList:
        i.direction = digitalio.Direction.OUTPUT
        i.value = True

    for i in rList:
        i.value = False
        for n in cList:
            if not n.value:
                buffer.append([cList.index(n), rList.index(i)])
        i.value = True

    for q in buffer:
        if buffer.count(q) > 1:
            buffer.remove(q)

    return buffer

