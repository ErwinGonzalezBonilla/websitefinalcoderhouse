hobies = input('Ingresa tus 3 hobies favoritos separados por un espacio: ')
archivo_abierto = open('miHobbieFavorito.txt','w')
archivo_abierto.write(hobies)
archivo_abierto.close()
