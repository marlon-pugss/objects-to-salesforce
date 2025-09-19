from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import src.controller.lead as controller
from src.exception import CreateLeadException, NotFoundException
from src.schema.lead import Lead

router = APIRouter()


@router.post("/leads")
async def create(lead: Lead) -> JSONResponse:
    try:
        lead_out = controller.create(lead)
        if lead_out:
            return JSONResponse(status_code=201, content=lead_out.model_dump())
        else:
            return JSONResponse(status_code=202, content={})

    except CreateLeadException as e:
        error_detail = e.args[0] if e.args else str(e)
        status_code = getattr(error_detail, 'status_code', 400)
        detail = getattr(error_detail, 'detail', error_detail)
        raise HTTPException(status_code=status_code, detail=detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error create Lead")

@router.get("/leads/{lead_id}")
async def get(lead_id: str) -> JSONResponse:
    try:
        lead = controller.get(lead_id)
        return JSONResponse(status_code=200, content=lead.model_dump(mode='json'))

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error get Lead")