import pandas as pd
from . import csv_to_any as csv_proc

class Unicov():
    ''' This class will be used to create a object and then use to read the file data and get it's type'''
    def __init__(self, input_filename, input_delimiter, output_filename, output_delimiter="|", column_names = []):
        self.input_filename = input_filename
        self.input_delimiter = input_delimiter
        self.column_names = column_names
        self.output_filename = output_filename
        self.output_delimiter = output_delimiter

    def read_file(self):
        ''' This function will read the file and get the data as well as file type and any other required parameters'''
        response = ""
        if self.input_filename.endswith(".csv"):
            response = csv_proc.CSVTOANY()
            read_data = response.read_csv_file(self.input_filename, self.input_delimiter, self.column_names)
        
        
        
        
        elif self.input_filename.endswith(".dat"):
            pass

        return response



if __name__ == "__main__":
    # file_data, file_type = read_file()
    pass