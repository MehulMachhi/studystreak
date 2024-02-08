# live_classes/utils/zoom_integration.py

from django_zoom_meetings import ZoomMeetings

class ZoomIntegration:
    def __init__(self, api_key, secret_key, zoom_email):
        self.api_key = api_key
        self.secret_key = secret_key
        self.zoom_email = zoom_email
        self.zoom = ZoomMeetings(api_key, secret_key, zoom_email)

    def create_meeting(self, date, topic, duration, password):
        # Create a new Zoom meeting
        return self.zoom.CreateMeeting(date, topic, duration, password)

    def get_meeting(self, meeting_id):
        # Get details of a Zoom meeting
        return self.zoom.GetMeeting(meeting_id)

    def delete_meeting(self, meeting_id):
        # Delete a Zoom meeting
        return self.zoom.DeleteMeeting(meeting_id)
