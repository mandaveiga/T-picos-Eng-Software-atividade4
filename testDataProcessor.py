import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry, avgAge, transformToMonths
import json

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Elizabeth Norris')
        self.assertEqual(data[1]['age'], 58)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avgAgeCountry_success(self):
        with open('users.json', 'r') as file:
            data = json.load(file)

        avg = avgAgeCountry(data, "BR")
        self.assertEqual(avg, 38.54)

    def test_avgAgeCountry_fail_country_without_entries(self):
        with open('users.json', 'r') as file:
            data = json.load(file)

        avg = avgAgeCountry(data, "test_country")
        self.assertEqual(avg, None)
    
    def test_avgAgeCountry_fail_no_data(self):
        avg = avgAgeCountry(None, "test_country")
        self.assertEqual(avg, None)
    
    def test_avgAgeCountry_fail_empty_users_list(self):
        avg = avgAgeCountry([], "BR")
        self.assertEqual(avg, None)
    
    def test_avgAgeCountry_fail_wrong_data_age(self):
        with open('missing_age.json', 'r') as file:
            data = json.load(file)
        avg = avgAgeCountry(data, "UK")
        self.assertEqual(avg, 47)

    def test_avgAgeCountry_fail_wrong_data_country(self):
        with open('missing_country.json', 'r') as file:
            data = json.load(file)
        avg = avgAgeCountry(data, "UK")
        self.assertEqual(avg, 45)

    def test_avgAge_success(self):
        with open('users.json', 'r') as file:
            data = json.load(file)

        avg = avgAge(data)
        self.assertEqual(avg, 39.15)
    
    def test_avgAge_fail_no_data(self):
        avg = avgAge(None)
        self.assertEqual(avg, None)

    def test_avgAge_fail_empty_users_list(self):
        avg = avgAge([])
        self.assertEqual(avg, None)
    
    def test_avgAge_fail_wrong_data_age(self):
        with open('missing_age.json', 'r') as file:
            data = json.load(file)
        avg = avgAge(data)
        self.assertEqual(avg, 47)
    
    def test_transformToMonths_success(self):
        months = transformToMonths(1)
        self.assertEqual(months, 12)

    def test_transformToMonths_fail_wrong_type(self):
        months = transformToMonths("some string")
        self.assertEqual(months, None)
    
    def test_transformToMonths_fail_wrong_value(self):
        months = transformToMonths(-1)
        self.assertEqual(months, None)

if __name__ == '__main__':
    unittest.main()