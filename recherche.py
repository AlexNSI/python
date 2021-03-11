#### Part 1 ####

def recherche(tab,n):
  try:
    return len(tab)-tab[::-1].index(n)-1
  except ValueError:
    return "Introuvable, longueur du tableau : " + str(len(tab))


r1,r2,r3 = recherche([5,3],1), recherche([2,4],2), recherche([2,3,5,2,4],2)

print("Recherche 1 :" , r1 , "\nRecherche 2 : " , r2 , "\nRecherche 3 : " , r3)

#### Part 2 ####

def courteDistance(depart,points):
  print(a) # En cours
  ## départ = (0,2)
  ## points = ((0,4),(0,7),(1,7))
  ## On doit trouver la plus courte distance entrre depart et
  ## la liste de points
