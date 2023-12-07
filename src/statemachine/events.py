from entities import npcs
from items import items
import random
"""
This file contains all possible events in the game (like npc encounters, random events, trading with npcs)
"""


def random_selection_npc():
    """
    Function selects random npcs from created pool "npc_pool" to provide
    as value for random encounter and pops it from list to avoid multi encounters
    :return:
    "random_selected_npc" - Class object with "name, inventory, catchphrase"
    """
    random_index = random.randint(0, len(npcs.npc_pool) - 1)
    random_selection = npcs.npc_pool.pop[random_index]
    return random_selection


def npc_speech(selected_npc):
    """
    This function just creates the speech part for a npc and prints the necessary statements
    :param selected_npc:
    :return: no return value
    """
    print(f" Hey ich bin {selected_npc.name} und mein Motto ist:'{selected_npc.catchphrase}'")
    print(f"Ich biete dir {selected_npc.inventory.name} - {selected_npc.inventory.description}!")
    print(f"Kostet auch nur: {selected_npc.inventory.buy_value} EUR - ich schwör dir, damit machst' Gewinn!")


def player_encounters_npc():
    """

    :return:
    """
    random_npc = random_selection_npc()


