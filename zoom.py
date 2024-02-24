import base64
import datetime
import json

import requests

Account_id = "hy5Qo6Z-T8-HWmI2vHf4og"
client_id = "qjhZVzGQpq3dMgNyPLdZw"
client_secret = "y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H"


# 1. Get the access token
def get_access_token(client_id, client_secret):
    url = "https://zoom.us/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f'Basic {base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")}',
    }

    data = {
        "grant_type": "account_credentials",
        "account_id": Account_id,
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()


print(get_access_token(client_id, client_secret))
# # 2. Create a meeting
# def create_meeting(access_token, topic, start_time, duration, timezone):
#     url = 'https://api.zoom.us/v2/users/me/meetings'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     data = {
#         'topic': topic,
#         'type': 2, # Scheduled meeting
#         'start_time': start_time,
#         'duration': duration,
#         'timezone': timezone
#     }
#     response = requests.post(url, headers=headers, data=data)
#     return response.json()

# # 3. List all the meetings
# def list_meetings(access_token):
#     url = 'https://api.zoom.us/v2/users/me/meetings'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.get(url, headers=headers)
#     return response.json()

# # 4. Delete a meeting
# def delete_meeting(access_token, meeting_id):
#     url = f'https://api.zoom.us/v2/meetings/{meeting_id}'
#     headers = {
#         'Authorization': f'Bearer {access_token}'
#     }
#     response = requests.delete(url, headers=headers)
#     return response.json()

# # 5. Main
# def main():
#     client_id = 'qjhZVzGQpq3dMgNyPLdZw'
#     client_secret = 'y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H'
#     access_token = get_access_token(client_id, client_secret)
#     print(access_token)

#     start_time = datetime.datetime.now()
#     duration = 30
#     timezone = 'Asia/Kolkata'
#     topic = 'Test meeting'
#     meeting = create_meeting(access_token, topic, start_time, duration, timezone)
#     print(meeting)
# acc_id = 'hy5Qo6Z-T8-HWmI2vHf4og'
# client_id = 'qjhZVzGQpq3dMgNyPLdZw'
# client_secet = 'y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H'

# x = base64.encode(f'{client_id}:{client_secet}', 'utf-8')
# print(x)
