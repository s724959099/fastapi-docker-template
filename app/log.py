from loguru import logger
import datetime
import logging
import sys
from loguru._defaults import LOGURU_FORMAT
from loguru import _datetime
import pytz

tz = pytz.timezone('Asia/Taipei')


# set time to my timezone
def my_now():
    now = datetime.datetime.now(tz)
    return _datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


_datetime.datetime.now = my_now


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging():
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel('INFO')

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True


# https://cuiqingcai.com/7776.html
# https://blog.csdn.net/mouday/article/details/88560543
"""
log 初始化資料
"""
logger.add(
    f'./logs/{datetime.datetime.now(tz):%Y%m%d}.log',
    rotation='1 day',
    retention='7 days',
    level='INFO',
    filter=lambda record: record["extra"].get("name") is None
)
