#Load libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
import joblib


# Read in dataset
file_path = r"C:\Users\nabe7\Documents\COMP_4450\Movie_Review_Sentiment_Analysis_App\IMDB Dataset.csv"
df = pd.read_csv(file_path)

# Split into features
X = df['review']
y = df['sentiment']

# Setting TfidfVectorizer
vectorizer = TfidfVectorizer()

# Create the pipeline
imbd_transformer = \
Pipeline([('vectorize_text', vectorizer),
        ('classifier', MultinomialNB())
          ])

# Setting parameters
param_grid = {
    'vectorize_text__max_features': [5000, 10000],
    'vectorize_text__ngram_range': [(1, 1), (1, 2)],
    'vectorize_text__stop_words': [None, 'english'],
    'classifier__alpha': [0.1, 0.5, 1.0, 2.0]
}

# Run GridSearchCV
grid_search = GridSearchCV(
    imbd_transformer,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs= -1
)

# Fit the model
grid_search.fit(X, y)

# Print best results
print("Best parameters:", grid_search.best_params_)
print("Best accuracy:  ", round(grid_search.best_score_ * 100, 2), "%")

# Save the model to a file
joblib.dump(grid_search.best_estimator_, 'sentiment_model.pkl')
print("Model trained and saved!")