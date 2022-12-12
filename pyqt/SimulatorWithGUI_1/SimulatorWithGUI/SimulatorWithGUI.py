""" This is simple application showing a simulator with Qt based GUI """

import simulator
import logging
import sys

if __name__ == '__main__':
    logger = logging.getLogger('Simulator')
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    sim = simulator.Simulator(logger=logger)
    sim.run()
