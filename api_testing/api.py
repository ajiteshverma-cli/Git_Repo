import requests
from requests.exceptions import HTTPError
import json

def parse_a_url(url):
    """
    :param url: url which needs to be parsed and then check for response
    :return:
    """
    # data = {"username": "bond",
    #         "address": "somewhere",
    #         "id": "007"
    # }

    # response = requests.post(url, json=data)

    response = requests.get(url)

    ok_to_use = check_status_code(response)
    if ok_to_use:
        # access JSOn content
        jsonResponse = response.json()
        print("Entire JSON response")
        print(json.dumps(jsonResponse, sort_keys=True, indent=4))


def check_status_code(resposnse):
    """
    check the url response and see if the api has send a usable resposne or not
    """

    status_code = resposnse.status_code
    print(f'status code is: {status_code}')
    if status_code == 200:
        return True
    else:
        return  False

if __name__ == '__main__':
    # main function starts
    url = "https://owen-wilson-wow-api.herokuapp.com/wows/movies"
    try:
        parse_a_url(url)
    except HTTPError as httperr:
        print(f'http error occured: {httperr}')
    except Exception as ex:
        print(f'other error occured: {ex}')
    # main function ends