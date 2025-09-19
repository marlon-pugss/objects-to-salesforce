import os
from simple_salesforce import Salesforce
from src.exception import SalesforceException
from dotenv import load_dotenv

load_dotenv()

SALESFORCE_CLIENT_ID = os.getenv('SALESFORCE_CLIENT_ID')
SALESFORCE_CLIENT_SECRET = os.getenv('SALESFORCE_CLIENT_SECRET')
SALESFORCE_USERNAME = os.getenv('SALESFORCE_USERNAME')
SALESFORCE_PASSWORD = os.getenv('SALESFORCE_PASSWORD')
SALESFORCE_SECURITY_TOKEN = os.getenv('SALESFORCE_SECURITY_TOKEN')
SALESFORCE_INSTANCE_URL = os.getenv('SALESFORCE_INSTANCE_URL')

_access_token = None
_instance_url = None

def get_access_token():
    global _access_token, _instance_url

    if _access_token:
        return _access_token, _instance_url


    print(SALESFORCE_CLIENT_ID, SALESFORCE_USERNAME, SALESFORCE_INSTANCE_URL)

    try:
        sf = Salesforce(
            username=SALESFORCE_USERNAME,
            password=SALESFORCE_PASSWORD,
            security_token=SALESFORCE_SECURITY_TOKEN,
            instance_url=SALESFORCE_INSTANCE_URL
        )

        _access_token = sf.session_id
        _instance_url = sf.sf_instance

        return _access_token, _instance_url

    except Exception as e:
        raise SalesforceException(f"Erro de autenticação: {e}")