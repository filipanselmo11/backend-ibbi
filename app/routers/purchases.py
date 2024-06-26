from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.purchase import PurchaseRequest
from app.shared.dependencies import get_db, token_verifier
from sqlalchemy.orm import Session
from app.use_cases.purchase_use_cases import PurchaseUseCases

router = APIRouter(prefix='/purchase')

@router.post('/make', response_model=PurchaseRequest, status_code=201, dependencies=[Depends(token_verifier)])
async def make_purchase(purchase: PurchaseRequest, db: Session=Depends(get_db)):
    pc = PurchaseUseCases(db=db)
    pc.make_purchase(purchase=purchase)
    return JSONResponse(content={'msg': 'Compra realizada'})