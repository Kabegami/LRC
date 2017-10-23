pere(pierre, aristide).
pere(marius, pierre).
mere(adelaide, pierre).
mere(felicie, aristide).
parent(X,Y) :- pere(X,Y).
parent(X,Y) :- mere(X,Y).
