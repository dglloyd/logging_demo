import logging

logger = logging.getLogger(__name__)

class ThingTwo(object):
    def thingy(self):
        logger.info("ThingTwo.thingy() checking in")
