# -Vibe-Coding-Sentiment-Analysis-on-Reddit

Bu proje, Reddit üzerinde "Yapay Zeka ve Gelecek" konulu gönderilerin duygu analizini yapmak için oluşturulmuştur. Proje, Python programlama dili ve Hugging Face'in Transformers kütüphanesi kullanılarak geliştirilmiştir.

## Projenin Amacı

Projenin temel amacı, Reddit'te "Yapay Zeka ve Gelecek" konulu gönderilerin başlıklarını analiz ederek, bu gönderilerin pozitif, negatif veya nötr duygu durumlarını belirlemektir. Bu analiz, BERT modeli kullanılarak gerçekleştirilir ve sonuçlar bir çubuk grafikle görselleştirilir.

## Gereksinimler

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `praw`: Reddit API'sine bağlanmak için kullanılır.
- `transformers`: Hugging Face'in BERT modelini kullanarak duygu analizi yapmak için kullanılır.
- `matplotlib`: Analiz sonuçlarını görselleştirmek için kullanılır.

Bu kütüphaneleri aşağıdaki komutla kurabilirsiniz:

```bash
pip install praw transformers matplotlib
