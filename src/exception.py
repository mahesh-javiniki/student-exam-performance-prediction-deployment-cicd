import sys

def error_message_detail(error, error_detail: sys):
    exception_class, exception_object, exception_traceback = error_detail.exc_info()
    file_name = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    from logger import logging
    logging.basicConfig(level=logging.INFO)
    try:
        a = 1 / 0
    except Exception as e:
        ce = CustomException(e, sys)
        logging.info(ce)
        raise ce