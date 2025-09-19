import os
from simple_salesforce import Salesforce
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def test_salesforce_simple():
    print("🔍 Testando conexão com Salesforce (Simple)...")
    
    try:
        # Conecta usando simple-salesforce
        sf = Salesforce(
            username=os.getenv('SALESFORCE_USERNAME'),
            password=os.getenv('SALESFORCE_PASSWORD'),
            security_token=os.getenv('SALESFORCE_SECURITY_TOKEN'),
            instance_url=os.getenv('SALESFORCE_INSTANCE_URL')
        )
        
        # Teste simples: busca informações da org
        org_info = sf.query("SELECT Id, Name FROM Organization LIMIT 1")
        
        print("✅ Conexão bem-sucedida!")
        print(f"Org ID: {org_info['records'][0]['Id']}")
        print(f"Org Name: {org_info['records'][0]['Name']}")
        
        # Teste de leads
        leads = sf.query("SELECT Id, FirstName, LastName, Email FROM Lead LIMIT 5")
        print(f"📊 Encontrados {leads['totalSize']} leads na org")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False

if __name__ == "__main__":
    test_salesforce_simple()