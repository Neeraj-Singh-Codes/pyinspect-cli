# Practical 4 - 1:
plays={"Anthony and Cleopatra":"anthony is there, brutus is caeser is with cleopatra mercy worser.",
       "Julius Ceaser":"anthony is there, brutus is caeser is but calpurnia is.",
       "The Tempest":"mercy worser","Hamlet":"caeser and brutus are present with mercy and worser",
       "Othello":"caeser is present with mercy and worser","Macbeth":"anthony is there, caeser, mercy."}
words=["anthony","brutus","caeser","calpurnia","cleopatra","mercy","worser"]

vector_metrix = [[0 for i in range(len(plays))] for j in range(len(words))]

tokens = []
string_list = []
text_list = list((plays.values()))
for i in range(len(words)):
    for j in range(len(text_list)):
        if words[i] in text_list[j]:
            vector_metrix[i][j] = 1
        else:
            vector_metrix[i][j] = 0

for i in vector_metrix:
    print(i)

def query_op(query):
    tokens = query.lower().split()
    print(tokens)
    for vector in vector_metrix:
        my_string = " "
        for digit in vector:
            my_string += str(digit)
        string_list.append(int(my_string, 2))
    print(string_list)
    return tokens

def or_op():
    cnt = 0
    tokens = query_op("anthony brutus")
    for i in range(len(tokens)):
        for j in range(len(words)):
            if tokens[i] in words[j]:
                if cnt == 1:
                    second_index = j
                    cnt = 0
                    print(bin(string_list[first_index]|string_list[second_index]))
                else:
                    cnt = 1
                    first_index = j

def and_op():
    cnt = 0
    tokens = query_op("anthony mercy")
    for i in range(len(tokens)):
        for j in range(len(words)):
            if tokens[i] in words[j]:
                if cnt == 1:
                    second_index = j
                    cnt = 0
                    print(bin(string_list[first_index] & string_list[second_index]))
                else:
                    cnt = 1
                    first_index = j

def first_not_op():
    cnt = 0
    tokens = query_op("anthony")
    for i in range(len(tokens)):
        for j in range(len(words)):
            if tokens[i] in words[j]:
                print(string_list[j])
                MASKS = 0B11111
                print(bin(~(string_list[j] & MASKS)))

or_op()
and_op()
first_not_op()













# Practical 4 - 2:
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog chased the fox",
    "The dog is lazy"
]

query = "brown dog"
nltk.download("punkt")
nltk.download("punkt_tab")
tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]
tokenized_query = word_tokenize(query.lower())
preprocessed_documents = [" ".join(doc) for doc in tokenized_documents]
preprocessed_query = " ".join(tokenized_query)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_documents)
query_vector = tfidf_vectorizer.transform([preprocessed_query])
cosine_sim_values = cosine_similarity(query_vector, tfidf_matrix)[0]
results = list(zip(documents, cosine_sim_values))
results.sort(key=lambda x: x[1], reverse=True)
for doc, similarity in results:
    print(f"Similarity: {similarity:.2f}\n{doc}\n")