import logging

logger = logging.getLogger(__name__)

class AppThing(object):
    def thingy(self):
        logger.info("AppThing.thingy() checking in")
