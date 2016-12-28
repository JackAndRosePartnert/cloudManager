#!/usr/bin/python

#Filename     log.py
#Author       
#Email        liuxioayan@webaddress.com

import os
import sys
import time
sys.path.append("..")
import conf
import logging
import logging.handlers

try:
    import curses
    curses.setupterm()
except:
    curses = None

default_logfile = getattr(conf,'SMARTCLOUD_LOGFILE')
#default_logfile = '/var/log/smartcloud/smartcloud.log'
print default_logfile

class Singleton(type):
    """Singleton Metaclass"""
    def __init__(cls,name,bases,dic):
        super(Singleton,cls).__init__(name,bases,dic)
        cls.instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls.instance

class MessageFormatter(logging.Formatter):
    def __init__(self,color,*args,**kwargs):
        logging.Formatter.__init__(self,*args,**kwargs)
        self._color=color
        if color and curses:
            fg_color = unicode(curses.tigetstr("setaf") or\
                                        curses.tigetstr("setf") or "", "ascii")

            self._colors={
                    logging.DEBUG: unicode(curses.tparm(fg_color,2),"ascii"),
                    logging.INFO: unicode(curses.tparm(fg_color,6),"ascii"),
                    logging.WARNING: unicode(curses.tparm(fg_color, 3), "ascii"),
                    logging.ERROR: unicode(curses.tparm(fg_color, 5), "ascii"),
                    logging.FATAL: unicode(curses.tparm(fg_color, 1), "ascii"),
                    }
            self._normal = unicode(curses.tigetstr("sgr0"), "ascii")

    def format(self,record):
        try:
            record.message = record.getMessage()
        except Exception, e:
            record.message = "Bad message (%r): %r" % (e, record.__dict__)
        record.asctime = time.strftime("%Y/%m/%d %H:%M:%S",\
                                                            self.converter(record.created))
        prefix = '[%(levelname)-8s %(asctime)s] ' % record.__dict__
        if self._color and curses:
            prefix = (self._colors.get(record.levelno, self._normal) +\
                                                                        prefix + self._normal)
        formatted = prefix + record.message
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            formatted = formatted.rstrip() + "\n" + record.exc_text
        return formatted.replace("\n", "\n    ")

class MessageLog(object):
    __metaclass__ = Singleton

    def __init__(self, logfile=default_logfile,):
        self._LEVE = {1:logging.INFO, 2:logging.WARNING, 3:logging.ERROR,\
                                                      4:logging.DEBUG, 5:logging.FATAL}
        self.loger = logging.getLogger()
        self._logfile = logfile
        self.init()

    def init(self):
        if not os.path.exists(self._logfile):
            os.mknod(self._logfile)
        handler = logging.handlers.RotatingFileHandler(self._logfile)
        handler.setFormatter(MessageFormatter(color=True))
        self._handler = handler
        self.loger.addHandler(handler)

    def INFO(self,msg,leve=1):
        self.loger.setLevel(self._LEVE[leve])
        self.loger.info(msg)

    def WARNING(self, msg, leve=2):
        self.loger.setLevel(self._LEVE[leve])
        self.loger.warning(msg)

    def ERROR(self, msg, leve=3):
        self.loger.setLevel(self._LEVE[leve])
        self.loger.error(msg)

    def DEBUG(self, msg, leve=4):
        self.loger.setLevel(self._LEVE[leve])
        self.loger.debug(msg)

    def FATAL(self, msg, leve=5):
        self.loger.setLevel(self._LEVE[leve])
        self.loger.fatal(msg)


if __name__ == "__main__":
	LOG = MessageLog()
	str1 = "aaaaaaaa"
	str2 = "bbbbbbbbbb"
	LOG.INFO("#%s###################################"
					        "@@@@%s@@@@@@@@@@@" %(str1,str2))
	LOG.WARNING("####################################")
	LOG.ERROR("####################################")
	LOG.DEBUG("####################################")
	LOG.FATAL("####################################")












