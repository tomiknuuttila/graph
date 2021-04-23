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

# Get node colors by class


def colorForNodetype(type):
    if (type == 'Yläluokka'):
        return '#CCEBC5'
    else:
        return '#B3CDE3'


nodetypes = [u[1] for u in g.nodes(data="nodetype")]
node_colors = list(map(colorForNodetype, nodetypes))

# Get colors for edges
edge_colors = range(g.number_of_edges())

# Get pos
pos = nx.circular_layout(g,scale=3)

# Plot it
plt.figure(1,figsize=(12,12))
nx.draw_networkx_nodes(g, pos=pos,node_color=node_colors, node_size=300)
nx.draw_networkx_edges(g, pos=pos,edge_color=edge_colors, edge_cmap=plt.get_cmap('Pastel1'))
nx.draw_networkx_labels(g, pos=pos, font_size=10)
plt.show()
