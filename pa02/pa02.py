

'''
Assignment: pa02 - Encrypting a plaintext file using the Hill cipher
Author: Joshu Gurman
Language: python
To Compile: n/a
To Execute: python3 pa02.py kX.txt pX.txt
where kX.txt is the keytext file
and pX.txt is plaintext file
Note:
All input files are simple 8 bit ASCII input
All execute commands above have been tested on Eustis

Class: CIS3360 - Security in Computing - Summer 2025
Instructor: McAlpin
Due Date: 07/06/27
'''
import sys




fileName = input()
key = open(fileName, "r").read()

fileName = input()
file = open(fileName, "r").read()

numSquare = int(key[0])


matrix=[]
m=[]
key = key[2:]
print("\nKey matrix:")

num = ''
counter=0
for i in key:
    if i != '\n' and i != '\t':
        num+=i
    else:   
        m.append(int(num))
        print("%4d" % int(num), end='')
        num=''
        counter+=1
    if counter == numSquare:
        matrix.append(m)
        m=[]
        print("\n", end='')
        counter = 0

plaintext = ''
for char in file:
    if char.isalpha():  
        plaintext+=char

plaintext = plaintext.lower()

while len(plaintext) % numSquare != 0:
    plaintext+='x'

print("\nPlaintext:", end='')
print("\n", end='')
print(plaintext, end='')


cipherText = ''

for counter in range(len(plaintext)//numSquare):
    for i in range(numSquare):
        val = 0
        for j in range(numSquare):
            val += matrix[i][j]*(ord(plaintext[counter*numSquare+j])-97)
        cipherText+=chr(val%26+97)

print("\n", end='')
print("\n", end='')
print("Ciphertext:\n", end='')
print(cipherText)



'''
I [Joshua Gurman] ([jo870281]) affirm that this program is
entirely my own work and that I have neither developed my code together with
any another person, nor copied any code from any other person, nor permitted
my code to be copied or otherwise used by any other person, nor have I
copied, modified, or otherwise used programs created by others. I acknowledge
that any violation of the above terms will be treated as academic dishonesty.
'''
