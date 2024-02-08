from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from zoom_integration import ZoomMeetings  # Assuming you have a separate module for Zoom integration

app = FastAPI()

# Replace these with your actual Zoom API credentials
api_key = 'AX1dgLG1QQS_NfkqnDtuTA'
secret_key = 'uT3i6Q4dl65CsjHbho9aZMtqTcGRhtmW'
zoom_email = 'your_zoom_email@example.com'  # Replace with your actual Zoom email

class LiveClass(BaseModel):
    date: str
    batch: str

@app.post("/live-classes/")
async def create_live_class(live_class: LiveClass):
    # Create a new LiveClass instance
    # (Assuming this is where you save it to the database)
    # ...

    # Initialize ZoomMeetings with your API credentials
    my_zoom = ZoomMeetings(api_key, secret_key, zoom_email)

    # Example: Create a new Zoom meeting when a LiveClass is created
    create_meeting = my_zoom.create_meeting(
        date=live_class.date,  # Use the date from the LiveClass instance
        topic=f'LiveClass Meeting for {live_class.batch}',  # Use dynamic topic based on the batch
        duration=60,  # Example: Meeting duration of 60 minutes
        password='1234'  # Example: Set a static meeting password
    )

    # Handle the response from the Zoom API (create_meeting)
    # ...

    # You can handle the response or return any data as needed
    return {"message": "LiveClass created successfully", "zoom_meeting_id": create_meeting['id']}

@app.delete("/live-classes/{live_class_id}/")
async def delete_live_class(live_class_id: int):
    # Delete the LiveClass instance with the given ID
    # (Assuming this is where you delete it from the database)
    # ...

    # Initialize ZoomMeetings with your API credentials
    my_zoom = ZoomMeetings(api_key, secret_key, zoom_email)

    # Example: Delete a Zoom meeting when a LiveClass is deleted
    delete_meeting = my_zoom.delete_meeting(
        meeting_id=live_class_id  # Use the LiveClass ID as the Zoom meeting ID
    )

    # Handle the response from the Zoom API (delete_meeting)
    # ...

    # You can handle the response or return any data as needed
    return {"message": "LiveClass deleted successfully"}
