from PIL import Image
import time
from threading import Thread


answer = None
def check():
    print("Start")
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow")


check()
