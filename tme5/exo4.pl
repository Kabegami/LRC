/* Base de données : Les Rougon-Macquart*/
pere(rougon, pierre).
pere(macquart, antoine).
pere(macquart, ursule).
pere(pierre, aristide).
pere(pierre, eugene).
pere(pierre, pascal).
pere(pierre, sidonie).
pere(aristide, maxime).
pere(aristide, clothilde).
pere(aristide, victor).
pere(antoine, gervaise).
pere(antoine, lisa).
pere(antoine, jean).
pere(mouret, francois).
pere(mouret, helene).
pere(mouret, silvere).
mere(adelaide, pierre).
mere(adelaide, antoine).
mere(adelaide, ursule).
mere(felicie, aristide).
mere(felicie, pascal).
mere(felicie, eugene).
mere(felicie, sidonie).
mere(ursule, francois).
mere(ursule, helene).
mere(ursule, silvere).
/* Relations */
parent(X,Y) :- pere(X,Y).
parent(X,Y) :- mere(X,Y).
parents(X,Y,Z) :- pere(X,Z), mere(Y, Z).
grandPere(X,Y) :- pere(X,Z), pere(Z,Y).
grandPere(X,Y) :- pere(X,Z), mere(Z,Y).
frereOuSoeur(X,Y) :- pere(Z,X), pere(Z,Y), mere(W,X), mere(W, Y).
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- parent(Z, Y), ancetre(X, Z).
                
