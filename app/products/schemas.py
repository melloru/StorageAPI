from pydantic import BaseModel, validator, Field, ConfigDict


class SProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length=1, max_length=50, description='Название товара от 1 до 30 символов')
    description: str | None = Field(None, max_length=150, description='Описание товара до 150 символов')
    price: float = Field(..., ge=0.01, description='Цена товара от 0.01')
    stock_quantity: int = Field(..., ge=0, description='Кол-во товара на складе')

