print("Wassim SAIDANE et Aurélien Authier")


F = "1|-2&3|4&-2|-3&4|-5&2|-5"
G = "0|2&0|-3&1|-3&1|-4&2|-4&0|-5&1|-5&2|-5&3|6&4|6&5|6"
dic = {}
dic[1] = True
dic[2] = False
dic[3] = True
dic[4] = None
dic[5] = False
dic[6] = False
dic[-1] = not(dic[1])
dic[-2] = not(dic[2])
dic[-3] = not(dic[3])
dic[-4] = not(dic[4])
dic[-5] = not(dic[5])
dic[-6] = not(dic[6])


def clauses_liste(F):
    return F.split("&")


def variables_par_clause(l1, l2):
    for i in range(len(l2)):
        l1.append(l2[i].split("|"))


def eval_clauses(d1, d2, l):
    for i in range(len(l)):
        v1 = int(l[i][0])
        v2 = int(l[i][1])
        d2[tuple(l[i])] = (d1[v1] or d1[v2])


def eval_2_sat(f, d1):
    #---------------------------------------------------------------------------------------------------------
    #| Le code ne prend pas en comple les formules qui ne sont pas rentrées en suivant notre sémentique"    #|
    #| Pas d'espace !                                                                                       #|
    #| Les clauses sont séparées par "&" (et)                                                               #|
    #| Les parenthés sont sous-entendu caractères avant le "&"                                              #|
    #| Les variables sont séparées par "|" (ou)                                                             #|
    #| Les formules 2-sat fonctionnent                                                                      #|
    #---------------------------------------------------------------------------------------------------------
    print(f"Affectation : {dic}")
    clauses = clauses_liste(f)
    print(f"Clauses : {clauses}")
    result = True
    clause = []
    variables_par_clause(clause, clauses)
    print(f"Variables par clause : {clause}")
    d2 = {}
    eval_clauses(d1, d2, clause)
    print(f"Evaluations par clause : {d2}")
    for value in d2:
        result = (result and d2[value])
    return result


def formula_2_graph(F):
    clauses = clauses_liste(F)
    print(f"Clauses : {clauses}")
    clause = []
    variables_par_clause(clause, clauses)
    print(f"Variables par clause : {clause}")
    g = DiGraph()
    for var in clause:
        g.add_vertices([int(var[0]), int(var[1])])
    sommets = g.vertices()
    for sommet in sommets:
        g.add_vertices([sommet*-1])
    sommets = g.vertices()
    print(f"Listes des sommets : {sommets}")
    for i in range(0, len(clause)):
        clause[i] = [int(clause[i][0]), int(clause[i][1])]
    for var in clause:
        g.add_edges([(var[0]*-1, var[1])])
        g.add_edges([(var[1]*-1, var[0])])
    return g


print("Exercice 3 : ")
print(" ")
print(f"F={F}")
if eval_2_sat(F, dic):
    print("F est satisfaisable")
else:
    print("F n'est pas satisfaisable")
print(" ")
print(" ")
print("Exercice 4 : ")
print(f"F={F}")
g = formula_2_graph(F)
g.show()
