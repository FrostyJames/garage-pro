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

@cli.command()
@click.option('--customer-id', prompt='Customer ID', type=int)
@click.option('--make', prompt='Vehicle make')
@click.option('--model', prompt='Vehicle model')
@click.option('--year', prompt='Year', type=int)
def add_vehicle(customer_id, make, model, year):
    session = SessionLocal()
    vehicle = Vehicle(make=make, model=model, year=year, customer_id=customer_id)
    session.add(vehicle)
    session.commit()
    click.echo(f"✅ Added vehicle: {make} {model} ({year})")

@cli.command()
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
@click.option('--type', prompt='Service type')
@click.option('--notes', prompt='Notes')
@click.option('--cost', prompt='Cost', type=float)
def log_service(vehicle_id, type, notes, cost):
    session = SessionLocal()
    service = ServiceRecord(
        vehicle_id=vehicle_id,
        service_type=type,
        date=datetime.today().date(),
        notes=notes,
        cost=cost
    )
    session.add(service)
    session.commit()
    click.echo(f"✅ Logged service: {type} for vehicle {vehicle_id}")

@cli.command()
@click.option('--vehicle-id', prompt='Vehicle ID', type=int)
def view_history(vehicle_id):
    session = SessionLocal()
    records = session.query(ServiceRecord).filter_by(vehicle_id=vehicle_id).all()
    if not records:
        click.echo("No service records found.")
        return
    for r in records:
        click.echo(f"{r.date} | {r.service_type} | Ksh {r.cost} | {r.notes}")

@cli.command()
@click.option('--make', default=None, help='Filter by vehicle make')
@click.option('--model', default=None, help='Filter by vehicle model')
@click.option('--year', default=None, type=int, help='Filter by manufacture year')
def filter_vehicles(make, model, year):
    """Filter vehicles by make, model, or year."""
    session = SessionLocal()
    query = session.query(Vehicle)

    if make:
        query = query.filter(Vehicle.make.ilike(f"%{make}%"))
    if model:
        query = query.filter(Vehicle.model.ilike(f"%{model}%"))
    if year:
        query = query.filter(Vehicle.year == year)

    results = query.all()
    if not results:
        click.echo("❌ No vehicles match the given filters.")
        return

    click.echo("🔍 Matching Vehicles:")
    for v in results:
        click.echo(f"- ID: {v.id} | {v.make} {v.model} ({v.year}) | Owner ID: {v.customer_id}")