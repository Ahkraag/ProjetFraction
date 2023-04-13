from random import *

# Cahier des charges :
# * créer des objets fractions possédant deux attributs : un numérateur et un dénominateur de type entier.
# * modifier ces objets (accesseurs en lecture et en écriture, en respectant les obligations mathématiques)
# * afficher ces objets avec print
# * simplifier ces fractions...
# * ajouter, soustraire, multiplier et diviser deux fractions
# * décider si deux fractions sont égales
# * décider si l'une est plus grande que l'autre
# * et plus, si affinités !

def gcd(a, b):  # Le pgcd de a et b est égal au pgcd du reste et de b
    """Fonction récursive pour trouver le Pgcd de deux nombres"""
    r = a % b
    if r == 0:
        return int(b)
    else:
        return gcd(b, r)


class Fractions:
    """Cette class créer des fractions et permet de réaliser plusieurs opérations sur ces fractions"""

    ################################--Magic Method--################################

    def __init__(self, n, den):
        """Constructeur de la class Fractions"""
        self.setNum(n)
        self.setDen(den)
        self.pgcd(n, den)

    def __lt__(self, other):
        """Methode permettant de verifier l'infériorité ou la supériorité de deux objets de la class Fractions"""
        return self.getNum() / self.getDen() < other.getNum() / other.getDen()

    def __eq__(self, other):
        """Méthode permettant de vérifier l'égalité entre deux objets de la class Fractions"""
        return self.getDen() == other.getDen() and self.getNum() == other.getNum()

    def __mul__(self, other):
        """Méthode permettant de multiplier deux objets de la class Fractions"""
        return Fractions(self.getNum() * other.getNum(), self.getDen() * other.getDen())

    def __add__(self, other):
        """Méthode permettant d'additionner deux objets de la class Fractions"""
        return Fractions(self.getNum() * other.getDen() + other.getNum() * self.getDen(),
                         self.getDen() * other.getDen())

    def __sub__(self, other):
        """Méthode permettant de soustraire deux objets de la class Fractions"""
        return Fractions(self.getNum() * other.getDen() - other.getNum() * self.getDen(),
                         self.getDen() * other.getDen())

    def __truediv__(self, other):
        """Méthode permettant de diviser deux objets de la class Fractions"""
        if other.getNum() == 0:
            raise ZeroDivisionError("Il ne peut pas y avoir un dénominateur égal a zero")
        return Fractions(self.getNum() * other.getDen(), self.getDen() * other.getNum())

    def __str__(self):
        """Méthode permettant d'afficher l'objet de la class Fractions"""
        if self.denominateur == 1:
            return "{}".format(self.numerateur)
        return "{}/{}".format(self.numerateur, self.denominateur)

    #################################--Accesseurs--#################################

    def setNum(self, n):
        """Accesseur en écriture du numérateur de la class Fractions"""
        assert type(n) == int, "Votre numérateur n'est pas un nombre entier"
        self.numerateur = n

    def getNum(self):
        """Accesseur en écriture du numérateur de la class Fractions"""
        return self.numerateur

    def setDen(self, n):
        """Accesseur en écriture du dénominateur de la class Fractions"""
        assert type(n) == int, "Votre dénominateur n'est pas un entier"
        if n == 0:
            raise ZeroDivisionError("Il ne peut pas y avoir un dénominateur égal a zero")
        self.denominateur = n

    def getDen(self):
        """Accesseur en écriture du dénominateur de la class Fractions"""
        return self.denominateur

    def pgcd(self, n, den):
        """Méthode pour réaliser le Pgcd du numérateur et du dénominateur afin de simplifier les fractions"""
        m = gcd(n, den)
        self.setNum(int(self.numerateur / m))
        self.setDen(int(self.denominateur / m))


# Test des opérateurs avec des fractions prédéfinies

p = Fractions(5, 2)
j = Fractions(3, -2)
print(p * j)
print(p + j)
print(p - j)
print(p / j)
print(p == j)
print(p < j)
print(p > j)
print(help(Fractions)) # Test de l'affichage des documentations des fonctions

# Tests pointus avec nombres aléatoires

a = randint(0,150)
b = randint(0,150)
c = randint(0,150)
d = randint(0,150)
print(f"\nLa première fraction est {a}/{b} et la deuxième {c}/{d} : ")
p = Fractions(a,b)
j = Fractions(c,d)
print(f"En simplifiant on a {p} et {j}")
print(p * j)
print(p + j)
print(p - j)
print(p / j)
print(p == j)
print(p < j)
print(p > j)



# ██████  ██    ██ ██████  ██    ██ ██ ███████     ████████  ██████  ███    ███     ████████  ██████
# ██   ██ ██    ██ ██   ██ ██    ██ ██ ██             ██    ██    ██ ████  ████        ██    ██
# ██   ██ ██    ██ ██████  ██    ██ ██ ███████        ██    ██    ██ ██ ████ ██        ██    ███████
# ██   ██ ██    ██ ██      ██    ██ ██      ██        ██    ██    ██ ██  ██  ██        ██    ██    ██
# ██████   ██████  ██       ██████  ██ ███████        ██     ██████  ██      ██        ██     ██████
