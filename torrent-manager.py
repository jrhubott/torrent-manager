#!/usr/bin/python3
import os
import time
import signal
from autoremovetorrents.main import pre_processor
from autoremovetorrents.logger import Logger

def sigterm_handler(signum,frame):  
    raise OSError("Received exit signal")


signal.signal(signal.SIGTERM,sigterm_handler)

Logger.log_path = ''
lg = Logger.register(__name__)

lg.info("Initial startup")

config_yml = os.environ.get('CONFIG_YML','config.yml')
delay = int(os.environ.get("SCAN_INTERVAL",5))

lg.info("Config: " + config_yml)
lg.info("Scan interval: " + str(delay))

#loop forever
while True:
    pre_processor(["--conf="+config_yml])
    lg.info("Scan again in " + str(delay) + " seconds")
    time.sleep(delay)

