import sys
from dotenv import load_dotenv

# Adiciona o diret\u00f3rio src ao path
sys.path.append('/src')

from src.io.http.client.salesforce import create_lead, update_lead

# Carrega vari\u00e1veis do .env
load_dotenv()

def test_create_lead():
    print("🧪 Testando cria\u00e7\u00e3o de lead...")
    
    payload = {
        "FirstName": "Jo\u00e3o",
        "LastName": "Silva",
        "Email": "joao.silva@test.com",
        "Company": "Empresa Teste",
        "Phone": "11999999999"
    }
    
    try:
        result = create_lead(payload)
        print(f"✅ Lead criado com sucesso!")
        print(f"Lead ID: {result}")
        return result
    except Exception as e:
        print(f"❌ Erro ao criar lead: {e}")
        return None

def test_update_lead(lead_id):
    print(f"🧪 Testando atualiza\u00e7\u00e3o do lead {lead_id}...")
    
    payload = {
        "Phone": "11888888888",
        "Status": "Working - Contacted"
    }
    
    try:
        update_lead(lead_id, payload)
        print("✅ Lead atualizado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar lead: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testando integra\u00e7\u00e3o direta com Salesforce...")
    
    # Teste de cria\u00e7\u00e3o
    lead_result = test_create_lead()
    
    # Teste de atualiza\u00e7\u00e3o (se a cria\u00e7\u00e3o funcionou)
    # if lead_result:
    #     test_update_lead(lead_result.id)