:- dynamic clue/3.
:- dynamic unexplored/1.
:- dynamic mine/1.
:- dynamic mine/2.
:- dynamic discovered/3.
mine((X,Y)) :- mine(X,Y).
neighbors(X,Y,Neighbors) :-
    findall(
        (NX,NY),
        (
            between(-1,1,DX),
            between(-1,1,DY),
            \+ (DX = 0, DY = 0),
            NX is X+DX,
            NY is Y+DY,
            NX >=0 , NX=<8,
            NY >=0 , NY=<8
        ),
        Neighbors
    ).
unexplored((X,Y)) :-
    \+ clue(X,Y,_),
    \+ mine(X,Y).

count_mines(X,Y,C) :-
    neighbors(X,Y,N),
    include(mine,N,Mines),
    length(Mines,C).

find_mines :- 
    clue(X,Y,Clue),
    neighbors(X,Y, Neighbors),
    include(unexplored,Neighbors,UnexploredNeighbors),
    count_mines(X,Y,Mn),
    length(UnexploredNeighbors,Unx),
    Clue-Mn =:= Unx,
    assert_mines(UnexploredNeighbors,X,Y),
    fail.
assert_mines([],_,_).
assert_mines([(X,Y)|T],XS,YS) :-
    assertz(mine(X,Y)),
    assertz(discovered((X,Y),XS,YS)),
    assert_mines(T,XS,YS).
member((X,Y),[]):-fail.
member((X,Y),[(X,Y)|_]):-!.
member((X,Y),[_|T]):- member((X,Y),T).

action(X,Y) :-
    clue(CX,CY,Clue),
    neighbors(CX,CY,N),
    count_mines(CX,CY,MC),
    MC=:=Clue,
    include(unexplored,N,UnexploredNeighbors),
    member((X,Y),UnexploredNeighbors).