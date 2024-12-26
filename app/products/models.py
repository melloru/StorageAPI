from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, Integer

from app.database import Base, int_pk, str_uniq, str_null_true


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    description: Mapped[str_null_true]
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(id={self.id}, name={self.name!r},'
                f'price={self.price},'
                f'stock_quantity={self.stock_quantity})')
