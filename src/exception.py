import sys  
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information including the file name and line number where the error occurred.

    Parameters:
        error (Exception): The caught exception.
        error_detail (sys): The sys module to extract traceback details.

    Returns:
        str: Formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extracts traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Gets the file where the error occurred
    line_number = exc_tb.tb_lineno  # Gets the line number where the error occurred

    error_message = f"Error occurred in script [{file_name}] at line [{line_number}] with message: {str(error)}"
    return error_message

class CustomException(Exception):
    """
    Custom exception class to log errors with detailed messages.

    Attributes:
        error_message (str): Detailed error message with traceback.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)  # Logs the error when the exception is raised

    def __str__(self):
        return self.error_message




if __name__ == "__main__":
    logging.info("Logging info message")
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)
