import os
from pathlib import Path

import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neural_network import MLPClassifier

DRIVE_DIRECTORY = Path.cwd() / "data"

df = pd.read_csv(os.path.join(DRIVE_DIRECTORY, "df_cleveland_limpo.csv"))

X = df.drop(columns=["num"]).values
y = df["num"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# rede_neural_cleveland = MLPClassifier(
#     max_iter=3000,
#     verbose=True,
#     tol=0.00000100,
#     solver="lbfgs",
#     activation="relu",
#     hidden_layer_sizes=(8, 8),
# )
# rede_neural_cleveland.fit(X_train, y_train)

# previsoes = rede_neural_cleveland.predict(X_test)

# print(accuracy_score(y_test, previsoes))
# print(classification_report(y_test, previsoes))

parametros = {
    "learning_rate": ['constant', 'invscaling', 'adaptive'],
    "activation": ['relu', 'identity', 'logistic', 'tanh'],
    "solver": ["adam", "sgd", "lbfgs"],
    'tol': [
        0.1,
        0.01,
        0.001,
    ],
    'batch_size':[
        2, 3, 5, 7, 11, 13, 17, 19
    ]
}
grid_search = GridSearchCV(estimator=MLPClassifier(), param_grid=parametros, verbose=True)
grid_search.fit(X_train, y_train)
melhores_parametros = grid_search.best_params_
melhores_resultado = grid_search.best_score_

print(melhores_parametros)
print(melhores_resultado)
#  {'activation': 'logistic', 'batch_size': 7, 'learning_rate': 'invscaling', 'solver': 'lbfgs', 'tol': 0.01}
