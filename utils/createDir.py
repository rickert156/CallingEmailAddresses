import os

SENT_DIR = 'Sent'
BUFFER = 'Buffer'

def createDir():
    if not os.path.exists(SENT_DIR):os.makedirs(SENT_DIR)
    if not os.path.exists(BUFFER):os.makedirs(BUFFER)


