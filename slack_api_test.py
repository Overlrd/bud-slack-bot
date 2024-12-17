"""
This script checks if a connection can be made with the Slack API.

It loads the "BOT_USER_OAUTH_TOKEN" and creates a test client to use the
builtin "api_test" function from the "slack_sdk".

Usage examples:
    # Good case, api_response["ok"] is True
    python3 slack_api_test.py   # Returns "WORKING!"

    # Bad case, api_response["ok"] is False or an error occurs
    python3 slack_api_test.py   # Prints the error message like 'invalid_auth' or 'channel_not_found'
"""

import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load the environment variables
load_dotenv()
slack_bot_token = os.getenv("BOT_USER_OAUTH_TOKEN")


if not slack_bot_token:
    raise Exception(
        "The 'BOT_USER_OAUTH_TOKEN' environment variable is not set. "
        "Please ensure that the bot's OAuth token is defined in your environment variables, "
        "and try again."
    )

client = WebClient(slack_bot_token)

# Verify it works
try:
    api_response = client.api_test()
    assert api_response["ok"]
    print("WORKING!")
except SlackApiError as e:
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"ERROR: {e.response['error']}")
