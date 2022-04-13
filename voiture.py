from vehicule import Vehicule


class Voiture(Vehicule):
    """
    Cette classe représente une voiture.
    C'est une classe conccrète qui étend (ou hérite de) la classe Véhicule.
    Cette classe est destinée à être instanciée.
    """

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, type_carrosserie: str):
        self._type_carrosserie = type_carrosserie
        super().__init__(marque, modele, carburant, vitesse)
        # il faut utiliser le setter s'il y a une procédure de vérification des données avant l'affectation
        self.set_vitesse(vitesse)


    def __str__(self):
        return super().__str__() + f"{self._type_carrosserie}"

    def get_type_carrosserie(self) -> str:
        return self._type_carrosserie
