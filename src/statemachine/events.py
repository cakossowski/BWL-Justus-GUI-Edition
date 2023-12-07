from entities import npcs
import random
"""
This file contains all possible events in the game (like npc encounters, random events, trading with npcs)
"""


def random_selection_npc:
    """
    Function selects random npcs from created pool "npc_pool" to provide
    as value for random encounter and pops it from list to avoid multi encounters
    :return:
    "random_selected_npc" - Class object with "name, inventory, catchphrase"
    """
    random_index = random.randint(0,len(npcs.npc_pool) - 1)
    random_selected_npc = npcs.npc_pool.pop[random_index]
    return random_selected_npc
def player_encounters_npc:
    """

    :return:
    """
