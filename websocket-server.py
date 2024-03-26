#!/usr/bin/env python

import asyncio
import json
import signal

import django
import websockets

django.setup()

from django.contrib.auth.models import User
from redis import asyncio as aioredis
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken
from websockets.frames import CloseCode


def validate_token(token):
    try:
        # Try to decode the token
        decoded_token = AccessToken(token)
        # Check if the token is valid
        decoded_token.verify()
        # If the token is valid, return the user associated with the token
        user_id = decoded_token.payload['user_id']
        user = User.objects.get(id=user_id)
        return user
    except TokenError as e:
        return None


CONNECTIONS = {}


async def handler(websocket):
    """Authenticate user and register connection in CONNECTIONS."""
    token = await websocket.recv()
    user = await asyncio.to_thread(validate_token, token)

    if user is None:
        await websocket.close(CloseCode.INVALID_DATA, "authentication failed")
        await websocket.send('Given Token is not valid')
        return
    CONNECTIONS[user.id] = websocket
    await websocket.send(f"authenticated as user {user.username}")
    try:
        await websocket.wait_closed()
    finally:
        del CONNECTIONS[user.id]


async def process_events():
    """Listen to events in Redis and process them."""

    redis = aioredis.from_url("redis://127.0.0.1:6379/1")
    pubsub = redis.pubsub()
    await pubsub.subscribe("events")
    async for message in pubsub.listen():
        if message["type"] != "message":
            continue
        payload = message["data"].decode()
        event = json.loads(payload)
        user_id = event.get("user_id")
        websocket = CONNECTIONS.get(user_id)
        payload.pop("user_id")
        if websocket:
            await websocket.send(payload)


async def main():
    # Set the stop condition when receiving SIGTERM.
    async with websockets.serve(handler, "0.0.0.0", 8888, reuse_port=True):
        await process_events()  # runs forever


async def shutdown(signal, loop):
    print("Received exit signal. Closing connections...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame),
                                lambda signame=signame: asyncio.create_task(shutdown(signame, loop)))

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
