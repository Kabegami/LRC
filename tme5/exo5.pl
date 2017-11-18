non(0,1).
non(1,0).

/* et */
et(1,1,1).
et(1,0,0).
et(0,0,0).
et(0,1,0).

/* ou */
ou(1,1,1).
ou(1,0,1).
ou(0,1,1).
ou(0,0,0).

/* xor */
xor(X,Y,1) :- ou(X,Y,1), et(X,Y,0).
xor(X,Y,0) :- ou(X,Y,0).
xor(X,Y,0) :- et(X,Y,1).
