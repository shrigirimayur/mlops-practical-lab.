from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score

def main():
    data = load_breast_cancer(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
    )
    pipe = Pipeline([("scale", StandardScaler()),
                     ("model", LogisticRegression(max_iter=3000))])
    params = {"model__C": [0.01, 0.1, 1.0, 10.0]}
    methods = [
        ("Grid Search", GridSearchCV(pipe, params, cv=5, scoring="f1", n_jobs=-1)),
        ("Random Search", RandomizedSearchCV(pipe, params, n_iter=4, cv=5,
                                             scoring="f1", random_state=42, n_jobs=-1)),
    ]
    for name, search in methods:
        search.fit(X_train, y_train)
        pred = search.predict(X_test)
        print(name)
        print("Best parameters:", search.best_params_)
        print("Best CV F1:", round(search.best_score_, 4))
        print("Test accuracy:", round(accuracy_score(y_test, pred), 4))
        print("Test F1:", round(f1_score(y_test, pred), 4))

if __name__ == "__main__":
    main()
