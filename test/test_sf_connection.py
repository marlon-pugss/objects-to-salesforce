import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def test_salesforce_connection():
    # Pega as credenciais do .env
    client_id = os.getenv('SALESFORCE_CLIENT_ID')
    client_secret = os.getenv('SALESFORCE_CLIENT_SECRET')
    username = os.getenv('SALESFORCE_USERNAME')
    password = os.getenv('SALESFORCE_PASSWORD')
    instance_url = os.getenv('SALESFORCE_INSTANCE_URL')
    
    print("🔍 Testando conexão com Salesforce...")
    print(f"Username: {username}")
    print(f"Instance: {instance_url}")
    
    # URL para obter token
    auth_url = f"{instance_url}/services/oauth2/token"
    
    # Dados para autenticação
    auth_data = {
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password
    }
    
    try:
        # Faz a requisição de autenticação
        response = requests.post(auth_url, data=auth_data)
        
        if response.status_code == 200:
            token_data = response.json()
            print("✅ Conexão bem-sucedida!")
            print(f"Access Token: {token_data['access_token'][:20]}...")
            print(f"Instance URL: {token_data['instance_url']}")
            return True
        else:
            print("❌ Falha na autenticação!")
            print(f"Status: {response.status_code}")
            print(f"Erro: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False

if __name__ == "__main__":
    test_salesforce_connection()