def fib(n):                  #declaration de la fonction
  if n==0 or n==1:            #conditions d'arret pour la fonction récusrive

    return 1
  else :
    return fib(n-1)+fib(n-2)      #le return

a=int(input("entrer un nombre"))   # demnede de saisir le nombre
for i in range(0,a):                # la boucle de 0 jusqua le nombre
       print(fib(i))                 #l'appel de de fonction avec l'affichage
