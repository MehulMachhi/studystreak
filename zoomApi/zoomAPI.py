import base64
import datetime
import json
import pprint
import time

import requests

from .main import json_data

base_url = 'https://zoom.us'
token_url = "https://zoom.us/oauth/token"
Account_id = "hy5Qo6Z-T8-HWmI2vHf4og"
client_id = "qjhZVzGQpq3dMgNyPLdZw"
client_secret = "y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H"
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set the logging level to INFO or desired level

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)


class ZOomClient:
    __client_id = None
    __client_secret = None
    __access_token = None
    expiry = None

    def __init__(self, account_id, client_id, client_secret) -> None:
        self.__class__.__client_id = client_id
        self.__class__.__client_secret = client_secret
        self.check_and_set_token()

    @property
    def access_token(cls):
        return cls.__access_token

    @access_token.setter
    def access_token(cls, token):
        cls.__access_token = token

    def __get_access_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f'Basic {base64.b64encode(f"{self.__class__.__client_id}:{self.__class__.__client_secret}".encode("utf-8")).decode("utf-8")}',
        }

        data = {
            "grant_type": "account_credentials",
            "account_id": Account_id,
        }

        try:
            response = requests.post(f'{base_url}/oauth/token', headers=headers, data=data)
            return response.json()

        except Exception as e:
            raise Exception(f"Error getting access token: {e}")

    def __save_token(self):
        logger.info("Getting the access token.")
        token = self.__get_access_token()
        logger.info("Token received.")
        token_data = {
            "access_token": token["access_token"],
            "expiry": (expiry_time:= time.time() + int(token["expires_in"])),
        }
        with open(".zoom_token", "w") as f:
            json.dump(token_data, f)

        self.__class__.access_token = token["access_token"]
        self.__class__.expiry = expiry_time
        return self
    
    def validate(self):
        try:
            with open(".zoom_token", "r") as f:
                token_data = json.load(f)
                if time.time() >= token_data["expiry"]:
                    logger.info('Token is expired. Setting up a new token.')
                    self.__save_token()
                else:
                    self.__class__.access_token = token_data["access_token"]
        except FileNotFoundError:
            logger.info('File not found. Setting up new token.')
            self.__save_token()
        except Exception as e:
            print(e)
            raise Exception(f"Error checking token expiry: {e}")
        return self
        
    def check_and_set_token(self):
        if self.access_token and time.time() > self.expiry:
            logger.info("Got the access token in cls. running the validation")
            self.validate()
        elif self.access_token is None:
            logger.info('unable to get the token from cls. running validate()')
            self.validate()
        else:
            return self
        
    def create_meeting(self,data:dict):
        url = f'{base_url}/v2/users/me/meetings'
        header = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type':'application/json',
        }
        json_data = json.dumps(data, indent=2)
        
        response = requests.post(url, headers=header, data=json_data)
        logger.info('Response when creating the zoom meeting.', response.text,)
        return response.json()
