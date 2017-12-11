subs(chat,felin).
subs(lion,felin).
subs(chien,canide).
subs(chat,mammifere).
subs(felin,mammifere).
subs(canide,mammifere).
subs(mammifere, animal).
subs(animal,vivant).
subs(canaris, animal).
subs(and(animal, plante), nothing).
subs(and(animal,some(aMaitre)) ,pet).
subs(and(pet, not(some(aMaitre))), nothing).
subs(lion, carnivoreExc).

subs(chihuahua, chien).
subs(chihuahua, pet).
subs(chien, canide).
subs(canide, chien).
inst(felix, chat).
inst(pierre, humain).
inst(princesse, chihuahua).
inst(marie, humain).
instR(felix, aMaitre, pierre).
instR(marie, aMaitre, marie).
subs(some(aMaitre), all(aMaitre, humain)).
all(aMaitre, humain).
equiv(carnivoreExc, all(mange, animal)).
equiv(herbivoreExc, all(mange, plante)).
equiv(toto,tata).
%carnivoreExc(lion).
subs(animal, and(some(mange), animal)).

%ajout de l'équivalence
subsS(_,_) :- equiv(_,_).
/*Pour eviter des boucles de dependances infinie
 le 3 eme terme correspond aux valeurs de subsomption deja rencontre
 il semblerai que le not en prolog soit \+*/
subsS(C,D) :- subsS(C,D,[C]).
subsS(C,C,_).
subsS(C,D,_) :- subs(C,D),C\==D.
subsS(C,D,L) :- subs(C,E), \+(member(E,L)), subsS(E,D,[E | L]), E\==D.
%and
subsS(C,and(D1,D2),L) :- D1 \= D2, subsS(C, D2,L).
%subsS(C, D, L) : \+subs(and(D1,D2),D), E=and(D1,D2), not(member(E,L)), subsS(C,E,[E|L]), E \==C.
%pourTous
subsS(all(R,C), all(R, D)) :- subsS(C,D).
       


 
