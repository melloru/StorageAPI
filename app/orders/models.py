from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

from app.database import Base, int_pk, str_null_false
from app.products.models import Product


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int_pk]
    status: Mapped[str_null_false]

    items: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='order')

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(id={self.id},'
                f'created_at={self.created_at},'
                f'status={self.status!r})')


class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int_pk]
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    order: Mapped['Order'] = relationship('Order', back_populates='items')
    product: Mapped['Product'] = relationship('Product')

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(id={self.id},'
                f'order_id={self.order_id},'
                f'product_id={self.product_id},'
                f'quantity={self.quantity})')
