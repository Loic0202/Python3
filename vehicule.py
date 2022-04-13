class Vehicule:
    """
    Cette classe représente un véhicule.
    Attention c'est une classe abstraite.
    Elle est destinée à être étendu par des classes enfants.
    """
    # les variable déclarées directement dans la classe sont "des variables de classe"
    # le underscore permet d'indiquer que la variable est privée
    # Attention car elle reste tout de même accessible depuis l'extérieur

    _acceleration = 20

    # # redéfinrir une variable de classe dans une classe s'appelle "surcharger une variable de classe"

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int):
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        # il faut utiliser le setter s'il y a une procédure de vérification des données avant l'affectation
        self.set_vitesse(vitesse)

    def __str__(self):
        return f"{self._marque} {self._modele} {self._carburant} {self._vitesse}"

    def get_marque(self) -> str:
        return self._marque

    def get_modele(self) -> str:
        return self._modele

    def get_carburant(self) -> str:
        return self._carburant

    # getter
    def get_vitesse(self) -> int:
        return self._vitesse

    # setter
    def set_vitesse(self, vitesse: int):
        if  type(vitesse) is not int:
            raise Exception("La Vitesse doit être unn int")
        elif vitesse > 220:
            raise Exception("La Vitesse max est 220")
        elif vitesse < -10:
            raise Exception("La Vitesse min est -10")

        self._vitesse = vitesse

    def accelerer(self):
        vitesse = self.get_vitesse()
        vitesse += self._acceleration
        self.set_vitesse(vitesse)

    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -= self._acceleration
        self.set_vitesse(vitesse)