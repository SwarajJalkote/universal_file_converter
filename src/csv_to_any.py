import pandas as pd
import traceback
import json

class CSVTOANY:
    def __init__(self, input_filename, input_delimiter, output_filename, output_delimiter="|", column_names=[]):
        self.input_filename = input_filename
        self.input_delimiter = input_delimiter
        self.output_filename = output_filename
        self.output_delimiter = output_delimiter
        self.column_names = column_names

    def read_csv_file(self) -> pd.DataFrame:
        '''
            This function reads the CSV file and converts it into pandas Dataframe.\n
            Description:
                input_file: csv file which needs to be converted with complete path
                input_del: delimiter used in input file. Default: , (comma)
                column_names: list of names of columns which you want to extract from csv
        '''
        if self.column_names != []:
            csv_data = pd.read_csv(filepath_or_buffer=self.input_filename,
                                sep=self.input_delimiter,
                                usecols=self.column_names,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
        else:
            csv_data = pd.read_csv(filepath_or_buffer=self.input_delimiter,
                                sep=self.input_delimiter,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
        return csv_data
    
    def csv_to_dat(self, csv_data):
        '''
            This function will convert the Dataframe to dat.\n
                Description:
                csv_data: pandas DataFrame returned by read_csv_file()
                output_path: dat file which will be created as output with expected path
                output_del: delimiter used in output file: Default: | (pipe)
        '''
        if self.output_filename.endswith(".dat"):
            try:
                csv_data.to_csv(path_or_buf=self.output_filename, sep=self.output_delimiter, header=True, index=False, mode="w", encoding="UTF-8")
                return f"File created successfully in {self.output_filename}" 
            except Exception as exception:
                print("Exception :", exception)
                traceback.print_exc()
        else:
            raise Exception("Please provide correct path with .dat file")

        return "Failed to provide correct output path"

    def csv_to_json(self, csv_data):
        '''
        This function converts the csv file into JSON and takes column_names parameter to filter out the data.\n
        Description:
            input_file: csv file which needs to be processed and converted to json
            input_del: delimiter used in input file. Default: , (comma)
            column_names: list of names of columns which you want to extract from csv
        '''
        
        json_data = []
        if csv_data.empty == False:
            self.column_names = list(csv_data)
            for indx, col in enumerate(self.column_names):
                if "Unnamed" in col:
                    self.column_names[indx] = f"col{indx}"

            for row in csv_data.itertuples(index=False):
                temp = {}
                for key, row in zip(self.column_names, list(row)):
                    temp[key] = row
                json_data.append(temp)
        else:
            return f"Input_File: {self.input_filename} is empty"
        return json.dumps(json_data, indent=4)
    
    def csv_to_excel(self):
        pass

    def csv_to_xml(self):
        pass

    def csv_to_parquet(self):
        pass

    def csv_to_avro(self):
        pass