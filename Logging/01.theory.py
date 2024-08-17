# Logging in Python is a powerful way to track events that happen when software runs. The logging module in Python is built-in and provides a flexible framework for emitting log messages from Python programs. It allows you to monitor, debug, and record the execution of your code by capturing and storing important information.

# 1. Why Use Logging?
# Debugging: Helps identify issues in the code by logging error messages.
# Monitoring: Track the execution flow and performance of your application.
# Auditing: Keep a record of significant events, such as transactions or security breaches.
# Centralized Error Handling: Manage errors and exceptions consistently across your application.


# 2. Basic Logging Setup
# The simplest way to use logging is by using the basicConfig method, which configures the root logger.

# Example:
import logging

logging.basicConfig(level=logging.DEBUG) 
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# 3. Logging Levels
# Logging levels define the severity of the events you are logging. Python has the following logging levels:

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.