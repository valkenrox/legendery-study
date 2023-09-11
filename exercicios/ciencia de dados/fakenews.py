import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv(r'C:/Users/soloq/Desktop/news.csv')

df.shape
df.head()

# Get the labels

labels = df.label
print(labels.head())


# Split the dataset
x_train,x_test,y_train,y_test= train_test_split(df['text'], labels, test_size=0.2, random_state=7) # 20% teste e 80% treino

# Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train = tfidf_vectorizer.fit_transform(x_train) # encaixa e transforma o texto em uma matriz de recursos TF-IDF na base de treino
tfidf_teste = tfidf_vectorizer.transform(x_test) # transforma o texto em uma matriz de recursos TF-IDF na base de teste


#DataFlair - inicializa o PassiveAggressiveClassifier
pac= PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
#DataFlair - prediz no conjunto de teste e calcula a precisão
y_pred=pac.predict(tfidf_teste)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

#DataFlair - constrói a matriz de confusão
print(confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))