# -*- coding: UTF-8 -*-
#!/usr/bin/env python

## Author: Mateo Restrepo

import sys, codecs
from collections import Counter
from numpy import ceil
from math import log

#Argument check for the program
if len(sys.argv)<4:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)


#Open the file
fo = codecs.open(sys.argv[1], "r")

#Save the input file name
fName = '{}'.format(sys.argv[1])
fName1 = fName[0:fName.find('.')]


#Save the input file in a string
fileOriginal = fo.read()
fo.close()


alphabetList=[]
#Define Alphabet, Frequencies...
alphabet = Counter(fileOriginal)
alphabetList = [(v, k) for k, v in alphabet.items()]
alphabetFreq = sorted(alphabetList,reverse=True)
alphabetFreqBack = sorted(alphabetList)
LogSizeAlphabet  = ceil(log(float(len(alphabetList)),2))
alphabetLetters = [x[1] for x in alphabetFreq]


#//-------------------------------------Plain Coder/Decoder-----------------------------------------------// 



#Plain Binary Coder
def plainCoder(inputfile):
    fileEncodedPlain = ''.join(format(ord(c), '07b') for c in inputfile) 
    #Se asume una codificación no ASCII de 7 bits por caracter, en caso de necesitar ASCII modificar el '07b' por '08b' 
    fPlainOut = open(fName1 + "_comp_plano.txt","w")
    fPlainOut.write(fileEncodedPlain)
    print '\nIm done coding!\n'
    
#Binary code Printing and saving
def plainCodeAlphabet(fileOriginal):
    #plainCode = [ bin(ord(ch))[2:].zfill(8) for ch in fileOriginal ] esta línea es para codificacion ASCII de 8bits por caracter.
    plainCode = [ format(ord(c), '07b') for c in fileOriginal ]#Codificación no ASCII de 7 bits por caracter, en caso de necesitar ASCII modificar el '07b' por '08b'
    fPlainOut1 = open("codigo_plano_" + fName1 + ".txt" ,"w")
    for ch in alphabetLetters:
        if ch == ' ': fPlainOut1.write ('Espacio en blanco' + " " + plainCode[fileOriginal.index(ch)] + '\n')
        elif ch == '\n': fPlainOut1.write ('Salto de linea'  + " " +  plainCode[fileOriginal.index(ch)] + '\n')
        else: fPlainOut1.write (ch + " " + plainCode[fileOriginal.index(ch)] + '\n')
            
    print '\nIm done writing files!\n'        
        
#Plain Binary Decoder
def plainDecoder(fileOriginal):
    fileDecodedPlain=''.join(chr(int(fileOriginal[i:i+7], 2)) for i in xrange(0, len(fileOriginal), 7))
    fPlainOut = open(fName1 + "_decomp_plano.txt","w")
    fPlainOut.write(fileDecodedPlain)
    print '\nIm done decoding! \n'
    print '\nIm done writing files!\n'


    
#//-------------------------------------Huffman Coder/Decoder-----------------------------------------------//   



#Build the Huffman tree
def buildTree(alphTuples) :
    while len(alphTuples) > 1 :
        leastTwo = tuple(alphTuples[0:2])                  
        theRest  = alphTuples[2:]                       
        combFreq = leastTwo[0][0] + leastTwo[1][0]     
        alphTuples   = theRest + [(combFreq,leastTwo)]     
        alphTuples.sort()                                 
    return alphTuples[0]

#Roaming the Huffman tree
def climbTree (tree) :
    p = tree[1]                                    
    if type(p) == type("") : return p              
    else : return (climbTree(p[0]), climbTree(p[1]))
    
#Code Assignation
codes   = {}
def assignCode (node, count='') :
    global codes
    if type(node) == type("") :
        codes[node] = count                
    else  :
        assignCode(node[0], count+"0")
        assignCode(node[1], count+"1")    
#Huffman coder function
def huffmanEncode (text) :
    global codes
    fileEncodedHuf = ""
    for ch in text : fileEncodedHuf += codes[ch]
    fHuffmanOut = open(fName1 + "_comp_huffman.txt","w")
    fHuffmanOut.write(fileEncodedHuf)
    print '\nIm done coding!\n'
#Huffman decoding function (May have a Bug Thread lightly)
def huffmanDecode (dictionary, text) :
    output=""
    i=0 #Infinite loop handler, ugly but works
    #Decoder (Can fail or loop forever if the codes do not match the message.)
    while len(text)>1 and i<pow(10, 8):
        for key in dictionary:                    
            if text.startswith(key):
                output += dictionary[key]
                text = text[len(key):]
            i+=1
        #If the while take more than 10 million steps it breaks the loop to avoid infinite looping (UGLY AS HELL but
        #I could not figure a better way)
        if i>pow(10, 7):
            print '\nNo es posible la Decodificación, revise los archivos de entrada!\n'
            break
    if output != "":
        fHufOut = open(fName1 + "_decomp_huffman.txt","w")
        fHufOut.write(output)
        print '\nIm done decoding! \n'
        print '\nIm done writing files!\n'
        
    
#//-------------------------------------Main-----------------------------------------------//



def main () :


##------------------PLAIN CODING------------------##


    if sys.argv[2]=='coder' and sys.argv[3]=='plain':
        plainCoder(fileOriginal)
        plainCodeAlphabet(fileOriginal)
    
    if sys.argv[2]=='decoder' and sys.argv[3]=='plain': plainDecoder(fileOriginal)
    
##------------------HUFFMAN CODING------------------##


    tree = buildTree(alphabetFreqBack)
    treeAux = climbTree(tree)
    assignCode(treeAux)   
     
    if sys.argv[2]=='coder' and sys.argv[3]=='huffman':
        
        huffmanCode = [(v, k) for k, v in codes.items()]
        huffmanCode.sort(key=lambda t: len(t[0]))
        
        huffmanEncode(fileOriginal)
        
        fHuffmanOut1 = open("codigo_huffman_" + fName1 + ".txt" ,"w")
        for item in huffmanCode:
            if item[1] == ' ': fHuffmanOut1.write('Espacio en blanco' + ": " +  item[0]  + '\n')
            elif item[1] == '\n': fHuffmanOut1.write('Salto de linea'  + ": " + item[0]  + '\n')
            else: fHuffmanOut1.write(item[1] + ": " + item[0] + '\n')
        
        print '\nIm done writing files!\n'
        
    if sys.argv[2]=='decoder' and sys.argv[3]=='huffman':
        if len(sys.argv)<5: 
            print('\nSe necesita un archivo con el codigo para continuar!\n')
            sys.exit(0)
        else: 
            f = codecs.open(sys.argv[4], "r")
            hufCode = f.read()
            f.close()
            aux = hufCode.splitlines()
            hufDictionary = []
            for thing in aux:
                if 'Espacio en blanco' in thing:
                    blanc = thing.split(': ')
                    blanc = [w.replace('Espacio en blanco', ' ') for w in blanc]
                    hufDictionary.append(blanc)
                elif 'Salto de linea' in thing:
                    jump = thing.split(': ')
                    jump = [w.replace('Salto de linea', '\n') for w in jump]
                    hufDictionary.append(jump)
                else: 
                    hufDictionary.append(thing.split(': '))
            
            hufDecodeDict = {t[1]:t[0] for t in hufDictionary}
            huffmanDecode(hufDecodeDict, fileOriginal)
               
if __name__ == "__main__": main()