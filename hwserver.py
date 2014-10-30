#! /bin/env python
# -*- coding: utf-8 -*-


import zmq

def main():
    context = zmq.Context.instance()
    responser = context.socket(zmq.REP)
    responser.bind("tcp://*:5555")
    while True:
        msg = responser.recv()
        print ("receive message: %s" % msg)
        responser.send(b"world")

    responser.close()
    context.term()