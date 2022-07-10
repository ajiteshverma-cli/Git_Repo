#
import requests

def parse_a_url(url):
    """
    :param url: url which needs to be parsed and then check for response
    :return:
    """
    response = requests.get(url)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)


if __name__ == '__main__':
    # main function starts
    url = "http://omdbapi.com/"
    try:
        parse_a_url(url)
    except Exception as ex:
        print(ex)
    # main function ends