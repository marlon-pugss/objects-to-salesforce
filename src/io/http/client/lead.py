from src.exception import CreateLeadException
from src.helpers import build_lead_out, build_lead_out_error, build_lead
from src.io.http.client.salesforce import post, get
import src.schema.lead as schema


def create_lead(payload: dict) -> schema.LeadOut:

    response = post("/Lead", payload)

    if not response.ok:
        raise CreateLeadException(build_lead_out_error(response))

    return build_lead_out(response)

def get_lead(lead_id: str) -> schema.Lead:

    response = get(f"/Lead/{lead_id}")

    if not response.ok:
        raise CreateLeadException(build_lead_out_error(response))

    return build_lead(response)