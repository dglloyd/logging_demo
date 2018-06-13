import logging
import logging.config


from main_app.thing import AppThing
from first_library import ThingOne
from second_library.nested_thing import ThingTwo

logger = logging.getLogger(__name__)

class MainApp(object):
    def __init__(self):
        logging.config.fileConfig('config.ini')

    def run(self):
        logger.info("main_app checking in")
        app_thing = AppThing()
        app_thing.thingy()
        thing_one = ThingOne()
        thing_one.thingy()
        thing_two = ThingTwo()
        thing_two.thingy()
