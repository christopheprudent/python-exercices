def myseq(n):
	if n<5:
		return 1
	else:
		return myseq(n-4)+myseq(n-3)+myseq(n-2)+myseq(n-1)

nth = int(input('Quel membre de la séquence voulez-vous obtenir: '))
print('La valeur du %dème membre vaut %d' %(nth, myseq(nth)))
