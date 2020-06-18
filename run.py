#!/usr/bin/python3
#import autoremovetorrents
import os
import time
from autoremovetorrents.main import pre_processor
from autoremovetorrents.logger import Logger


Logger.log_path = ''
lg = Logger.register(__name__)

lg.info("Initial startup")

config_yml = os.environ.get('CONFIG_YML','config.yml')
delay = os.environ.get("SCAN_INTERVAL",5)

lg.info("Config: " + config_yml)
lg.info("Scan interval: " + str(delay))

#loop forever
while True:
    pre_processor(["--conf",config_yml,"--view"])
    time.sleep(delay)

