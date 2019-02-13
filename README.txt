Este programa tiene dos modalidades (plain y huffman) y ejecuta dos operaciones (coder, decoder).

Para ejecutar el script necesita pasarle como parametros desde la consola lo siguiente:



------------------------- EN MODO CODER -------------------------

a) /////////////// plain ///////////////


1. Archivo .txt a codificar
2. coder (para quen se ejecute el codificador)
3. plain (para quen se ejecute en modalidad binaria plana)

Ejemplo (asumiendo que está en el directorio donde esta el compresor):

	 python compresor.py bin.txt coder plain

Así se ejecutará el compresor en modo plano comprimiendo bin.txt


b) /////////////// huffman ///////////////

1. Archivo .txt a codificar
2. coder (para quen se ejecute el codificador)
3. huffman (para quen se ejecute en modalidad huffman)

Ejemplo (asumiendo que está en el directorio donde esta el compresor):

	 python compresor.py bin.txt coder huffman

Así se ejecutará el compresor en modo huffman comprimiendo bin.txt




------------------------- EN MODO DECODER -------------------------

a) /////////////// plain ///////////////


1. Archivo .txt a decodificar
2. decoder (para quen se ejecute el decodificador)
3. plain (para quen se ejecute en modalidad binaria plana)

Ejemplo (asumiendo que está en el directorio donde esta el compresor):

	 python compresor.py fim.txt decoder plain

Así se ejecutará el compresor en modo plano descomprimiendo fim.txt


b) /////////////// huffman ///////////////

1. Archivo .txt a decodificar
2. decoder (para quen se ejecute el codificador)
3. huffman (para quen se ejecute en modalidad huffman)
4.(¡¡MUY IMPORTANTE!!) Archivo .txt que fue generado al usar la funcion 'coder huffman' que contiene el diccionario de "código huffman" a ASCII

Ejemplo (asumiendo que está en el directorio donde esta el compresor):

	 python compresor.py fim.txt coder huffman codigo_huffman_fim.txt

Así se ejecutará el compresor en modo huffman descomprimiendo fim.txt usando el diccionario en codigo_huffman_fim.txt

