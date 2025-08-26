from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Float
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)

    vehicles = relationship("Vehicle", back_populates="customer")



class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String)
    year = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="vehicles")
    service_records = relationship("ServiceRecord", back_populates="vehicle")


class ServiceRecord(Base):
    __tablename__ = 'service_records'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    service_type = Column(String)
    date = Column(Date)
    notes = Column(Text)
    cost = Column(Float)

    vehicle = relationship("Vehicle", back_populates="service_records")

