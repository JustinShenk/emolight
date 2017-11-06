#!/ usr/bin/env python
import os
import http.client
import json
import time
import requests
import configparser

from requests import ConnectionError
from urllib.parse import urlencode

_url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
_maxNumRetries = 10

MY_API = 'INSERT_MY_EMOTION_API'


class Emotion_API(object):
    """Get Emotions results from Microsoft Oxford API."""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config['Microsoft'] = {'api': MY_API}

    @classmethod
    def get_emotions(self, image_path, local=True):

        self.config = get_conf()
        """ Send image to Microsoft/Oxford emotion API."""
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self.config['Microsoft']['api']
        headers['Content-Type'] = 'application/octet-stream'

        # Load raw image file into memory
        pathToFileInDisk = os.path.abspath(image_path)
        print(pathToFileInDisk)
        with open(pathToFileInDisk, 'rb') as f:
            data = f.read()
        json = None
        params = None
        callback = None
        result, callback = self.processRequest(json, data, headers, params)
        print(headers)

        if result is not None:
            print("Emotions found:", result)
        return result, callback

    @classmethod
    def processRequest(self, json, data, headers, params):
        """
        Helper function to process the request to Project Oxford

        Parameters:
        json: Used when processing images from its URL. See API Documentation
        data: Used when processing image read from disk. See API Documentation
        headers: Used to pass the key information and the data type request
        """

        retries = None
        result = None
        callback = None

        while True:

            try:
                response = requests.request(
                    'post', _url, json=json, data=data, headers=headers, params=params)
                print(response)
            except ConnectionError:
                print("Cannot connect - check internet connection")
                callback = 'ConnectionError'
                continue

            if response.status_code == 429:

                print("Message: %s" % (response.json()['error']['message']))

                if retries <= _maxNumRetries:
                    time.sleep(1)
                    retries += 1
                    continue
                else:
                    print('Error: failed after retrying!')
                    break

            elif response.status_code == 200 or response.status_code == 201:

                if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                    result = None
                elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                    if 'application/json' in response.headers['content-type'].lower():
                        result = response.json() if response.content else None
                    elif 'image' in response.headers['content-type'].lower():
                        result = response.content
            else:
                print("Error code: %d" % (response.status_code))
                print("Message: %s" % (response.json()['error']['message']))
            break

        return result, callback


def main():
    Emotion_API()


if __name__ == '__main__':
    main()
