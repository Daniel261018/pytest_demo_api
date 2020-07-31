# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 23:10

from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager(logger_name="api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                   log_filename="api.log",
                                                                   log_path=LOG_PATH)
logger.debug("-------debug-------")
logger.info("-------info-------")
logger.warning("-------warning-------")
logger.error("-------error-------")
logger.critical("-------critical-------")
print("hrllo")