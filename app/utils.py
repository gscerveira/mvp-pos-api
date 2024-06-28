from rdflib import Graph, Namespace
from rdflib.namespace import DCAT, DCTERMS as DCT

# Dicionário com os valores de score para cada campo de metadata
CRITERIO_SCORE = {
    DCAT.keyword: 30,
    DCAT.theme: 30,
    DCT.spatial: 20,
    DCT.temporal: 20,
    DCAT.accessURL: 50,
    DCAT.downloadURL: 20,
    DCT.format: 20,
    DCAT.mediaType: 10,
    DCT.license: 20,
    DCT.accessRights: 10,
    DCAT.contactPoint: 20,
    DCT.publisher: 10,
    DCT.rights: 5,
    DCAT.byteSize: 5,
    DCT.issued: 5,
    DCT.modified: 5
}

# Função para calcular o score de um dataset a partir de um arquivo RDF/XML
def calcular_score_mqa(arquivo_xml):
    # Ler o arquivo e armazenar em um grafo RDF
    g = Graph()
    g.parse(arquivo_xml)

    score = 0

    # Adicionar valor do campo ao score, se o campo estiver no grafo
    for field, value in CRITERIO_SCORE.items():
        if (None, field, None) in g:
            score += value

    return score




