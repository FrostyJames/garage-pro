import click
from database import SessionLocal
from models import Customer, Vehicle, ServiceRecord
from datetime import datetime

@click.group()
def cli():
    """GaragePro CLI - Manage customers, vehicles, and service records."""
    pass

@cli.command()
@click.option('--name', prompt='Customer name')
@click.option('--phone', prompt='Phone number')
@click.option('--email', prompt='Email')
@click.option('--address', prompt='Address')
def add_customer(name, phone, email, address):
    session = SessionLocal()
    customer = Customer(name=name, phone_number=phone, email=email, address=address)
    session.add(customer)
    session.commit()
    click.echo(f"✅ Added customer: {name}")