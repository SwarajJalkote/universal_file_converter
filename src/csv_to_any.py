import pandas as pd

class CSVTOANY:
    def read_csv_file(self, input_filename, input_delimiter, column_names=[]) -> pd.DataFrame:
        '''
            This function reads the CSV file and converts it into pandas Dataframe.\n
            Description:
                input_file: csv file which needs to be converted with complete path
                input_del: delimiter used in input file. Default: , (comma)
                column_names: list of names of columns which you want to extract from csv
        '''
        if column_names != []:
            csv_data = pd.read_csv(filepath_or_buffer=input_filename,
                                sep=input_delimiter,
                                usecols=column_names,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
        else:
            csv_data = pd.read_csv(filepath_or_buffer=input_delimiter,
                                sep=input_delimiter,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
        return csv_data
    
    def csv_to_dat(self):
        pass

    def csv_to_json(self):
        pass
    
    def csv_to_excel(self):
        pass

    def csv_to_xml(self):
        pass

    def csv_to_parquet(self):
        pass

    def csv_to_avro(self):
        pass