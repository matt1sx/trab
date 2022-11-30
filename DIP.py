from enum import Enum

class Equipes(Enum):
    Natacao_Equipe = 1
    Basquete_Equipe = 2
    Futebol_Equipe = 3

class Estudantes():
    def __init__(self, nome):
        self.nome = nome

class IntegrantesEquipes():
    def __init__(self):
        self.integrantes_equipes = []

    def adicionar_integrantes_equipe(self, estudantes, equipes):
        self.integrantes_equipes.append ((estudantes, equipes))

class InspecionarIntegrantes():
    def __init__(self, estudantes_equipes_integrantes):
        integrantes = estudantes_equipes_integrantes.integrantes_equipes

        for integrantes in IntegrantesEquipes:
            if integrantes[1] == Equipes.Natacao_Equipe:
                print (f'{integrantes[0].nome} está no time de Natação')
            elif integrantes[1] == Equipes.Basquete_Equipe:
                print (f'{integrantes[0].nome} está no time de Basquete')
            elif integrantes[1] == Equipes.Futebol_Equipe:
                print (f'{integrantes[0].nome} está no time de Futebol')

Estudante_1 = Estudantes ('Fabricio')
Estudante_2 = Estudantes ('Thamires')    
Estudante_3 = Estudantes ('Matheus')

Integrantes_Equipes = IntegrantesEquipes()

Integrantes_Equipes.adicionar_integrantes_equipe(Estudante_1, Equipes.Natacao_Equipe)
Integrantes_Equipes.adicionar_integrantes_equipe(Estudante_2, Equipes.Basquete_Equipe)
Integrantes_Equipes.adicionar_integrantes_equipe(Estudante_3, Equipes.Futebol_Equipe)
        
InspecionarIntegrantes (Integrantes_Equipes)