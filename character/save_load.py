from .character import Character
import json
import os


def get_file_name(name): return "savedata/{}.json".format(name)

def save(character):

    if character.name == "" or character.name == None:
        character.name = "dave"
    try:
        file_name = get_file_name(character.name)
        with open(file_name, 'w') as f:
            f.write(json.dumps(character.__dict__))
    except:
        print("Error occured while saving.")

def load(character_name):
    if os.path.isfile(get_file_name(character_name)):
        data = None
        with open(get_file_name(character_name), 'r') as f:
            data = f.read()
            jsonData = json.loads(data)

        return Character(**jsonData)

def delete(character_name):
    if os.path.isfile(get_file_name(character_name)):

        answer = str(input("Type in the characters name to delete the character: "))
        if answer == character_name:
            os.remove(get_file_name(character_name))
            print("Character: {} has been deleted.".format(character_name))
        else:
            print("Character: {} was not deleted, input did not match the save name.".format(character_name))

    else:
        print("{} does not exist.".format(character_name))

def get_saves():
    directory = "savedata"

    file_list = []

    for file in os.listdir(directory):
        if file.endswith(".json"):
            file_list.append(file.split('.')[0])
    return file_list