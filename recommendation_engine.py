import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# 1. تجهيز البيانات (القيم التي يختارها المستخدم)
data = {
    'item_id': [1, 2, 3],
    'tags': ['Python Cloud', 'Java Algorithms', 'Python Web Design']
}
df = pd.DataFrame(data)

# 2. تحويل النصوص إلى متجهات (Vector Mapping)
count = CountVectorizer()
count_matrix = count.fit_transform(df['tags'])

# 3. دالة التوصية (Similarity Logic)
def get_recommendations(user_preferences):
    # تحويل تفضيلات المستخدم إلى نفس فضاء المتجهات
    user_vec = count.transform([user_preferences])
    # حساب التشابه
    sim_scores = cosine_similarity(user_vec, count_matrix)
    # ترتيب النتائج
    df['score'] = sim_scores[0]
    return df.sort_values(by='score', ascending=False)

# تجربة النظام
print(get_recommendations('Python'))