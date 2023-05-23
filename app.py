from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import ast  # Import the ast module for literal_eval

df = pd.read_csv('./data/embeddings.csv')
app = Flask(__name__)
model = pickle.load(open("similarity-seach-model.pkl", "rb"))

# Convert the string representation of embeddings back to a list of floats
df['embeddings'] = df['embeddings'].apply(ast.literal_eval)

@app.route('/', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        user_description = request.form.get('description')
        user_embedding = model.encode([user_description])

        df['similarity'] = cosine_similarity(np.vstack(df['embeddings'].values), user_embedding)
        top_indexes = df['similarity'].argsort()[-10:][::-1]

        print(top_indexes)
        recommendations = []
        for i in top_indexes:
            recommendations.append({
                'name': df.iloc[i]["Product Name"],
                'url': df.iloc[i]["URL"],
                'price': df.iloc[i]["Price"]
            })
        print(recommendations)

        return render_template('index.html', recommendations=recommendations)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
