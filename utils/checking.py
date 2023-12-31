"""Methods for checking answers from our requests"""
import json

from requests import Response
class Checking():

    """Method for checking status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successful! Status code = " + str(response.status_code))
        else:
            print("Failure! Status code = " + str(response.status_code))

    """Method for checking if mandatory fields are present in the query response"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields exists")

    """Method for checking values of mandatory fields in the request response"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " is correct!")

    """Method for checking values against a mandatory field in a query response"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " exists")
        else:
            print("Word " + search_word + " NOT exists")