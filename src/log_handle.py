import logging
import os

def get_logger(name: str, level: int = logging.DEBUG, to_file=True, to_console=False, 
               log_file="pacman.log", enabled=False):
    """
    Returns a preconfigured logger instance.
    
    Parameters:
        name (str): Name of the logger, typically __name__ of the module.
        level (int): Logging level. Defaults to DEBUG.
        to_file (bool): Whether to log to file. Defaults to True.
        to_console (bool): Whether to log to console. Defaults to False.
        log_file (str): Path to log file. Defaults to "pacman.log".
        enabled (bool): Whether logging is enabled at all. Defaults to True.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    
    # Clear any existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()
    
    if not enabled:
        # Set level to CRITICAL+1 to disable all logging
        logger.setLevel(logging.CRITICAL + 1)
        # Add a NullHandler to prevent "No handlers found" warnings
        logger.addHandler(logging.NullHandler())
        return logger
        
    logger.setLevel(level)
    
    # Define a standard format for all logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add file handler if requested
    if to_file:
        # Make sure the directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Add console handler if requested
    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
