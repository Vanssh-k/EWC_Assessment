from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_sentence_embedding(sentence):
    return model.encode([sentence])[0]

def find_most_similar_sentence(input_phrase, english_keys):
    input_embedding = get_sentence_embedding(input_phrase)

    sentence_embeddings = np.array([get_sentence_embedding(sentence) for sentence in english_keys])

    similarities = cosine_similarity([input_embedding], sentence_embeddings)

    most_similar_idx = np.argmax(similarities)
    return english_keys[most_similar_idx], similarities[0][most_similar_idx]

def find_similarity(phrase1, phrase2):
    p1_embedding = get_sentence_embedding(phrase1)
    p2_embedding = get_sentence_embedding(phrase2)

    p1_embedding = p1_embedding.reshape(1, -1)
    p2_embedding = p2_embedding.reshape(1, -1)

    similarities = cosine_similarity(p1_embedding, p2_embedding)

    return similarities[0][0]