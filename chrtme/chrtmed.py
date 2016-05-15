#!/usr/bin/env python
# coding: utf-8

version = '0.0.1'
author = """
Emanuele 'Lele' Calo'
Email:<lele [at] quasinormale [dot] it>
Github/Twitter: eldios
"""

import sys,time
from daemon import Daemon
class MyDaemon(Daemon):
    def run(self):
        from chrtme import main

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'kill' == sys.argv[1]:
            print("Not yet impletemented - TODO")
            sys.exit(2)
        elif 'signal' == sys.argv[1]:
            print("Not yet impletemented - TODO")
            sys.exit(2)
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'status' == sys.argv[1]:
            print("Not yet impletemented - TODO")
            sys.exit(2)
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: {} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)
