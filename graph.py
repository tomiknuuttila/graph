# libraries
import networkx as nx
import matplotlib.pyplot as plt

# Build your graph
g = nx.Graph()

# Luokat yhdistettynä
g.add_node('Adaptoituminen', nodetype='Yläluokka')
g.add_node('Aktiivisuus', nodetype='Yläluokka')
g.add_node('Analyyttiset- ja ongelmanratkaisutaidot', nodetype='Yläluokka')
g.add_node('Analyyttiset taidot', nodetype='Alaluokka')
g.add_node('Avoimuus', nodetype='Alaluokka')
g.add_node('Haavoittuvuus', nodetype='Alaluokka')
g.add_node('Henkilökohtaiset ominaisuudet', nodetype='Yläluokka')
g.add_node('Ihmissuhdetaidot', nodetype='Alaluokka')
g.add_node('Innovatiivisuus', nodetype='Yläluokka')
g.add_node('Itseluottamus', nodetype='Alaluokka')
g.add_node('Itsenäinen työskentely', nodetype='Alaluokka')
g.add_node('Itsenäisyys', nodetype='Yläluokka')
g.add_node('Itseohjautuvuus', nodetype='Yläluokka')
g.add_node('Johtajuus', nodetype='Yläluokka')
g.add_node('Johtaminen', nodetype='Alaluokka')
g.add_node('Keskinäinen kunnioitus', nodetype='Alaluokka')
g.add_node('Kommunikaatiotaidot', nodetype='Alaluokka')
g.add_node('Kulttuurien tunteminen', nodetype='Alaluokka')
g.add_node('Luottamus', nodetype='Alaluokka')
g.add_node('Mittaus ja monitorointi', nodetype='Alaluokka')
g.add_node('Ongelmanratkaisukyky', nodetype='Alaluokka')
g.add_node('Oppiminen', nodetype='Yläluokka')
g.add_node('Organisaation tunteminen', nodetype='Alaluokka')
g.add_node('Organisointitaidot', nodetype='Yläluokka')
g.add_node('Osallistuminen', nodetype='Alaluokka')
g.add_node('Päätöksen tekeminen', nodetype='Alaluokka')
g.add_node('Paineen ja stressin sietäminen', nodetype='Alaluokka')
g.add_node('Rohkeus', nodetype='Alaluokka')
g.add_node('Sosiaaliset taidot', nodetype='Yläluokka')
g.add_node('Tietoisuus', nodetype='Yläluokka')
g.add_node('Uuden oppiminen', nodetype='Alaluokka')
g.add_node('Vastuullisuus', nodetype='Yläluokka')
g.add_node('Yhteistyö', nodetype='Yläluokka')
g.add_node('Yhteisvastuu', nodetype='Alaluokka')

# Adaptoituminen
g.add_weighted_edges_from([
    ('Paineen ja stressin sietäminen', 'Adaptoituminen', 1),
    ('Ongelmanratkaisukyky', 'Adaptoituminen', 1),
    ('Osallistuminen', 'Adaptoituminen', 1),
    ('Päätöksen tekeminen', 'Adaptoituminen', 1),
    ('Uuden oppiminen', 'Adaptoituminen', 1),
])
# Aktiivisuus

g.add_weighted_edges_from([
    ('Tietoisuus', 'Aktiivisuus', 2),
    ('Motivaatio', 'Aktiivisuus', 2),
    ('Yhteistyö', 'Aktiivisuus', 2),
    ('Uuden oppiminen', 'Aktiivisuus', 2),
    ('Osallistuminen', 'Aktiivisuus', 2),
])

# Analyyttiset- ja ongelmanratkaisutaidot
g.add_weighted_edges_from([
    ('Itseluottamus', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Rohkeus', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Ongelmanratkaisukyky', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Paineen ja stressin sietäminen', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Päätöksen tekeminen', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Mittaus ja monitorointi', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
    ('Analyyttiset taidot', 'Analyyttiset- ja ongelmanratkaisutaidot', 3),
])
# 'Henkilökohtaiset ominaisuudet'

g.add_weighted_edges_from([
    ('Keskinäinen kunnioitus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Luottamus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Haavoittuvuus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Kommunikaatiotaidot', 'Henkilökohtaiset ominaisuudet', 4),
    ('Itseluottamus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Rohkeus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Paineen ja stressin sietäminen', 'Henkilökohtaiset ominaisuudet', 4),
    ('Päätöksen tekeminen', 'Henkilökohtaiset ominaisuudet', 4),
    ('Vastuullisuus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Organisaation tunteminen', 'Henkilökohtaiset ominaisuudet', 4),
    ('Motivaatio', 'Henkilökohtaiset ominaisuudet', 4),
    ('Yhteistyö', 'Henkilökohtaiset ominaisuudet', 4),
    ('Ihmissuhdetaidot', 'Henkilökohtaiset ominaisuudet', 4),
    ('Analyyttiset taidot', 'Henkilökohtaiset ominaisuudet', 4),
    ('Kulttuurien tunteminen', 'Henkilökohtaiset ominaisuudet', 4),
    ('Johtaminen', 'Henkilökohtaiset ominaisuudet', 4),
    ('Avoimuus', 'Henkilökohtaiset ominaisuudet', 4),
    ('Osallistuminen', 'Henkilökohtaiset ominaisuudet', 4),
])

# Innovatiivisuus
g.add_weighted_edges_from([
    ('Rohkeus', 'Innovatiivisuus', 5),
    ('Ongelmanratkaisukyky', 'Innovatiivisuus', 5),
    ('Päätöksen tekeminen', 'Innovatiivisuus', 5),
    ('Uuden oppiminen', 'Innovatiivisuus', 5),
    ('Osallistuminen', 'Innovatiivisuus', 5),
])

# Itsenäisyys
g.add_weighted_edges_from([
    ('Itseluottamus', 'Itsenäisyys', 6),
    ('Paineen ja stressin sietäminen', 'Itsenäisyys', 6),
    ('Päätöksen tekeminen', 'Itsenäisyys', 6),
    ('Tietoisuus', 'Itsenäisyys', 6),
    ('Organisaation tunteminen', 'Itsenäisyys', 6),
    ('Motivaatio', 'Itsenäisyys', 6),
    ('Itsenäinen työskentely', 'Itsenäisyys', 6),
])

# Itseohjautuvuus
g.add_weighted_edges_from([
    ('Itsenäinen työskentely', 'Itseohjautuvuus', 7),
    ('Johtaminen', 'Itseohjautuvuus', 7),
])

# Johtajuus
g.add_weighted_edges_from([
    ('Motivaatio', 'Johtajuus', 8),
    ('Mittaus ja monitorointi', 'Johtajuus', 8),
    ('Ihmissuhdetaidot', 'Johtajuus', 8),
    ('Johtaminen', 'Johtajuus', 8),
])

# Oppiminen
g.add_weighted_edges_from([
    ('Motivaatio', 'Oppiminen', 9),
    ('Yhteistyö', 'Oppiminen', 9),
    ('Mittaus ja monitorointi', 'Oppiminen', 9),
    ('Uuden oppiminen', 'Oppiminen', 9),
    ('Analyyttiset taidot', 'Oppiminen', 9),
    ('Kulttuurien tunteminen', 'Oppiminen', 9),
    ('Johtaminen', 'Oppiminen', 9),
    ('Avoimuus', 'Oppiminen', 9),
])

# Organisointitaidot
g.add_weighted_edges_from([
    ('Ongelmanratkaisukyky', 'Organisointitaidot', 10),
    ('Päätöksen tekeminen', 'Organisointitaidot', 10),
    ('Tietoisuus', 'Organisointitaidot', 10),
    ('Mittaus ja monitorointi', 'Organisointitaidot', 10),
    ('Johtaminen', 'Organisointitaidot', 10),
])

# Sosiaaliset taidot
g.add_weighted_edges_from([
    ('Keskinäinen kunnioitus', 'Sosiaaliset taidot', 11),
    ('Luottamus', 'Sosiaaliset taidot', 11),
    ('Haavoittuvuus', 'Sosiaaliset taidot', 11),
    ('Kommunikaatiotaidot', 'Sosiaaliset taidot', 11),
    ('Itseluottamus', 'Sosiaaliset taidot', 11),
    ('Rohkeus', 'Sosiaaliset taidot', 11),
    ('Yhteistyö', 'Sosiaaliset taidot', 11),
    ('Ihmissuhdetaidot', 'Sosiaaliset taidot', 11),
    ('Kulttuurien tunteminen', 'Sosiaaliset taidot', 11),
    ('Johtaminen', 'Sosiaaliset taidot', 11),
    ('Avoimuus', 'Sosiaaliset taidot', 11),
    ('Osallistuminen', 'Sosiaaliset taidot', 11),
])

# Tietoisuus
g.add_weighted_edges_from([
    ('Yhteisvastuu', 'Tietoisuus', 12),
    ('Ongelmanratkaisukyky', 'Tietoisuus', 12),
    ('Päätöksen tekeminen', 'Tietoisuus', 12),
    ('Tietoisuus', 'Tietoisuus', 12),
    ('Organisaation tunteminen', 'Tietoisuus', 12),
    ('Mittaus ja monitorointi', 'Tietoisuus', 12),
    ('Ihmissuhdetaidot', 'Tietoisuus', 12),
    ('Analyyttiset taidot', 'Tietoisuus', 12),
    ('Kulttuurien tunteminen', 'Tietoisuus', 12),
    ('Avoimuus', 'Tietoisuus', 12),
    ('Osallistuminen', 'Tietoisuus', 12),
])

# Vastuullisuus
g.add_weighted_edges_from([
    ('Haavoittuvuus', 'Vastuullisuus', 13),
    ('Yhteisvastuu', 'Vastuullisuus', 13),
    ('Vastuullisuus', 'Vastuullisuus', 13),
    ('Organisaation tunteminen', 'Vastuullisuus', 13),
    ('Motivaatio', 'Vastuullisuus', 13),
    ('Mittaus ja monitorointi', 'Vastuullisuus', 13),
    ('Johtaminen', 'Vastuullisuus', 13),
    ('Avoimuus', 'Vastuullisuus', 13),
    ('Osallistuminen', 'Vastuullisuus', 13),
])

# Yhteistyö
g.add_weighted_edges_from([
    ('Keskinäinen kunnioitus', 'Yhteistyö', 14),
    ('Luottamus', 'Yhteistyö', 14),
    ('Haavoittuvuus', 'Yhteistyö', 14),
    ('Kommunikaatiotaidot', 'Yhteistyö', 14),
    ('Yhteisvastuu', 'Yhteistyö', 14),
    ('Vastuullisuus', 'Yhteistyö', 14),
    ('Ihmissuhdetaidot', 'Yhteistyö', 14),
    ('Kulttuurien tunteminen', 'Yhteistyö', 14),
    ('Avoimuus', 'Yhteistyö', 14),
    ('Osallistuminen', 'Yhteistyö', 14),
])

# Get node colors by nodetype


def colorForNodetype(type):
    if (type == 'Yläluokka'):
        return '#CCEBC5'
    else:
        return '#B3CDE3'


nodetypes = [u[1] for u in g.nodes(data="nodetype")]
node_colors = list(map(colorForNodetype, nodetypes))

# Get pos
pos = nx.circular_layout(g, scale=3)

# Plot it
plt.figure(1, figsize=(12, 12))
nx.draw_networkx_nodes(g, pos=pos, node_color=node_colors, node_size=300)
nx.draw_networkx_edges(g, pos=pos, edge_cmap=plt.get_cmap('Pastel1'))
nx.draw_networkx_labels(g, pos=pos, font_size=10)
plt.show()
