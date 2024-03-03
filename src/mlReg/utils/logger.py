import os
import logging
import sys

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging_str = "[ [%(asctime)s] : %(levelname)s : %(module)s : %(message)s ]"

logging.basicConfig(
    format = logging_str,
    level = logging.INFO,

    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlRegLogger")

