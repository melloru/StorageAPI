from fastapi import APIRouter
from app.products.dao import ProductDAO
from app.products.schemas import SProduct

router = APIRouter(prefix='/products', tags=['Работа с товаром'])


@router.get('/', summary='Получить список всех товаров')
async def get_all_products() -> list[SProduct]:
    return await ProductDAO.find_all()
