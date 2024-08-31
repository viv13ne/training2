# ---DOCUMENTATION--------------------------------------------------------------
#-------------------------------------------------------------------------------
# Diam's - Jeune Demoiselle
# j'tai pas trouvé sur la planète, j'te trouverais peut-être sur internet
#--------------------------------------------------------------------------------
# > Somme d'un ensemble de termes élevés à des puissances croissantes : 
#   2¹+2²+2³+...+2 puissance n
#--------------------------------------------------------------------------------
# n = puissance maximum 
#--------------------------------------------------------------------------------
# hviviane@gmail.com !)
#--------------------------------------------------------------------------------
# Merci
#--------------------------------------------------------------------------------

n=int(input("puissance maximum ?"))
i=1
somme=2**i
bilan=str(somme)+"|"

while i<n:
    bilan +=str(somme)+"|"
    i=i+1
    somme=somme+2**i
    
print(bilan,"\n", "Somme = ", somme)
