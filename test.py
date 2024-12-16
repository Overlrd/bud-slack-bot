import logging


import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logging.basicConfig(level=logging.DEBUG)
load_dotenv()
slack_token = os.getenv("BOT_USER_OAUTH_TOKEN")
channel_id = os.getenv("CHANNEL_ID")
client = WebClient(token=slack_token)

if not slack_token:
    raise Exception(
        "    BOT_USER_OAUTH_TOKEN environement not found, please make sure to provide one     "
    )
elif not channel_id:
    raise Exception(
        "CHANNEL_ID environement variable not found, please make sure to provide one"
    )

try:
    response = client.chat_postMessage(
        channel="C085AH5KP9R", text="Hello from your app! :tada:"
    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
