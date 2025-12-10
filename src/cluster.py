from sentence_transformers import SentenceTransformer

#generate embeddings
embedder = SentenceTransformer("all-mpnet-base-v2")
df["Embedding"] = df["Lyrics"].apply(lambda x: embedder.encode(str(x)).tolist())
df.to_csv("jvke_song_emotions.csv", index=False)
df.head

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
#compare songs' vectors' cosine similarity and load it into similarity_matrix
embedding_matrix = np.vstack(df["Embedding"].values)
similarity_matrix = cosine_similarity(embedding_matrix)
similarity_matrix[:5, :5]

from sklearn.cluster import KMeans
#creating clusters by unsupervised learning through K-Means
kmeans = KMeans(cluster_count, random_state = 42)
df["Cluster"] = kmeans.fit_predict(embedding_matrix)
df.to_csv("jvke_song_emotions.csv", index=False)
df[["Title", "Cluster"]]
