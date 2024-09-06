import logging
import os

# Step 1: Define the directory for logs and create it if it doesn't exist
LOG_DIR = "reports\logs"  # Directory name for storing logs
os.makedirs(LOG_DIR, exist_ok=True)  # Create the directory if it does not exist

class Logger:
    @staticmethod
    def setup_logger(name, log_file, level=logging.INFO):
        """
        Set up a logger with a specified name and log file.
        
        Args:
        - name (str): Name of the logger.
        - log_file (str): File path for logging output.
        - level (int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        
        Returns:
        - logger (logging.Logger): Configured logger instance.
        """
        # Step 2: Construct the log file path using os.path.join
        log_file_path = os.path.join(LOG_DIR, log_file)

        # Step 3: Create a handler for writing log messages to the file
        handler = logging.FileHandler(log_file_path)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Step 4: Set up the logger with the specified name and add the handler
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        # Step 5: Optionally, add a console handler for output to the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(console_handler)

        return logger

# Example usage in a module:
# logger = Logger.setup_logger('test_logger', 'test.log')
# logger.info('This is an info message')
