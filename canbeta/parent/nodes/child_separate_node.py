
import time

from pisat.core.nav import Node
from pisat.handler import PigpioDigitalOutputHandler

import can09.parent.setting as setting


class ChildSeparateNode(Node):
    
    model = None
    
    THRESHOLS_HEATING_TIME = 10.    # [sec]
    
    def enter(self):
        self.fethandler: PigpioDigitalOutputHandler \
            = self.manager.get_component(setting.NAME_MOSFET_CHILD)
        
        # start
        self.time_begin = time.time()
        self.fethandler.set_high()

    def judge(self, data: None) -> bool:
        if time.time() - self.time_begin > self.THRESHOLD_HEATING_TIME:
            return True
        else:
            return False

    def exit(self):
        self.slogger.info("Parent stops heating and separates the child.")
        self.fethander.set_low()
    