from ex1 import *

class Graphe(object):
    def __init__(self, noeuds, relations):
        """ noeuds : set
            relations : dict """
        self.noeuds = noeuds
        self.n = len(noeuds)
        self.relations = relations

    def getRelations(self, i,j):
        k = (i,j)
        if k in self.relations:
            return self.relations[k]
        if (j,i) in self.relations:
            return transposeSet(self.relations[(j,i)])
        #quand on ne connait pas les relations tout est possible
        #return set()
        return GLOBAL_ALL_STATES

    def __str__(self):
        s = "GRAPHE \n"
        s += "========================================== \n"
        s += 'noeuds : {} \n'.format(self.noeuds)
        s +='------------------------------------------ \n'
        s +='relations : {} \n'.format(self.relations)
        s += "========================================= \n"
        return s

    def ajouter(self, n1,n2,R):
        #si le noeud existe deja ne fait rien
        self.noeuds.add(n1)
        self.noeuds.add(n2)
        # Rij = self.getRelations(n1,n2)
        # if type(R) == set:
        #     Rij.union(R)
        # else:
        #     Rij.add(R)
        if type(R) == set:
            self.relations[(n1,n2)] = R
        else:
            self.relations[(n1,n2)] = {R}

    def propa(self, n1,n2, c):
        if self.relations == "Le système est impossible !":
            return False
        pile = [(n1,n2)]
        cpt = 0
        
        if type(c) == set:
            self.relations[(n1,n2)] = c
        else:
            self.relations[(n1,n2)] = {c}
        while pile != []:
            i, j = pile.pop()
            Rij = self.getRelations(i,j)
            # print('Rij : ', Rij)
            self.ajouter(i,j,Rij)
            for k in self.noeuds:
                if k != n1 and k != n2:
                    Rik = self.getRelations(i,k)
                    Rjk = self.getRelations(j,k)
                    # print('R{}{} : {}'.format(i,j, Rij))
                    # print('bla R{}{} : {}'.format(j,k ,Rjk))
                    cc1 = compositionSet(Rij, Rjk)
                    # print('Rik :', Rik)
                    # print('cc1 :',cc1)
                    new_Rik = Rik.intersection(cc1)
                    #---------------------------
                    Rkj = self.getRelations(k,j)
                    # print('Rkj :', Rkj)
                    Rki = self.getRelations(k,i)
                    cc2 = compositionSet(Rki, Rij)
                    # print('cc2 :' ,cc2)
                    new_Rkj = Rkj.intersection(cc2)
                    # print('new_Rkj :' ,Rkj)
                    if new_Rik == set() or new_Rkj == set():
                        print('Contradiction temporelle')
                        self.relations = "Le système est impossible !"
                        return False
                    if new_Rik != Rik:
                        #print('new info')
                        if (k,i) in self.relations:
                            self.relations[(k,i)] = transposeSet(new_Rik)
                            pile.append((k,i))
                        else:
                            self.relations[(i,k)] = new_Rik.copy()
                            pile.append((i,k))
                    if new_Rkj != Rkj:
                        #print('new info')
                        if (j,k) in self.relations:
                            self.relations[(j,k)] = transposeSet(new_Rkj)
                            pile.append((j,k))
                        else:
                            self.relations[(k,j)] = new_Rkj.copy()
                            pile.append((k,j))
            print('cpt :', cpt)
            cpt += 1
            

def question4():
    #exemple 1
    G1 = Graphe(set(), dict())
    G1.ajouter('A','B','<')
    G1.ajouter('A','C','>')
    G1.propa('B','C','=')
    #contradiction temporelle mais c'est normal car on a A < B = C et A > C ce qui est impossible
    print('G1 :' ,G1)
    
    G2 = Graphe(set(), dict())
    G2.ajouter('A','B','<')
    G2.ajouter('A','C','<')
    G2.propa('B','C','=')
    #marche sans problème pas d'information suplémentaire ajouté
    print('G2 : ', G2) 

#if __name__ == "__main__":
def main():
    #question4()
    #Question 5
    G3 = Graphe({'S','L','R'}, dict())
    G3.propa('L','S',{'ot','mt'})
    #John n'est pas dans la piece quand j'appuis sur l'interupteur donc soit j'appuis avant soit apres
    G3.propa('S','R',{'<','m','mt', '>'})
    G3.propa('L','R',{'<','mt'})
    print('G3 : ', G3)
    #on obtient l'information que je touche l'interrupteur avant que John soit dans la piece

main()
