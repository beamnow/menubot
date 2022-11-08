import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from keyfile import key

slack_token = key.slack_token # Bot OAuth Token
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel=key.channel_id, # Channel ID
        text="say hi to Ryan! :thumbsup:"
    )
except SlackApiError as e:
    assert e.response["error"]