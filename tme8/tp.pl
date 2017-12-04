motTrouRef([_,m,_,r,_]).

prefixe([X | L1], L2) :- append([X | L1],_,L2).

lin(Mot, [Mot | _]).
lin(Mot, [_ | R]) :- lin(Mot, R).

chercheDico(_,[],[]).
chercheDico(Mot, [ E | Dico], [E | Res]) :- prefixe(Mot, E), chercheDico(Mot, Dico, Res).
chercheDico(Mot, [ E | Dico], Res) :- not(prefixe(Mot, E)), chercheDico(Mot, Dico, Res).

valeurPossible(X,Pref,Dico,Alphabet,NewPref) :- member(X, Alphabet), append(Pref, [X], NewPref), chercheDico(NewPref, Dico, Res), Res \= [].
valeurPossible(_, _, [], _, []).

remplit(Mt, [ E | Dico], Alphabet) :- valeurPossible(X, Mt, Dico, Alphabet, NewPref), remplit(Mt, Dico, Alphabet).
