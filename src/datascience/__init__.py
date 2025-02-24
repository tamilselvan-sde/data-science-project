import os
import logging
import sys
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_dir = "logs"
logging_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(logging_filepath),
        logging.StreamHandler(sys.stdout)  # Fixed: Added sys. prefix to stdout
    ]
)

logger = logging.getLogger("datasciencelogger")
