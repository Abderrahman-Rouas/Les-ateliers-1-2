myset1={3,4,7,2,6,22,1,25,90,55,66}       #declaration de deux sets
myset2={3,6,2,7,7,4,6,6,22,22,3}
myset3=myset1.intersection(myset2)        #fair une intersection des deux sets dans une troisieme
print("myset3=",myset3)                             #afficher myset3

myset1=myset1.difference(myset3)          #supprimer les element commune dans la set 1
print("myset1=",myset1)                   #afficher list 1 sans les elements
