#!/usr/bin/python3
print("\n ----0---- Class 03 -------0---- \n")


acess = []
x=0
while x <= 3:
	name= str(input("Whats your name? Write please! "))
	print("\n Welcome to Class Python \
		FUndamentals Mr.(s) %s.\n" %name)
	acess.append(name)
	x+=1

print(sorted(acess))




print("\n Now write how old are you?")
old= int(input(" :"))

print("\n Very cool! You are %d old!" %old)

print("\n----- Using separator sep ----")

n= 'Dip'
sobrenome = 'cX2'
print(n,sobrenome, sep=".")

print("\n----- Using round for rounding ----")
nota=[]
y=0
while y<=2:
	valor= float(input("ENter the value of your note: "))
	nota.append(valor)
	y+=1
soma= 0
for v in nota:
	soma += v

#print(round(nota,2))
print("\nA soma arredondada: %.2f" % (round(soma,3)))
print("Media eh: %.2f" % (soma / len(nota)))

print("\n ------- File Manipulation -------- \n")
with  open ('douglas.txt','r+') as f:
	f.write('pYthon is Cool, TEST MASTER')

'''print("\n ------- File Manipulation Add Lines-------- \n")
with  open ('douglas.txt','a') as f:
	f.write('\nAdd the line TOPPPEnnnnn')
'''

print("\n ------- File Manipulation Add Lines-------- \n")
with  open ('douglas.txt','a') as f:
	texto= str(input('\nDigite o texto para o arquivo: '))
	f.write(texto)

print("\n ------- File Manipulation View-------- \n")
with  open ('douglas.txt','r') as f:
	print(f.read())

print("\n ------- File Manipulation Read Lines-------- \n")
with  open ('douglas.txt','r') as f:
	print(f.readlines()[1])
	print(f.readlines())

print("\n ------- File Manipulation Seek / WRITE -------- \n")
with  open ('douglas.txt','r+') as f:
	f.seek(2)
	f.write('2')

''' outra forma que pode dar mais bugs e problemas
f = open('douglas.txt','+')
f.close()'''
