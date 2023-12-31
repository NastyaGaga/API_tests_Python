from utils.http_methods import Http_methods
"""Methods for testing Google API"""

base_url = "https://rahulshettyacademy.com"  #Base Url
key = "?key=qaclick123"  #Parameter for all requests

class Coogle_maps_api():

    """Method for creating a new location"""


    @staticmethod
    def create_new_place():

       json_for_create_new_place = {
           "location": {
               "lat": -38.383494,
               "lng": 33.427362
           }, "accuracy": 50,
           "name": "Frontline house",
           "phone_number": "(+91) 983 893 3937",
           "address": "29, side layout, cohen 09",
           "types": [
               "shoe park",
               "shop"
           ],
           "website": "http://google.com",
           "language": "French-IN"

       }
       
       post_resurce = "/maps/api/place/add/json"  #POST method resource
       post_url = base_url + post_resurce + key
       print(post_url)
       result_post = Http_methods.post(post_url, json_for_create_new_place)
       print(result_post.text)
       return result_post

    """Method for checking a new location"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json" #GET method resource
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for updating location"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"  # PUT method resource
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    """Method for deleting location"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"  # DELETE method resource
        put_url = base_url + delete_resource + key
        print(put_url)
        json_for_delete_new_location = {
            "place_id":place_id
        }
        result_delete = Http_methods.put(put_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
