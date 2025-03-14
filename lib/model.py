from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="customer", nullable=False)

    rentals = relationship("Rental", back_populates="customer")

    # ORM Methods
    @classmethod
    def create(cls, session, **kwargs):
        customer = cls(**kwargs)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', role='{self.role}')>"

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    available = Column(Boolean, default=True, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

    rentals = relationship("Rental", back_populates="car")


    @classmethod
    def create(cls, session, **kwargs):
        car = cls(**kwargs)
        session.add(car)
        session.commit()
        return car

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
    def __repr__(self):
        return f"<Car(id={self.id}, make='{self.make}', model='{self.model}', year={self.year}, price={self.price}, available={self.available})>"


class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    return_date = Column(DateTime, nullable=True)
    rental_date = Column(DateTime, nullable=False)

    car = relationship("Car", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")


    @classmethod
    def create(cls, session, **kwargs):
        rental = cls(**kwargs)
        session.add(rental)
        session.commit()
        return rental

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
    def __repr__(self):
        return f"<Rental(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, rental_date={self.rental_date}, return_date={self.return_date})>"