concatene([],L,L).
concatene([T | L1], L2, [T | R]) :-concatene(L1, L2, R).

inverse([],[]).
inverse([A | L1], Y) :-  inverse(L1, L2), concatene(L2, [A], Y).

supprime([],X,[]).
supprime([X | L], X, Res) :- supprime(L, X, Res).
supprime([T | L], X, Res) :- T \= X, supprime(L, X, S), concatene([T], S, Res).

filtre([],L2,[]).
filtre(L1, [], L1).
filtre(L1, [X | L2], L3) :- supprime(L1, X, S), filtre(S, L2, L3).

palindrome(X) :- inverse(X,X).

dernier(X, L) :- concatene(L2, [X], L).
palindrome2([X]).
palindrome2([]).
palindrome2([X | L]) :- concatene(L2, [X], L), palindrome2(L2).
