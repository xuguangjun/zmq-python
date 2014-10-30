#! /bin/env python
# -*- coding: utf-8 -*-


import zmq
import time


def main():
    context = zmq.Context.instance()
    sender = context.socket(zmq.REQ)
    sender.connect("tcp://23.245.26.23:5555")
    while True:
        sender.send(b"hello")
        response = sender.recv()
        print ("get response: %s" % response)
        time.sleep(1)

    sender.close()
    context.term()

if __name__ == "__main__":
    main()