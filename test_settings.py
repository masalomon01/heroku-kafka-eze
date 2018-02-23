# settings.py
import config
import heroku3


app_name = config.APP_NAME
heroku_conn = heroku3.from_key(config.SECRET_KEY)
heroku_app = heroku_conn.apps()[app_name]
config_vars = heroku_app.config().to_dict()

KAFKA_URL = config_vars['KAFKA_URL']
KAFKA_CLIENT_CERT = config_vars['KAFKA_CLIENT_CERT']
KAFKA_CLIENT_CERT_KEY = config_vars['KAFKA_CLIENT_CERT_KEY']
KAFKA_TRUSTED_CERT = config_vars['KAFKA_TRUSTED_CERT']
KAFKA_PREFIX = config_vars['KAFKA_PREFIX']

TOPIC1 = config.TOPIC1
TOPIC2 = config.TOPIC2

TOPIC1_WITH_PREFIX = KAFKA_PREFIX + TOPIC1
TOPIC2_WITH_PREFIX = KAFKA_PREFIX + TOPIC2