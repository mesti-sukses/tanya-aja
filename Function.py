import math
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from collections import Counter

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

# Untuk ngitung TF-IDF
def tfidf(documents, idf):
    doc_tfidf = []
    for term in idf.keys():
        tf = log_term_frequency(term, documents)
        # print(type(tf))
        # print("Term :" + term)
        # print(type(idf[term]))
        doc_tfidf.append(tf * idf[term])
    return doc_tfidf

def unique_term(data) :
    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    train_documents_stemmed = stemmer.stem(data)
    # print("Hasil Stemming Dokumen Training: ")
    # print(train_documents_stemmed)

    # tokenizing
    train_documents_tokenized = train_documents_stemmed.split()
    # print("Hasil Tokenisasi Dokumen Training: ")
    # print(train_documents_tokenized)

    # Stopword
    stop_words=[]
    with open("stop_words.txt") as f:
        content = f.readlines()
    stop_words = [x.strip() for x in content]
    #stop_words = ['dan', 'atau', 'itu']
    train_documents_filtered = [w for w in train_documents_tokenized if w not in stop_words]
    # print("Hasil Filtering Dokumen Training: ")
    # print(train_documents_filtered)

    # Biar ga dobel
    return train_documents_filtered
    # print("Term Unik: ")

def cosine(dataA, dataB) :
    AB = sum(dataA[i]*dataB[i] for i in range(len(dataA)))
    A = math.sqrt(sum(i**2 for i in dataA))
    B = math.sqrt(sum(i**2 for i in dataB))
    return AB/(A*B)

def search(tfidf, qtype) :
    # TF-IDF data hadist
    training_file = open("document/value.txt", "r")
    training_vsm = []
    training_type = []
    qtype_lib = []
    res = {}
    for line in training_file :
        line = line.split('|')
        training_type.append(line[0].split(';'))
        training_vsm.append([float(x) for x in line[1].split(';')])
    training_file.close()
    print("File training berhasil diload")
    
    for q in training_type :
        ktype = {}
        if len(q) > 1 :
            for k in q[1:] :
                l = k.split(':')
                ktype[l[0]] = l[1]
        qtype_lib.append(ktype)
    # print(qtype_lib)

    file = open("document/raw.txt", "r")
    training_raw = []
    for line in file :
        training_raw.append(line)
    file.close()

    for i,j in enumerate(range(len(training_vsm))) :
        if qtype in qtype_lib[i].keys() :
            tmp = cosine(training_vsm[i],tfidf)
        else :
            tmp = 0
        res[i] = tmp
        # print(tmp)
    print("Berhasil menghitung cosine")

    # Cari yang maksimal
    hasil = dict(Counter(res).most_common(1))
    for x,y in hasil.items() :
        if qtype == 'blank' :
            print(training_raw[x])
        else :
            print(qtype_lib[x][qtype])

    return training_vsm

def average(dataA, dataB) :
    return [(dataA[i] + dataB[i])/2 for i in range(len(dataA))]
