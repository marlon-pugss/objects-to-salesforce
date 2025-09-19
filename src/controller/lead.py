import logging
import src.schema.lead as schema
from src.exception import NotFoundException
from src.io.http.client.lead import create_lead, get_lead

logger = logging.getLogger()


def create(lead: schema.Lead) -> schema.LeadOut | None:
    try:
        result = create_lead(lead.model_dump(by_alias=True, exclude_none=True))
        logger.info(f"Lead created successfully with ID: {result.id}")
        return result
    except Exception as e:
        logger.error(f"Error creating lead: {str(e)}")
        raise e

def get(lead_id: str) -> schema.Lead:
    try:
        lead = get_lead(lead_id)

        if not lead:
            raise NotFoundException("Lead Not found")

        logger.info(f"Lead retrieved successfully with ID: {lead_id}")
        return lead
    except Exception as e:
        logger.error(f"Error getting lead: {str(e)}")
        raise e