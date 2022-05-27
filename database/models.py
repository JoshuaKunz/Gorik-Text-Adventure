from peewee import *

db = SqliteDatabase('gorik.db')

class BaseModel(Model):
    class Meta:
        database = db

class Character(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)

    level = IntegerField(null=False)
    experience = IntegerField(null=False)

    #inventory & equipped items
    inventory = IntegerField(null=False)

    #location in game
    location = TextField(null=False)
    position = IntegerField(null=False)
    
    head_equipment = IntegerField(null=True)
    chest_equipment = IntegerField(null=True)
    leg_equipment = IntegerField(null=True)
    weapon_equipment = IntegerField(null=True)
    ammunition_equipment = IntegerField(null=True)
    ammunition_count = IntegerField(null=True)

    hitpoints = IntegerField(null=False)

    #non combat skills
    charisma = IntegerField(null=False)
    
    #stats
    #attack
    pierce_attack = IntegerField(null=False)
    slash_attack = IntegerField(null=False)
    blunt_attack = IntegerField(null=False)
    magical_attack = IntegerField(null=False)

    #defence
    pierce_defence = IntegerField(null=False)
    slash_defence = IntegerField(null=False)
    blunt_defence = IntegerField(null=False)
    magical_defence = IntegerField(null=False)

class ItemType:
    armor = 1
    weapon = 2
    potion = 3
    quest = 4
    ammunition = 5
    shield = 6
    tool = 7

class ArmorType:
    head = 1
    chest = 2
    legs = 3

class Armor(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    item_type = IntegerField(null=False)
    level_requirement = IntegerField(null=False)
    pierce_defence = IntegerField(null=False)
    slash_defence = IntegerField(null=False)
    blunt_defence = IntegerField(null=False)
    magical_defence = IntegerField(null=False)
    description = TextField(null=True)

class WeaponType:
    melee = 1
    range = 2
    magic = 3

class Weapon(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    item_type = IntegerField(null=False)
    level_requirement = IntegerField(null=False)
    pierce_attack = IntegerField(null=False)
    slash_attack = IntegerField(null=False)
    blunt_attack = IntegerField(null=False)
    magical_attack = IntegerField(null=False)
    requires_ammunition = BooleanField(null=False)
    description = TextField(null=True)

class ShieldType:
    round_shield = 1
    tower_shield = 2
    buckler = 3

class Shield(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    item_type = IntegerField(null=False)
    level_requirement = IntegerField(null=False)
    pierce_defence = IntegerField(null=False)
    slash_defence = IntegerField(null=False)
    blunt_defence = IntegerField(null=False)
    magical_defence = IntegerField(null=False)
    description = TextField(null=True)

class PotionType:
    health = 1
    attack = 2
    defence = 3
    antidote = 4

class Potion(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    item_type = IntegerField(null=False)
    boost_amount = IntegerField(null=False)
    description = TextField(null=False)

class QuestItem(BaseModel):
    id = PrimaryKeyField()
    quest_id = IntegerField(null=False)
    name = TextField(unique=True, null=False)
    item_type = IntegerField(null=False)
    description = TextField(null=False)

class AmmunitionType:
    arrow = 1
    bolt = 2
    pages = 3

class Ammunition(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    item_type = IntegerField(null=False)
    damage_bonus = IntegerField(null=False)
    description = TextField(null=False)

class Tool(BaseModel):
    id = PrimaryKeyField()
    name = TextField(unique=True, null=False)
    type = IntegerField(null=False)
    description = TextField(null=False)

class Level(BaseModel):
    level = PrimaryKeyField()
    min_exp = IntegerField(null=False)