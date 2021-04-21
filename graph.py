# libraries
import networkx as nx
import matplotlib.pyplot as plt

# Build your graph
graph = nx.Graph()

# Luokat yhdistettynä
graph.add_nodes_from([
    'Adaptoituminen',
    'Aktiivisuus',
    'Analyyttiset- ja ongelmanratkaisutaidot',
    'Analyyttiset taidot',
    'Avoimuus',
    'Haavoittuvuus',
    'Henkilökohtaiset ominaisuudet',
    'Ihmissuhdetaidot',
    'Innovatiivisuus',
    'Itseluottamus',
    'Itsenäinen työskentely',
    'Itsenäisyys',
    'Itseohjautuvuus',
    'Johtajuus',
    'Johtaminen',
    'Keskinäinen kunnioitus',
    'Kommunikaatiotaidot',
    'Kulttuurien tunteminen',
    'Luottamus',
    'Mittaus ja monitorointi',
    'Ongelmanratkaisukyky',
    'Oppiminen',
    'Organisaation tunteminen',
    'Organisointitaidot',
    'Osallistuminen',
    'Päätöksen tekeminen',
    'Paineen ja stressin sietäminen',
    'Rohkeus',
    'Sosiaaliset taidot',
    'Tietoisuus',
    'Uuden oppiminen',
    'Vastuullisuus',
    'Yhteistyö',
    'Yhteisvastuu'])


# Adaptoituminen
graph.add_edges_from([
    ('Paineen ja stressin sietäminen', 'Adaptoituminen'),
    ('Ongelmanratkaisukyky', 'Adaptoituminen'),
    ('Osallistuminen', 'Adaptoituminen'),
    ('Päätöksen tekeminen', 'Adaptoituminen'),
    ('Uuden oppiminen', 'Adaptoituminen'),
])
# Aktiivisuus

graph.add_edges_from([
    ('Tietoisuus', 'Aktiivisuus'),
    ('Motivaatio', 'Aktiivisuus'),
    ('Yhteistyö', 'Aktiivisuus'),
    ('Uuden oppiminen', 'Aktiivisuus'),
    ('Osallistuminen', 'Aktiivisuus')
])

# Analyyttiset- ja ongelmanratkaisutaidot
graph.add_edges_from([
    ('Itseluottamus', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Rohkeus', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Ongelmanratkaisukyky', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Paineen ja stressin sietäminen', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Päätöksen tekeminen', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Mittaus ja monitorointi', 'Analyyttiset- ja ongelmanratkaisutaidot'),
    ('Analyyttiset taidot', 'Analyyttiset- ja ongelmanratkaisutaidot')
])
#'Henkilökohtaiset ominaisuudet'

graph.add_edges_from([
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
graph.add_edges_from([
    ('Rohkeus', 'Innovatiivisuus'),
    ('Ongelmanratkaisukyky', 'Innovatiivisuus'),
    ('Päätöksen tekeminen', 'Innovatiivisuus'),
    ('Uuden oppiminen', 'Innovatiivisuus'),
    ('Osallistuminen', 'Innovatiivisuus'),
])

# Itsenäisyys
graph.add_edges_from([
    ('Itseluottamus', 'Itsenäisyys'),
    ('Paineen ja stressin sietäminen', 'Itsenäisyys'),
    ('Päätöksen tekeminen', 'Itsenäisyys'),
    ('Tietoisuus', 'Itsenäisyys'),
    ('Organisaation tunteminen', 'Itsenäisyys'),
    ('Motivaatio', 'Itsenäisyys'),
    ('Itsenäinen työskentely', 'Itsenäisyys'),
])

# Itseohjautuvuus
graph.add_edges_from([
    ('Itsenäinen työskentely', 'Itseohjautuvuus'),
    ('Johtaminen', 'Itseohjautuvuus'),
])

# Johtajuus
graph.add_edges_from([
    ('Motivaatio', 'Johtajuus'),
    ('Mittaus ja monitorointi', 'Johtajuus'),
    ('Ihmissuhdetaidot', 'Johtajuus'),
    ('Johtaminen', 'Johtajuus'),
])

# Oppiminen
graph.add_edges_from([
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
graph.add_edges_from([
    ('Ongelmanratkaisukyky', 'Organisointitaidot'),
    ('Päätöksen tekeminen', 'Organisointitaidot'),
    ('Tietoisuus', 'Organisointitaidot'),
    ('Mittaus ja monitorointi', 'Organisointitaidot'),
    ('Johtaminen', 'Organisointitaidot'),
])

# Sosiaaliset taidot
graph.add_edges_from([
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
graph.add_edges_from([
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
graph.add_edges_from([
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
graph.add_edges_from([
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
nx.draw(graph, with_labels=True)
plt.show()
