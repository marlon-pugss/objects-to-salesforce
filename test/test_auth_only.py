import os
import sys
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def test_auth_and_create():
    print("🔍 Testando autenticação e criação direta...")
    
    # Credenciais
    client_id = os.getenv('SALESFORCE_CLIENT_ID')
    client_secret = os.getenv('SALESFORCE_CLIENT_SECRET')
    username = os.getenv('SALESFORCE_USERNAME')
    password = os.getenv('SALESFORCE_PASSWORD')
    security_token = os.getenv('SALESFORCE_SECURITY_TOKEN')
    instance_url = os.getenv('SALESFORCE_INSTANCE_URL')
    
    # 1. Obter token
    auth_url = f"{instance_url}/services/oauth2/token"
    auth_data = {
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': f"{password}{security_token}"
    }
    
    try:
        print("🔐 Obtendo token de acesso...")
        auth_response = requests.post(auth_url, data=auth_data)
        
        if auth_response.status_code != 200:
            print(f"❌ Erro na autenticação: {auth_response.text}")
            return False
            
        token_data = auth_response.json()
        access_token = token_data['access_token']
        sf_instance_url = token_data['instance_url']
        
        print("✅ Token obtido com sucesso!")
        
        # 2. Criar lead
        print("📝 Criando lead de teste...")
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        lead_data = {
            "FirstName": "Teste",
            "LastName": "Claude",
            "Email": "teste.claude@example.com",
            "Company": "Test Company"
        }
        
        lead_url = f"{sf_instance_url}/services/data/v58.0/sobjects/Lead"
        
        lead_response = requests.post(lead_url, json=lead_data, headers=headers)
        
        if lead_response.status_code == 201:
            result = lead_response.json()
            print(f"✅ Lead criado com sucesso! ID: {result['id']}")
            return True
        else:
            print(f"❌ Erro ao criar lead: {lead_response.status_code} - {lead_response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    test_auth_and_create()