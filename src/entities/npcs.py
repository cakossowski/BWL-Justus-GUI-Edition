from .entities import Entity
import random

# this list contains all names that are used to generate random npcs at game start
npc_names_pool = [
    "Maximilian Monopol",
    "Charlotte Chart",
    "Frederik Fonds",
    "Viktoria Vorstand",
    "Benjamin Bilanz",
    "Isabella Investment",
    "Alexander Aktie",
    "Sophia Strategie",
    "Constantin Consulting",
    "Lara Liquidität",
    "Sebastian Soll",
    "Vanessa Vertrieb",
    "Julian Jahresabschluss",
    "Fiona Finanzierung",
    "Niklas Nutzwertanalyse",
    "Emilia Einkommen",
    "Tobias Tagesgeld",
    "Katharina Kredit",
    "Felix Fixkosten",
    "Melanie Marktanalyse",
    "Dominik Dividende",
    "Clara Controlling",
    "Lucas Leverage",
    "Annika Anlage",
    "Martin Mehrwert",
    "Julia Jura",
    "Fabian Faktura",
    "Sarah Steuer",
    "Philipp Portfolio",
    "Lena Leitzins"
]

# this list contains all catchphrases npcs will be assigned upon creation (also random)
npc_catchphrase_pool = [
    "Auf den Cent genau!",
    "Zeit ist Geld, Freunde!",
    "Immer schön liquide bleiben!",
    "Da muss der ROI stimmen!",
    "Kaufe niedrig, verkaufe hoch!",
    "Das ist eine Win-Win-Situation!",
    "Lass uns das netzwerken!",
    "Alles eine Frage der Bilanz!",
    "Kosten senken, Gewinne steigern!",
    "Nicht ohne meinen Taschenrechner!",
    "Das übersteigt meine Opportunitätskosten!",
    "Immer den Markt im Blick!",
    "Kannst du das amortisieren?",
    "Diversifikation ist der Schlüssel!",
    "Sind die Zinsen im Sinkflug?",
    "Das ist doch peanuts!",
    "Das parken wir mal kurz!",
    "Eine kluge Investition, würde ich sagen!",
    "Läuft das auf Provisionsbasis?",
    "Mehr Netto vom Brutto!",
    "Ist das steuerlich absetzbar?",
    "Das muss noch durchs Controlling!",
    "Bereit für den Börsengang?",
    "Ich habe da eine risikoarme Anlagestrategie!",
    "Das ist ja fast geschenkt!",
    "Cashflow ist König!",
    "Brauchen wir dafür ein Meeting?",
    "Der Kunde ist König, aber die Bilanz ist Gott!",
    "Das schreibe ich gleich in mein Moleskine!",
    "Haben wir dafür eine Case Study?"
]
# this is the initial empty pool where all created npc objects will be stored for each play through
npc_pool = []


# class to create NPCs, but needs generated items beforehand to properly work
class NPC(Entity):
    def __init__(self, name, inventory=None, catchphrase=None):
        super().__init__(name, inventory)
        self.catchphrase = catchphrase


"""
Function creates npc pool, the number of iteration is determined by the difficulty level,
which is given at the start of a game and chosen by player.
The formula to determine the amount of npcs is stil to be developed
"""


def create_npc_pool(amount_by_difficulty):
    copy_npc_pool_names = npc_names_pool.copy()
    while amount_by_difficulty > 0:
        new_npc_name = random.choice(copy_npc_pool_names)
        new_npc_item = random.choice(copy_item_pool_names)
