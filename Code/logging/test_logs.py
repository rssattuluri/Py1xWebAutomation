# Logging means - capture details, which are useful while debugging
# and show the user details about execution of program

# warning to the users
# information to the users
# errors, critical errors to the user

import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)  # returns a logger with the specific name
    # __name__ = uses root name (file name that we have)

    # intentional logging to use
    LOGGER.info("This is the information Logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is error logs")
    LOGGER.critical("This is critical logs")


