import click
from database import SessionLocal
from models import Customer, Vehicle, ServiceRecord
from datetime import datetime

@click.group()
def cli():
    """GaragePro CLI - Manage customers, vehicles, and service records."""
    pass