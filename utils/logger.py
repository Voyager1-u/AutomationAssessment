# import logging
# import os


# # Create logs folder automatically
# if not os.path.exists("logs"):
#     os.makedirs("logs")


# def get_logger():

#     logger = logging.getLogger("API_Test_Logger")

#     logger.setLevel(logging.INFO)

#     # Prevent duplicate logs
#     if not logger.handlers:

#         file_handler = logging.FileHandler(
#             "logs/api_logs.log"
#         )

#         formatter = logging.Formatter(
#             "%(asctime)s - %(levelname)s - %(message)s"
#         )

#         file_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)

#     return logger

import logging
import os


# Create logs folder automatically
if not os.path.exists("logs"):
    os.makedirs("logs")


def get_logger(log_file_name):

    logger = logging.getLogger(log_file_name)

    logger.setLevel(logging.INFO)

    # Avoid duplicate logs
    if not logger.handlers:

        file_handler = logging.FileHandler(
            f"logs/{log_file_name}.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger