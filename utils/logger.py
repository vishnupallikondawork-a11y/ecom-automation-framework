import logging
import os
from datetime import datetime

_logger = None #global logger reference

def get_logger():
    global _logger

    if _logger:
        return _logger

    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        #create logs folder
        if not os.path.exists("logs"):
            os.makedirs("logs")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file  = f"logs/test_{timestamp}.log"
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    _logger = logger

    return logger
