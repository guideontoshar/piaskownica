""" This module contains the top level classes for simulator engine """

class Simulator:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.info("Running simulation")
