def limit_size(field):
    return field[:254] if field else None

def cleanup_to_salesforce(payload):
    # Remove todos os campos exceto os essenciais
    clean_payload = {}
    
    # Mantém apenas campos básicos obrigatórios
    if payload.get("LastName"):
        clean_payload["LastName"] = payload["LastName"]
    if payload.get("FirstName"):
        clean_payload["FirstName"] = payload["FirstName"] 
    if payload.get("Email"):
        clean_payload["Email"] = payload["Email"]
    if payload.get("Phone"):
        clean_payload["Phone"] = payload["Phone"]
        
    # Company é obrigatório no SF, usar LastName como fallback
    clean_payload["Company"] = payload.get("Company", payload.get("LastName", "Unknown"))

    return clean_payload