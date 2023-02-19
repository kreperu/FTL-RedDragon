import time
import scan
import comm
import redirect
import os

keymap = redirect.getmap()

print("Hello World!")
b = []

debug = os.getenv("debug")

while True:
    pt = time.monotonic()
    b = scan.scan()
    c = comm.passkey(b, keymap, 0)
    comm.release(c, b)
    ct = time.monotonic()
    if debug >= 1:
        print(ct - pt)
    time.sleep(0.0167)
