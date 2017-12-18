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
        return set(d.transpose.keys())

    def propagation(self, n1, n2, c):
        R = (n1, n2)
        pile = [R]
        print('c : ', c)
        S = self.relations.get(R,set())
        S.add(c)
        self.relations[R] = S
        print('self.relations : ', self.relations)
        while pile != []:
            Rij = pile.pop()
            i,j = Rij
            Rij_elems = self.getRelations(i,j)
            print('i :',i)
            print('j :',j)
            for k in self.noeuds:
                if k != i and k != j:
                    Rik_elems = self.getRelations(i,k)
                    Rki_elems = self.getRelations(k,i)
                    Rkj_elems = self.getRelations(k,j)
                    Rjk_elems = self.getRelations(j,k)
                    new_Rik = Rik_elems.intersection(compositionSet(Rij_elems, Rjk_elems))
                    new_Rkj = Rkj_elems.intersection(compositionSet(Rki_elems, Rij_elems))
                    if new_Rik == set() or new_Rkj == set():
                        print('Contradiction temporelle !')
                        return False
                    if new_Rik != Rik_elems:
                        self.relations[(i,k)] = new_Rik
                        pile.append((i,k))
                    if new_Rkj != Rkj_elems:
                        self.relations[(k,j)] = new_Rkj
                        pile.append((k,j))

if __name__ == "__main__":
    noeuds = {'A','B','C'}
    R = {('A','B') : set('<'), ('A','C') : set('>')}
    G = Graphe(noeuds, R)
    G.propagation('B','C','=')
    print('relations : ', G.relations)
                
            
