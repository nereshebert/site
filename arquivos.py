MHP = open('numeros.txt','w')


for linha in range(1,101):
    MHP.write('%d\n'%linha)


MHP.close()
