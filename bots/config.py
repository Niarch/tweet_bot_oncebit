import tweepy
import logging
import json

logger = logging.getLogger()


def read_json(filename):
    with open(filename) as json_obj:
       creds =  json.load(json_obj)
    return creds


def create_api():
    creds = read_json("creds.json")
    consumer_key = creds.get("CONSUMER_KEY")
    consumer_secret = creds.get("CONSUMER_SECRET")
    access_token = creds.get("ACCESS_TOKEN")
    access_token_secret = creds.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
