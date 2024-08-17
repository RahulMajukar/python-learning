# You can direct your log messages to a file instead of the console by specifying the filename parameter in basicConfig.

# Example:
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logging.info("This message will be logged to the file")