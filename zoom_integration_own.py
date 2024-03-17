import json

import requests
from zoomus import ZoomClient

base_url = 'https://zoom.us'
token_url = "https://zoom.us/oauth/token"
Account_id = "4h9jZgnETeC1jeCttAqewA"
client_id = "uWxvDYmLRBGf6uW2HUWgA"
client_secret = "B8Xg5H6UJbjppdTptwa2IOjn6mQaFsBs"
client = ZoomClient(client_id, client_secret, Account_id)
print("trrrrr")


def list_users():
    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    print(user_list_response, user_list)

# list_users()

def create_meeting(user_id):
    meeting_list = client.meeting.create(user_id="jP0UzREKQdaFADMVsxTRlA", json={
            'topic': 'My Zoom Meeting 2',
            'type': 2  # 1 for instant meeting, 2 for scheduled meeting
        })
    print("meeting_list",meeting_list)
    print("meeting_list",meeting_list.json())


# create_meeting("jP0UzREKQdaFADMVsxTRlA")

def list_meetings(user_id):
    list_meeting = client.meeting.list(user_id=user_id)
    print(list_meeting)
    print(list_meeting.json())


list_meetings("jP0UzREKQdaFADMVsxTRlA")