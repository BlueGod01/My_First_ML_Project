'''this file is especially used for handling exceptions through out the code. 
This is done for project execution monitoring and resolve issues in execution
Whenever we will use 'try' block  and raise custom exception throughout our code
this code will help to identify Errors. This code will tell in which 
python script this error has raised, in which Line no and what is the cause of the error.'''
import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tab = error_detail.exc_info()#extracting the details about the error i.e file_name, line no etc
    filename = exc_tab.tb_frame.f_code.co_filename #python script where the error has occured
    error_message = "Error has occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tab.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        #this function is for printing error message when we perform print(Error)
        return self.error_message
    


        