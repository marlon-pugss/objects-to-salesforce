import requests
import logging
from typing import Optional

logger = logging.getLogger()


class SalesforceAuthService:
    def __init__(self, client_id: str, client_secret: str, username: str, password: str, security_token: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.security_token = security_token
        self.access_token: Optional[str] = None
        self.instance_url: Optional[str] = None

    def get_access_token(self) -> str:
        """
        Obtém o access token do Salesforce usando OAuth2 Password Flow
        """
        if self.access_token:
            return self.access_token

        url = "https://login.salesforce.com/services/oauth2/token"
        
        data = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': f"{self.password}{self.security_token}"
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data['access_token']
            self.instance_url = token_data['instance_url']
            
            logger.info("Access token obtido com sucesso")
            return self.access_token
            
        except requests.RequestException as e:
            logger.error(f"Erro ao obter access token: {e}")
            raise e

    def get_instance_url(self) -> str:
        """
        Retorna a instance URL do Salesforce
        """
        if not self.instance_url:
            self.get_access_token()
        
        return self.instance_url

    def refresh_token(self) -> str:
        """
        Força a renovação do token
        """
        self.access_token = None
        return self.get_access_token()