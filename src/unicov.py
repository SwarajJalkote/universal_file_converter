import pandas as pd
import csv_to_any as csv_proc

class Unicov():
    ''' This class will be used to create a object and then use to read the file data and get it's type'''
    def __init__(self, input_filename, input_delimiter, output_filename, output_delimiter="|", column_names = []):
        self.input_filename = input_filename
        self.input_delimiter = input_delimiter
        self.column_names = column_names
        self.output_filename = output_filename
        self.output_delimiter = output_delimiter

    def get_response(self):
        ''' This function will get the file type object'''
        response = ""
        if self.input_filename.endswith(".csv"):
            response = csv_proc.CSVTOANY(self.input_filename, self.input_delimiter, self.output_filename, self.output_delimiter, self.column_names)

        elif self.input_filename.endswith(".dat"):
            pass

        return response
        

if __name__ == "__main__":
    # file_data, file_type = read_file()
    file = Unicov("input_file.csv", ",", "output.dat", "|", ["Rank in India","Changes Rank from last Year","Forbes 2000 rank in World","Name","Headquarters"])

    data_obj = file.get_response()
    data = data_obj.read_csv_file()
    print("Data: ", data)


