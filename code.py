import time
import scan
import comm
import redirect

keymap = redirect.getmap()

print("Hello World!")
b = []

while True:
    b = scan.scan()
    #c = comm.passkey(b, keymap, 0)
    print(b)
    #print(c)
    #comm.release(c, b)
    time.sleep(0.0167)
