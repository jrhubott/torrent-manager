#!/usr/bin/python3
import os
import time
import signal
from autoremovetorrents.main import pre_processor
from autoremovetorrents.logger import Logger
from autoremovetorrents.version import __version__ as __autoremovetorrents_version__


__version__ = '1.0.0'

#Handle shutdown gracefully when loaded in docker
def sigterm_handler(signum,frame):  
    raise OSError("Received exit signal")


signal.signal(signal.SIGTERM,sigterm_handler)

Logger.log_path = ''
lg = Logger.register(__name__)

lg.info("Initial startup")

# Show versions
lg.info('Torrent Manager Version: %s' % __version__)
lg.info('Auto Remove Torrents Version: %s' % __autoremovetorrents_version__)

config_yml = os.environ.get('CONFIG_YML','conf/config.yml')
delay = int(os.environ.get("SCAN_INTERVAL",5))

lg.info("Config: " + config_yml)
lg.info("Scan interval: " + str(delay))

#loop forever
while True:
    pre_processor(["--conf="+config_yml])
    lg.info("Scan again in " + str(delay) + " seconds")
    time.sleep(delay)

