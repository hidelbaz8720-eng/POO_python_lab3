# Classe mère : Document
class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")


# Classe fille : Livre
class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre : {self.titre} par {self.auteur} ({self.annee})")


# Classe fille : Magazine
class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine : {self.titre} No. {self.numero} ({self.annee})")


# Programme principal
if __name__ == "__main__":

    # Création d'une liste de documents
    documents = [
        Livre("1984", 1949, "George Orwell"),
        Magazine("Science & Vie", 2023, 456),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
    ]

    # Affichage de tous les documents
    for document in documents:
        document.afficher()