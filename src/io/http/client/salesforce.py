import os
import logging
import requests
from dotenv import load_dotenv
from src.service.auth import get_access_token

load_dotenv()

logger = logging.getLogger()

SF_CONNECTOR_TIMEOUT = int(os.getenv("SALESFORCE_CONNECTOR_TIMEOUT", "5"))


def post(endpoint, data):
    try:
        access_token, instance_url = get_access_token()

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        url = f"https://{instance_url}/services/data/v59.0/sobjects{endpoint}"

        response = requests.post(url, json=data, headers=headers, timeout=SF_CONNECTOR_TIMEOUT)

        if response.content:
            logger.info(f'Response from Salesforce {response.status_code} {response.json()}')
        else:
            logger.info(f'Response from Salesforce {response.status_code}')

        return response
    except requests.RequestException as e:
        logger.error(f"Error send event to Salesforce {e}")
        raise e

def get(endpoint):
    try:
        access_token, instance_url = get_access_token()

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        url = f"https://{instance_url}/services/data/v59.0/sobjects{endpoint}"

        response = requests.get(url, headers=headers, timeout=SF_CONNECTOR_TIMEOUT)

        if response.content:
            logger.info(f'Response from Salesforce {response.status_code} {response.json()}')
        else:
            logger.info(f'Response from Salesforce {response.status_code}')

        return response
    except requests.RequestException as e:
        logger.error(f"Error getting data from Salesforce {e}")
        raise e
