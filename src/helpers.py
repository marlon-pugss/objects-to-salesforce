import src.schema.lead as schema


def build_lead(body) -> schema.Lead:

    response = body.json()

    last_name = response["LastName"]
    email = response["Email"]
    phone = response["Phone"]
    company = response["Company"]
    lead_id = response["Id"]
    first_name = response["FirstName"]

    return schema.Lead(
        last_name=last_name,
        email=email,
        phone=phone,
        company=company,
        id=lead_id,
        first_name=first_name
    )

def build_lead_out_error(response):
    if response.content:
        return response.json()
    return {"error": "Unknown error"}

def build_lead_out(response) -> schema.LeadOut:
    lead_id = response.json()["id"]

    return schema.LeadOut(id=lead_id)
