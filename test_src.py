from src import unicov
from src import csv_to_any
import pytest
import pandas as pd

class TestUnicovCSV:
    
    file = unicov.Unicov(
        "input_file.csv", 
        ",", 
        "output.dat", 
        "|", 
        ["Rank in India","Changes Rank from last Year","Forbes 2000 rank in World","Name","Headquarters"])
    
    def test_unicov(self):
        expected_input_filename = "input_file.csv"
        expected_input_delimiter = ","
        expected_column_names = ["Rank in India","Changes Rank from last Year","Forbes 2000 rank in World","Name","Headquarters"]
        expected_output_filename = "output.dat"
        expected_output_delimiter = "|"

        assert all([
            expected_input_filename == self.file.input_filename,
            expected_input_delimiter == self.file.input_delimiter,
            expected_column_names == self.file.column_names,
            expected_output_filename == self.file.output_filename,
            expected_output_delimiter == self.file.output_delimiter
        ])



    def test_get_response_for_csv(self):
        expected_input_filename = "input_file.csv"
        expected_input_delimiter = ","
        expected_column_names = ["Rank in India","Changes Rank from last Year","Forbes 2000 rank in World","Name","Headquarters"]
        expected_output_filename = "output.dat"
        expected_output_delimiter = "|"

        response = self.file.get_response()
        
        assert all([
            expected_input_filename == response.input_filename,
            expected_input_delimiter == response.input_delimiter,
            expected_column_names == response.column_names,
            expected_output_filename == response.output_filename,
            expected_output_delimiter == response.output_delimiter
        ])
        

    def test_read_csv_filewith_col_list(self):
        expected_csv_file = ""
        response = self.file.get_response()

        assert "<class 'pandas.core.frame.DataFrame'>" == str(type(response.read_csv_file()))
