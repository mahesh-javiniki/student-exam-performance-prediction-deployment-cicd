import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to output to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(filename)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Log to file
        logging.StreamHandler()  # Log to console/terminal
    ]
)


if __name__ == "__main__":
    logging.info("Logging has been set up.")
    logging.info("This is an info message.")
