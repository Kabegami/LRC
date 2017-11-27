subs(chat,félin).
subs(lion,félin).
subs(chien,canidé).
subs(chat,mammifère).
subs(félin,mammifère).
subs(canidé,mammifère).
subs(mammifère, animal).
subs(animal,vivant).
subs(canaris, animal).
subs(and(animal, plante), nothing).
subs(and(animal,some(aMaitre)) ,pet).
subs(and(pet, -some(aMaitre )), nothing).
subs(chihuahua, chien).
subs(chihuahua, pet).
subs(chien, canidé).
subs(canidé, chien).

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
carnivoreExc(lion).
subs(animal, and(some(mange), animal)).

subsS(C,D) :- equiv(C,D).
subsS(C,D) :- equiv(D,C).
subsS(C,D) :- subsS(C,D,[C]).
subsS(C,D,_).
subsS(C,D,_) :- subs(C,D),C\==D.
subsS(C,D,L) :- subs(C,E), not(member(E,L)), subsS(E,D,[E | L]), E\==D.
                                 
       


 
