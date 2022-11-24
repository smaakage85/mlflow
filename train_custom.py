import argparse
import logging

import mlflow

from model_wrapper import (
    CustomModel,
    simulate_salaries
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MLflow run")

# parse arguments to training routine
parser = argparse.ArgumentParser()
parser.add_argument("--n_obs",
                    type=int,
                    default=10000,
                    help="number of observations")
args = parser.parse_args()

if __name__ == "__main__":
    with mlflow.start_run() as run:
        artifact_dir='outputs'
        logger.info(f"Arguments for this run: {args}")
        # get data for model training
        age, salary = simulate_salaries(n=args.n_obs)
        # train model from scratch and save to file
        m = CustomModel()
        m.train(age, salary)
        rmse = m.evaluate(age, salary)
        artifacts = m.save(dir=artifact_dir)
        logger.info(artifacts)
        # logging
        logger.info("Logging run with MLflow")
        mlflow.log_params({"n_obs": args.n_obs})
        mlflow.log_metrics({"rmse": rmse})
        mlflow.pyfunc.log_model(
            artifact_path="outputs",
            python_model=CustomModel(),
            artifacts=artifacts,
        )
        mlflow.end_run()