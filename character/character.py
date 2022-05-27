from database.models import Level


class Character(object):
    def __init__(self):
        self.name = ""

        self.level = 1
        self.experience = 0

        self.inventory = []

        #location in game
        self.location = None
        self.position = None

        self.head_equipment = None
        self.chest_equipment = None
        self.leg_equipment = None
        self.weapon_equipment = None
        self.ammunition_equipment = None
        self.ammunition_count = None

        self.hitpoints = 3

        self.charisma = 1

        self.pierce_attack = 0
        self.slash_attack = 0
        self.blunt_attack = 0
        self.magical_attack = 0
        self.pierce_defence = 0
        self.slash_defence = 0
        self.blunt_defence = 0
        self.magical_defence = 0

    def __init__(self, name, level, experience, inventory, location, position, head_equipment,
                 chest_equipment, leg_equipment, weapon_equipment, ammunition_equipment,
                 ammunition_count, hitpoints, charisma, pierce_attack, slash_attack,
                 blunt_attack, magical_attack, pierce_defence, slash_defence, blunt_defence, magical_defence):

        self.name = name

        self.level = level
        self.experience = experience

        self.inventory = inventory

        #location in game
        self.location = location
        self.position = position

        self.head_equipment = head_equipment
        self.chest_equipment = chest_equipment
        self.leg_equipment = leg_equipment
        self.weapon_equipment = weapon_equipment
        self.ammunition_equipment = ammunition_equipment
        self.ammunition_count = ammunition_count

        self.hitpoints = hitpoints

        self.charisma = charisma

        self.pierce_attack = pierce_attack
        self.slash_attack = slash_attack
        self.blunt_attack = blunt_attack
        self.magical_attack = magical_attack
        self.pierce_defence = pierce_defence
        self.slash_defence = slash_defence
        self.blunt_defence = blunt_defence
        self.magical_defence = magical_defence

    def get_level(self):
        try:
            base_level = int(str(self.level))

            while True:

                if base_level == 100:
                    break

                data = Level.select(Level.min_exp).where(
                    Level.level == base_level)

                x = 0
                for row in data:
                    x = row.min_exp

                if self.experience >= x:
                    base_level += 1
                else:
                    break

            self.level = base_level
        except:
            print("not working")

        finally:
            return self.level
