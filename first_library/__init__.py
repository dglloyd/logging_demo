import logging

logger = logging.getLogger(__name__)

class ThingOne(object):
    def thingy(self):
        logger.info("ThingOne.thingy() checking in")
