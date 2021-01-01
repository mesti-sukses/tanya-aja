import Function

idf = {}
idf_file = open("document/term.txt", "r")
for line in idf_file :
	d = line.split()
	idf[d[0]] = float(d[1])

print("Masukkan query : ", end='')
s = input()
words = s.split();
term = Function.unique_term(s)
tfidf = Function.tfidf(term, idf)

qtype = 'blank'
for word in words :
	if word == 'dimana' :
		qtype = 'tmpt'
	elif word == 'kapan' :
		qtype = 'tgl'
	elif word == 'kuliah' or word == 'sekolah' :
		qtype = 'sch'
	elif word == 'pekerjaan' :
		qtype = 'prfs'
	elif word == 'siapa' :
		qtype = 'org'

vsm = Function.search(tfidf, qtype)