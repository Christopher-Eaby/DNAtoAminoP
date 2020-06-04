# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jun  4 09:13:05 2020
@author: Chris
"""
#function to read from file
def mutate():
    #reads from the main file and from the normal one
    File_normal = open("DNAFile.txt","r")
    File_normal_fixed = open("normalDNA.txt","w")
    #adds the main file to a string
    end = File_normal.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File_normal_fixed.writelines("A")
        else: 
            File_normal_fixed.writelines(end[x])
            
    #reads from the main file and from the normal one
    File_mutate = open("DNAFile.txt","r")
    File_mutate_fixed = open("mutatedDNA.txt","w")
    #adds the main file to a string
    end = File_mutate.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File_mutate_fixed.writelines("T")
        else: 
            File_mutate_fixed.writelines(end[x])
            
    #closes all the files
    File_normal.close()
    File_normal_fixed.close()
    File_mutate.close()
    File_mutate_fixed.close()

#reads everything from file and returns it
def readFromFile(file):
    File_object = open(file,"r")
    return File_object.read().replace("\n", "")

tfile = "DNAFile.txt"
#taking the DNA sequence from the .txt file and adding it to a string
DNAfirst = readFromFile(tfile)

#function to create a protein from the DNA sequence
def translate(DNA):
    #dictionary containing only the first 5 aminos as stated in the question
    aminoacids = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    
    aminosequence = "" 
    #runs through the DNA sequence taking strings of 3 in length
    for x in range(0, len(DNA), 3): 
        #finds the 3 length codon
        codon = DNA[x: x + 3] 
        #tests if the codon is in the table
        if codon in aminoacids:
            #adds the amino
            aminosequence += aminoacids[codon]
        else:
            #adds an X because it doesn't contain an amino
            aminosequence += "X"
    return aminosequence

def txtTranslate():
    #recall the mutate
    mutate()
    #adds the contents of the text files to the variables "mut" and "nor"
    mut = readFromFile("mutatedDNA.txt")
    nor = readFromFile("normalDNA.txt")
    #turns them into protein strings
    mutend = translate(mut)
    norend = translate(nor)
    #prints out the finished products
    print("-----------------------------------------------") 
    print("MutatedDNA output : " + "\n"+ mutend + "\n\n" + "NormalDNA output : "+ "\n" + norend)
    print("-----------------------------------------------")
    
#runs the translation
txtTranslate()

#the example given

print("\nThe example output given (ATTCTCATA) - " + translate(("ATTCTCATA")))
print("-----------------------------------------------") 