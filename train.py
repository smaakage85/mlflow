import numpy as np
from sklearn.linear_model import LogisticRegression
import mlflow

if __name__ == "__main__":    
    ## connect to MLflow server through tracking URI
    # mlflow.set_tracking_uri([MLFLOW_TRACKING_URI])    
    with mlflow.start_run() as run:
        X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
        y = np.array([0, 0, 1, 1, 1, 0])
        lr = LogisticRegression()
        lr.fit(X, y)
        score = lr.score(X, y)
        print("Score: %s" % score)
        mlflow.log_metric("score", score)
        mlflow.sklearn.log_model(lr, "model")
