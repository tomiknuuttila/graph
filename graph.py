# libraries
import networkx as nx
import matplotlib.pyplot as plt

# Build your graph
g = nx.Graph()

# Luokat yhdistettynä
g.add_nodes_from([
    ('Adaptoituminen', {"class": "Yläluokka"}),
    ('Aktiivisuus', {"class": "Yläluokka"}),
    ('Analyyttiset- ja ongelmanratkaisutaidot', {"class": "Yläluokka"}),
    ('Analyyttiset taidot', {"class": "Alaluokka"}),
    ('Avoimuus', {"class": "Alaluokka"}),
    ('Haavoittuvuus', {"class": "Alaluokka"}),
    ('Henkilökohtaiset ominaisuudet', {"class": "Yläluokka"}),
    ('Ihmissuhdetaidot', {"class": "Alaluokka"}),
    ('Innovatiivisuus', {"class": "Yläluokka"}),
    ('Itseluottamus', {"class": "Alaluokka"}),
    ('Itsenäinen työskentely', {"class": "Alaluokka"}),
    ('Itsenäisyys', {"class": "Yläluokka"}),
    ('Itseohjautuvuus', {"class": "Yläluokka"}),
    ('Johtajuus', {"class": "Yläluokka"}),
    ('Johtaminen', {"class": "Alaluokka"}),
    ('Keskinäinen kunnioitus', {"class": "Alaluokka"}),
    ('Kommunikaatiotaidot', {"class": "Alaluokka"}),
    ('Kulttuurien tunteminen', {"class": "Alaluokka"}),
    ('Luottamus', {"class": "Alaluokka"}),
    ('Mittaus ja monitorointi', {"class": "Alaluokka"}),
    ('Ongelmanratkaisukyky', {"class": "Alaluokka"}),
    ('Oppiminen', {"class": "Yläluokka"}),
    ('Organisaation tunteminen', {"class": "Alaluokka"}),
    ('Organisointitaidot', {"class": "Yläluokka"}),
    ('Osallistuminen', {"class": "Alaluokka"}),
    ('Päätöksen tekeminen', {"class": "Alaluokka"}),
    ('Paineen ja stressin sietäminen', {"class": "Alaluokka"}),
    ('Rohkeus', {"class": "Alaluokka"}),
    ('Sosiaaliset taidot', {"class": "Yläluokka"}),
    ('Tietoisuus', {"class": "Yläluokka"}),
    ('Uuden oppiminen', {"class": "Alaluokka"}),
    ('Vastuullisuus', {"class": "Yläluokka"}),
    ('Yhteistyö', {"class": "Yläluokka"}),
    ('Yhteisvastuu', {"class": "Alaluokka"}),
])


# Adaptoituminen
g.add_edges_from([
    ('Paineen ja stressin sietäminen', 'Adaptoituminen'),
    ('Ongelmanratkaisukyky', 'Adaptoituminen'),
    ('Osallistuminen', 'Adaptoituminen'),
    ('Päätöksen tekeminen', 'Adaptoituminen'),
    ('Uuden oppiminen', 'Adaptoituminen'),
])
# Aktiivisuus

g.add_edges_from([
    ('Tietoisuus', 'Aktiivisuus'),
    ('Motivaatio', 'Aktiivisuus'),
    ('Yhteistyö', 'Aktiivisuus'),
    ('Uuden oppiminen', 'Aktiivisuus'),
    ('Osallistuminen', 'Aktiivisuus')
])

# Analyyttiset- ja ongelmanratkaisutaidot
g.add_edges_from([
    ('Itseluottamus', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Rohkeus', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Ongelmanratkaisukyky', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Paineen ja stressin sietäminen', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Päätöksen tekeminen', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Mittaus ja monitorointi', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Analyyttiset taidot', 'Analyyttiset- ja ongelmanratkaisutaidot')
])
# 'Henkilökohtaiset ominaisuudet'

g.add_edges_from([
    ('Keskinäinen kunnioitus', 'Henkilökohtaiset ominaisuudet'),
    ('Luottamus', 'Henkilökohtaiset ominaisuudet'),
    ('Haavoittuvuus', 'Henkilökohtaiset ominaisuudet'),
    ('Kommunikaatiotaidot', 'Henkilökohtaiset ominaisuudet'),
    ('Itseluottamus', 'Henkilökohtaiset ominaisuudet'),
    ('Rohkeus', 'Henkilökohtaiset ominaisuudet'),
    ('Paineen ja stressin sietäminen', 'Henkilökohtaiset ominaisuudet'),
    ('Päätöksen tekeminen', 'Henkilökohtaiset ominaisuudet'),
    ('Vastuullisuus', 'Henkilökohtaiset ominaisuudet'),
    ('Organisaation tunteminen', 'Henkilökohtaiset ominaisuudet'),
    ('Motivaatio', 'Henkilökohtaiset ominaisuudet'),
    ('Yhteistyö', 'Henkilökohtaiset ominaisuudet'),
    ('Ihmissuhdetaidot', 'Henkilökohtaiset ominaisuudet'),
    ('Analyyttiset taidot', 'Henkilökohtaiset ominaisuudet'),
    ('Kulttuurien tunteminen', 'Henkilökohtaiset ominaisuudet'),
    ('Johtaminen', 'Henkilökohtaiset ominaisuudet'),
    ('Avoimuus', 'Henkilökohtaiset ominaisuudet'),
    ('Osallistuminen', 'Henkilökohtaiset ominaisuudet'),
])

# Innovatiivisuus
g.add_edges_from([
    ('Rohkeus', 'Innovatiivisuus'),
    ('Ongelmanratkaisukyky', 'Innovatiivisuus'),
    ('Päätöksen tekeminen', 'Innovatiivisuus'),
    ('Uuden oppiminen', 'Innovatiivisuus'),
    ('Osallistuminen', 'Innovatiivisuus'),
])

# Itsenäisyys
g.add_edges_from([
    ('Itseluottamus', 'Itsenäisyys'),
    ('Paineen ja stressin sietäminen', 'Itsenäisyys'),
    ('Päätöksen tekeminen', 'Itsenäisyys'),
    ('Tietoisuus', 'Itsenäisyys'),
    ('Organisaation tunteminen', 'Itsenäisyys'),
    ('Motivaatio', 'Itsenäisyys'),
    ('Itsenäinen työskentely', 'Itsenäisyys'),
])

# Itseohjautuvuus
g.add_edges_from([
    ('Itsenäinen työskentely', 'Itseohjautuvuus'),
    ('Johtaminen', 'Itseohjautuvuus'),
])

# Johtajuus
g.add_edges_from([
    ('Motivaatio', 'Johtajuus'),
    ('Mittaus ja monitorointi', 'Johtajuus'),
    ('Ihmissuhdetaidot', 'Johtajuus'),
    ('Johtaminen', 'Johtajuus'),
])

# Oppiminen
g.add_edges_from([
    ('Motivaatio', 'Oppiminen'),
    ('Yhteistyö', 'Oppiminen'),
    ('Mittaus ja monitorointi', 'Oppiminen'),
    ('Uuden oppiminen', 'Oppiminen'),
    ('Analyyttiset taidot', 'Oppiminen'),
    ('Kulttuurien tunteminen', 'Oppiminen'),
    ('Johtaminen', 'Oppiminen'),
    ('Avoimuus', 'Oppiminen'),
])

# Organisointitaidot
g.add_edges_from([
    ('Ongelmanratkaisukyky', 'Organisointitaidot'),
    ('Päätöksen tekeminen', 'Organisointitaidot'),
    ('Tietoisuus', 'Organisointitaidot'),
    ('Mittaus ja monitorointi', 'Organisointitaidot'),
    ('Johtaminen', 'Organisointitaidot'),
])

# Sosiaaliset taidot
g.add_edges_from([
    ('Keskinäinen kunnioitus', 'Sosiaaliset taidot'),
    ('Luottamus', 'Sosiaaliset taidot'),
    ('Haavoittuvuus', 'Sosiaaliset taidot'),
    ('Kommunikaatiotaidot', 'Sosiaaliset taidot'),
    ('Itseluottamus', 'Sosiaaliset taidot'),
    ('Rohkeus', 'Sosiaaliset taidot'),
    ('Yhteistyö', 'Sosiaaliset taidot'),
    ('Ihmissuhdetaidot', 'Sosiaaliset taidot'),
    ('Kulttuurien tunteminen', 'Sosiaaliset taidot'),
    ('Johtaminen', 'Sosiaaliset taidot'),
    ('Avoimuus', 'Sosiaaliset taidot'),
    ('Osallistuminen', 'Sosiaaliset taidot'),
])

# Tietoisuus
g.add_edges_from([
    ('Yhteisvastuu', 'Tietoisuus'),
    ('Ongelmanratkaisukyky', 'Tietoisuus'),
    ('Päätöksen tekeminen', 'Tietoisuus'),
    ('Tietoisuus', 'Tietoisuus'),
    ('Organisaation tunteminen', 'Tietoisuus'),
    ('Mittaus ja monitorointi', 'Tietoisuus'),
    ('Ihmissuhdetaidot', 'Tietoisuus'),
    ('Analyyttiset taidot', 'Tietoisuus'),
    ('Kulttuurien tunteminen', 'Tietoisuus'),
    ('Avoimuus', 'Tietoisuus'),
    ('Osallistuminen', 'Tietoisuus'),
])

# Vastuullisuus
g.add_edges_from([
    ('Haavoittuvuus', 'Vastuullisuus'),
    ('Yhteisvastuu', 'Vastuullisuus'),
    ('Vastuullisuus', 'Vastuullisuus'),
    ('Organisaation tunteminen', 'Vastuullisuus'),
    ('Motivaatio', 'Vastuullisuus'),
    ('Mittaus ja monitorointi', 'Vastuullisuus'),
    ('Johtaminen', 'Vastuullisuus'),
    ('Avoimuus', 'Vastuullisuus'),
    ('Osallistuminen', 'Vastuullisuus'),
])

# Yhteistyö
g.add_edges_from([
    ('Keskinäinen kunnioitus', 'Yhteistyö'),
    ('Luottamus', 'Yhteistyö'),
    ('Haavoittuvuus', 'Yhteistyö'),
    ('Kommunikaatiotaidot', 'Yhteistyö'),
    ('Yhteisvastuu', 'Yhteistyö'),
    ('Vastuullisuus', 'Yhteistyö'),
    ('Ihmissuhdetaidot', 'Yhteistyö'),
    ('Kulttuurien tunteminen', 'Yhteistyö'),
    ('Avoimuus', 'Yhteistyö'),
    ('Osallistuminen', 'Yhteistyö'),
])


# Plot it
nx.draw_circular(g, with_labels=True, node_color=range(g.number_of_nodes()), node_size=1500)
plt.show()
