# this list contains dicts that have item names and a description, which form the initial pool, where items are from

item_generation_pool = [
    {"name": "Goldener Taschenrechner", "description": "Unverzichtbar für jede Bilanzberechnung, glänzt im Dunkeln."},
    {"name": "Plüsch-Bull and Bear", "description": "Ein weiches Symbol für die Höhen und Tiefen des Marktes."},
    {"name": "Luxus-Kaffeetasse", "description": "Für den Kaffee zwischen zwei Meetings, in echtem Gold."},
    {"name": "Ewiger Kalender", "description": "Damit kein Quartalsabschluss verpasst wird."},
    {"name": "Ledergebundenes Notizbuch", "description": "Für alle brillanten Geschäftsideen."},
    {"name": "Marktschreier Megafon", "description": "Für den, der immer das letzte Wort im Markt haben will."},
    {"name": "Networking-Handbuch", "description": "Jedes Kapitel ein neuer Kontakt!"},
    {"name": "Aktien-Zauberwürfel", "description": "Finden Sie die richtige Kombination zum Reichtum."},
    {"name": "Risiko-Würfel", "description": "Für Entscheidungen, die zu schwer für Münzwurf sind."},
    {"name": "Krawattenhalter 'Executive'", "description": "Für den professionellen Auftritt in jedem Meeting."},
    {"name": "Stressball 'Börsencrash'", "description": "Für die Hände, wenn der Markt mal wieder verrückt spielt."},
    {"name": "Moleskine für Milliardäre", "description": "Ihre Ideen sind Gold wert? Dann holen sie dieses Notizbuch!"},
    {"name": "Sparbuch-Safe", "description": "Ein sicherer Ort für Ihre kleinen und großen Ersparnisse."},
    {"name": "Excel-Zauberstab", "description": "Macht jede Tabelle zum Meisterwerk."},
    {"name": "Investor's Tee-Set", "description": "Für die ruhigen Momente zwischen den Investitionen."},
    {"name": "Wirtschaftsorakel", "description": "Ein bisschen Hilfe bei schwierigen Geschäftsentscheidungen."},
    {"name": "Monopol-Spielkarten", "description": "Für den spielerischen Umgang mit dem Wettbewerb."},
    {"name": "Bilanz-Bumerang", "description": "Es kommt immer zurück, vor allem bei der Bilanz."},
    {"name": "Gewinnmaximierungs-Brille", "description": "Damit Sie immer das große Geld im Blick haben."},
    {"name": "Liquiditäts-Lampe", "description": "Erleuchtung in Finanzfragen."},
    {"name": "Trend-Teleskop", "description": "Blicken Sie in die Zukunft der Märkte."},
    {"name": "Dividenden-Detektor", "description": "Finden Sie die besten Aktienauszahlungen."},
    {"name": "Kosten-Kalkulator", "description": "Rechnet schneller als der Schatten."},
    {"name": "Rentabilitäts-Rechen", "description": "Für die perfekte Anbauplanung Ihrer Finanzen."},
    {"name": "Gewinnmargen-Messer", "description": "Misst präzise den Erfolg Ihrer Geschäfte."},
    {"name": "Marketing-Magnet", "description": "Zieht Kunden magisch an."},
    {"name": "Vertriebs-Ventilator", "description": "Verteilt Ihre Produkte überall hin."},
    {"name": "Branding-Bürste", "description": "Für das glänzende Image Ihrer Marke."},
    {"name": "Cashflow-Kompass", "description": "Weist den Weg durch finanzielle Nebel."},
    {"name": "Strategie-Sternenkarte", "description": "Navigieren Sie durch das Universum der Geschäftswelt."},
    {"name": "Erfolgs-Echolot", "description": "Misst die Tiefe Ihres Geschäftserfolgs."},
    {"name": "Zielgruppen-Zirkel", "description": "Zeichnet den perfekten Kundenkreis."},
    {"name": "Budget-Balance-Board", "description": "Hält Ihre Finanzen im Gleichgewicht."},
    {"name": "Umsatz-Uhr", "description": "Tickt im Takt Ihrer Verkäufe."},
    {"name": "Preis-Pendel", "description": "Findet das optimale Preisniveau."},
    {"name": "Rabatt-Reißzwecke", "description": "Spitz für die besten Deals."},
    {"name": "Provision-Puzzle", "description": "Setzen Sie die Teile Ihrer Provision zusammen."},
    {"name": "Finanzfluss-Flaschenpost", "description": "Trägt Ihre Investitionen über weite Meere."},
    {"name": "Börsen-Bumerang", "description": "Für den Handel, der zurückkommt."},
    {"name": "Geschäftsgeist-Glas", "description": "Für den Durst nach mehr Erfolg."},
    {"name": "Rendite-Radar", "description": "Ortet die profitabelsten Anlagen."},
    {"name": "Verkaufsvolumen-Vuvuzela", "description": "Machen Sie Lärm für Ihr Produkt."},
    {"name": "Anlage-Assistent", "description": "Ein kleiner Helfer für große Investments."},
    {"name": "Konjunktur-Konfetti", "description": "Für die Feier eines jeden Wirtschaftsaufschwungs."},
    {"name": "Portfolio-Pyramide", "description": "Bauen Sie Ihr finanzielles Reich auf."},
    {"name": "Markt-Mandala", "description": "Für die entspannte Sicht auf den Markt."},
    {"name": "Wachstums-Wecker", "description": "Weckt Sie, wenn es Zeit ist zu expandieren."},
    {"name": "Bilanzen-Balalaika", "description": "Spielt die Melodie des Erfolgs."},
    {"name": "Kredit-Karussell", "description": "Dreht sich immer schneller mit Ihren Finanzen."},
    {"name": "Diversifikations-Dudelsack", "description": "Spielt die Musik der vielfältigen Anlagen."},
    {"name": "Effizienz-Eieruhr", "description": "Zählt die Minuten bis zum nächsten Geschäftsabschluss."},
    {"name": "Steuer-Schlüsselanhänger", "description": "Hält Ihre Steuerangelegenheiten zusammen."},
    {"name": "Innovations-Iglu", "description": "Ein kühler Ort für heiße Ideen."},
    {"name": "Risikomanagement-Rucksack", "description": "Tragen Sie Ihre Risiken mit Leichtigkeit."},
    {"name": "Netzwerk-Nadelkissen", "description": "Für die kleinen Stiche im Geschäftsleben."}
]

""" 
Class is used to create objects named "Items" to use as trade objects between player / npc
name - Name of created Item
description - funny description of the given item (no functional purpose,, just for the lulz)
buy_value - determines the price at which it can be bought from the npc
sell_value - determines the price in the daily sell off at the end of the day
"""


class Items:
    def __init__(self, name, description, buy_value, sell_value):
        self.name = name
        self.description = description
        self.buy_value = buy_value
        self.sell_value = sell_value


"""

"""


def create_item_pool_object(amount_by_difficulty):
    copy_item_pool_names = item_generation_pool.copy()
    while amount_by_difficulty > 0:
