nome=input("Qual o seu nome? ")
f=len(nome)-1
i=0
k=[]
contrario=""
for n in range(0, f+1):
	k.append(nome[n])
while f>i:
	b=k[f]
	k[f]=k[i]
	k[i]=b
	i=i+1
	f=f-1
print("Seu nome ao contrário é: ")
n=0
while n<len(k):
	contrario="{}{}".format(contrario, k[n])
	n=n+1
contrario=contrario.lower()
contrario=contrario.title()
print(contrario)