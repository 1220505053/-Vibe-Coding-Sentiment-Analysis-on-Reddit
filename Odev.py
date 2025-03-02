import praw
from transformers import pipeline
import matplotlib.pyplot as plt

# Reddit API'ye bağlanma
reddit = praw.Reddit(
    client_id="PHr9_Q1MmSWFIcxT-TXySg",
    client_secret="Nd5YB9Jyxu89JfZYwnaHLRw8siev3Q",
    user_agent="odev/1.0 (by u/Possible_Bridge614)"
)

# "Yapay Zeka ve Gelecek" başlığıyla arama yap
subreddit = reddit.subreddit("all")
posts = []
for post in subreddit.search("Yapay Zeka ve Gelecek", limit=5000):
    posts.append(post.title)

# Hugging Face Transformers BERT sentiment analizi pipeline'ı
classifier = pipeline("sentiment-analysis")

# Sentiment analizi yapalım
pozitif = 0
negatif = 0
nötr = 0

for post in posts:
    result = classifier(post)
    sentiment = result[0]['label']
    if sentiment == 'POSITIVE':
        pozitif += 1
    elif sentiment == 'NEGATIVE':
        negatif += 1
    else:
        nötr += 1

# Sonuçları çubuk grafikle görselleştirelim
etiketler = ['Pozitif', 'Negatif', 'Nötr']
değerler = [pozitif, negatif, nötr]

plt.bar(etiketler, değerler, color=['gold', 'lightcoral', 'lightskyblue'])
plt.title("Yapay Zeka ve Gelecek Konusundaki Reddit Gönderilerinin Sentiment Analizi (BERT)")
plt.xlabel("Sentiment")
plt.ylabel("Gönderi Sayısı")
plt.show()