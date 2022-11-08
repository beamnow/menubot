import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = token # Bot OAuth Token
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel= Channeld ID, # Channel ID
        text="say hi to Ryan! :thumbsup:"
    )
except SlackApiError as e:
    assert e.response["error"]
