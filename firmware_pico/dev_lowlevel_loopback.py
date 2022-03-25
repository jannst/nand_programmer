#!/usr/bin/env python3

import usb_handler;
import logging
import threading
import time

# sudo pip3 install pyusb

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")


logging.info("init USB connection");
usb_handler.init_usb();


x = threading.Thread(target=usb_handler.continous_read)
x.start()

while True:
    time.sleep(1)
    num_packets_sec = usb_handler.packet_counter;
    usb_handler.packet_counter = 0;
    logging.info('bytes per sec: %s' % (num_packets_sec * 512 * 8));


#print("Device Says: {}".format()
