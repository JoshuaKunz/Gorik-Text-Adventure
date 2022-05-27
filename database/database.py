from peewee import SqliteDatabase
from .models import *
class Database:
    db = SqliteDatabase('gorik.db')

    def init():
        tables = [Armor, Weapon, Shield, Potion, QuestItem, Ammunition, Tool]
        
        Database.db.create_tables(tables)