import math
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#------------------------------------------------------------------------#

#Fungsi

def binary_term_frequency(term, tokenized_document):
    return term in tokenized_document

def raw_term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

def log_term_frequency(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    return 1 + math.log10(count)

def inverse_document_frequencies(tokenized_documents, all_tokens_set):
    idf_values = {}
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        # print(tkn)
        # print(len(tokenized_documents))
        res = len(tokenized_documents)/sum(contains_token)
        # print(res)
        idf_values[tkn] = math.log10(res)
    return idf_values

def tfidf(documents, idf):
    tfidf_documents = []
    for document in documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = log_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents

#------------------------------------------------------------------------#
#Preprocessing Dokumen Training

train_documents = []
ner = []
ner_entity = []
# Buka file hadist 
file = open("Corpus/01.txt")
for line in file :
    stripped = line.strip()
    for sentences in stripped.split('.') :
        if sentences != '' :
            s = re.sub(r'<[^>]*>',"" , sentences)
            entity = re.findall(r'</([^>]*)>', sentences)
            entity_item = re.findall(r'<[^>]*>([^<]*)</[^>]*>', sentences)
            ner_entity.append(entity_item)
            ner.append(entity)
            train_documents.append(s)
# print(s)
# Masukkan ke variabel train_documents
file.close()
print(ner)
print(ner_entity)
# print("Dokumen Training Asal: ")
# print(train_documents)

# Stemming dengan sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()
train_documents_stemmed = []
i = 1
for d in train_documents :
	print(i)
	train_documents_stemmed.append(stemmer.stem(d))
	i+=1
# print("Hasil Stemming Dokumen Training: ")
# print(train_documents_stemmed)

# Tokenizing
tokenize = lambda doc: doc.lower().split(" ")
train_documents_tokenized = [tokenize(d) for d in train_documents_stemmed]
# print("Hasil Tokenisasi Dokumen Training: ")
# print(train_documents_tokenized)

# Stopword removal
stop_words=[]
with open("stop_words.txt") as f:
    content = f.readlines()
stop_words = [x.strip() for x in content]
#stop_words = ['dan', 'atau', 'itu']
filter = lambda doc: [w for w in doc if w not in stop_words]
train_documents_filtered = [filter(d) for d in train_documents_tokenized]
# print("Hasil Filtering Dokumen Training: ")
# print(train_documents_filtered)

# Tokennya biar ga dobel
all_tokens_set = set([item for sublist in train_documents_filtered for item in sublist])
all_tokens_set.remove('')
print("Term Unik: ")
print(all_tokens_set)

# Hitung IDF
idf = inverse_document_frequencies(train_documents_filtered, all_tokens_set)
# print("IDF: ")
# print(idf)

# SImpan token dalam file
file = open("document/term.txt", 'w+')
for i,j in idf.items() :
	file.write(i + ' ' + str(j) + '\n')
file.close()

# print("TF-IDF Dokumen Training:")
file = open("document/value.txt", 'w+')
res = tfidf(train_documents_filtered, idf)
for i,j in enumerate(res) :
    ner_line = 'blank'
    for x,y in enumerate(ner[i]) :
        ner_line += ';' + y + ':' + ner_entity[i][x]
    s = ''.join(str(x) + ';' for x in j[:-1])
    s+= str(j[-1])
    file.write(ner_line + '|' + s + '\n')
file.close()

file = open('document/raw.txt', 'w+')
for i,j in enumerate(train_documents) :
    file.write(str(i) + ' ' + j + '\n')
file.close()
# print(res)