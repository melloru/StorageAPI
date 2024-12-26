from fastapi import APIRouter
from app.products.dao import ProductDAO
from app.products.schemas import SProduct

router = APIRouter(prefix='/products', tags=['Работа с товаром'])


@router.get('/', summary='Получить список всех товаров')
async def get_all_products() -> list[SProduct]:
    return await ProductDAO.find_all()


@router.get('/{id}', summary='Получить товар по ID')
async def get_product_by_id(product_id: int) -> SProduct | dict:
    result = await ProductDAO.find_one_or_none(product_id)
    if result is None:
        return {'message': f'Товара с ID {product_id} не существует.'}
    return result
