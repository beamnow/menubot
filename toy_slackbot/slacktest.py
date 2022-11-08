import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from keyfile import slack_token, channel_id
from parsertest import get

from apscheduler.schedulers.blocking import BlockingScheduler
slack_token = slack_token
channel_id = channel_id

def process(slack_token=slack_token, channel_id=channel_id):
    slack_token = slack_token # Bot OAuth Token
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(
            channel=channel_id, # Channel ID
            text="이번 주 식단표 입니다 :+1:",
            blocks=[
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "이번 주 식단표 입니다 :+1:",
                    "emoji": True
                },
                "image_url": get(),
                "alt_text": "babmucja"
            }
            ]
        )
    except SlackApiError as e:
        assert e.response["error"]

# Schedules job_function to be run on the Mon-Friday
# at 11:00
sched = BlockingScheduler()
sched.add_job(process, 'cron', day_of_week='mon-fri', hour=11, minute=00)

sched.start()
