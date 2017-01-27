#! /usr/bin/python

'''with open("/home/lmi-03/Documentos/Lucas/APA/example.in", "r") as f:
    read_data = f.readlines()
f.closed '''
#listateste = ['3','5','0','2','1']
import sys

y = sys.argv[1]
#print y

x=[]
while(True):
	try:
		x.append(input())
	except:
		break

	#read_data = [int(x.strip()) for x in read_data] 
	##############################################################################################
if y == '1':
	def selection_sort (lista):
		for i in range(0,len(lista)):
			menor=i
			for k in range(i,len(lista)):
				if lista[k]<lista[menor]:
					menor=k
			lista[menor],lista[i]=lista[i],lista[menor]

	selection_sort(x)
	#print 'selection_sort'

	##############################################################################################

elif y == '2':

	def insertion_sort(lista):
		for i in range(1,len(lista)):
			#print 'i = '+str(i)
			key = lista[i]
			k = i
			while k > 0 and key < lista[k - 1]:
				lista[k] = lista[k - 1]
				k -= 1
			lista[k] = key

	insertion_sort(x)
	#print 'insertion_sort'

	##############################################################################################
elif y == '3':

	def mergeSort(lista):
	    
		if len(lista) > 1:
			meio = len(lista)/2
	        
			listaEsquerda = lista[:meio]
			listaDireita = lista[meio:]

			mergeSort(listaEsquerda)
			mergeSort(listaDireita)

			i = 0
			j = 0
			k = 0
	        
			while i < len(listaEsquerda) and j < len(listaDireita):
	            
				if listaEsquerda[i] < listaDireita[j]:
					lista[k]=listaEsquerda[i]
					i += 1
				else:
					lista[k]=listaDireita[j]
					j += 1
				k += 1

			while i < len(listaEsquerda):
	            
				lista[k]=listaEsquerda[i]
				i += 1
				k += 1

			while j < len(listaDireita):
				lista[k]=listaDireita[j]
				j += 1
				k += 1

	mergeSort(x)
	#print 'mergeSort'
	##############################################################################################
elif y == '4':

	def quickSort(lista):
		quickSortHelper(lista,0,len(lista)-1)

	def quickSortHelper(lista,primeiro,ultimo):
		if primeiro<ultimo:

			splitpoint = partition(lista,primeiro,ultimo)

			quickSortHelper(lista,primeiro,splitpoint-1)
			quickSortHelper(lista,splitpoint+1,ultimo)


	def partition(lista,primeiro,ultimo):
		primeiroValor = lista[primeiro]

		ladoEsquerdo = primeiro+1
		ladoDireito = ultimo

		done = False
		while not done:

			while ladoEsquerdo <= ladoDireito and lista[ladoEsquerdo] <= primeiroValor:
				ladoEsquerdo = ladoEsquerdo + 1

			while lista[ladoDireito] >= primeiroValor and ladoDireito >= ladoEsquerdo:
				ladoDireito = ladoDireito -1

			if ladoDireito < ladoEsquerdo:
				done = True
			else:
				temp = lista[ladoEsquerdo]
				lista[ladoEsquerdo] = lista[ladoDireito]
				lista[ladoDireito] = temp

		temp = lista[primeiro]
		lista[primeiro] = lista[ladoDireito]
		lista[ladoDireito] = temp

		return ladoDireito #tinha apagado sem querer

	quickSort(x)
	#print 'quickSort'

	##############################################################################################
elif y == '5':

	def heapsort(lst):
		for start in range((len(lst)-2)/2, -1, -1):
			siftdown(lst, start, len(lst)-1)

		for end in range(len(lst)-1, 0, -1):
			lst[end], lst[0] = lst[0], lst[end]
			siftdown(lst, 0, end - 1)
		return lst

	def siftdown(lst, start, end):
		root = start
		while True:
			child = root * 2 + 1
			if child > end: break
			if child + 1 <= end and lst[child] < lst[child + 1]:
				child += 1
			if lst[root] < lst[child]:
				lst[root], lst[child] = lst[child], lst[root]
				root = child
			else:
				break
	heapsort(x)
	#print 'Heapsort'

##############################################################################################
#print x
for t in x:
	print t
