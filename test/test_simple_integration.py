import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def test_salesforce_integration():
    print("🚀 Testando integração com simple-salesforce...")
    
    try:
        from simple_salesforce import Salesforce
        
        # Autentica
        sf = Salesforce(
            username=os.getenv('SALESFORCE_USERNAME'),
            password=os.getenv('SALESFORCE_PASSWORD'),
            security_token=os.getenv('SALESFORCE_SECURITY_TOKEN'),
            instance_url=os.getenv('SALESFORCE_INSTANCE_URL')
        )
        
        print("✅ Autenticação bem-sucedida!")
        print(f"Session ID: {sf.session_id[:20]}...")
        print(f"Base URL: {sf.base_url}")
        
        # Testa criação de lead usando requests com o token
        headers = {
            'Authorization': f'Bearer {sf.session_id}',
            'Content-Type': 'application/json'
        }
        
        lead_data = {
            "FirstName": "Teste",
            "LastName": "Integração",
            "Email": "teste.integracao@example.com", 
            "Company": "Teste Company"
        }
        
        url = f"{sf.base_url}/sobjects/Lead"
        
        print("📝 Criando lead via API REST...")
        response = requests.post(url, json=lead_data, headers=headers)
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Lead criado! ID: {result['id']}")
            return result['id']
        else:
            print(f"❌ Erro: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

if __name__ == "__main__":
    test_salesforce_integration()