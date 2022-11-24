# Training and logging with [MLflow](https://mlflow.org/) <img src='mlflow.jpeg' align="right" height="140" />

This project explores and exemplifies the different ways of training and logging (Python) machine learning models, that MLflow has to offer. 

To run all of the included examples, install: [`Python`](https://www.python.org/downloads/), [`miniconda`](https://docs.conda.io/en/latest/miniconda.html), [`virtualenv`](https://pypi.org/project/virtualenv/), [`docker`](https://docs.docker.com/get-docker/), [`pyenv`](https://github.com/pyenv/pyenv) and [`mlflow`>=2.0](https://pypi.org/project/mlflow/).

## :candy: Model flavors

MLflow provides support several standard [model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) meaning either model frameworks (e.g. `pytorch`, `tensorflow` or `scikit-learn`) or specific algorithms (e.g. `CatBoost`, `xgboost` or `LightGBM`) out-of-the-box. 

### Built-in flavors

Training and logging a model with one of the the built-in model flavors is straightforward:

```bash
python train.py
```

### Custom flavor

Training and logging a model with a custom model flavor requires more footwork:

```bash
python train_custom.py --n_obs 15000
```

In this case the user must define a model wrapper for the custom model inheriting from the `mlflow.pyfunc.PythonModel` equipped with specific methods like `load_context()` and `predict()`.

## :shell: Built-in Command-Line Interface

MLflow offers a convenient built-in command-line interface for training and logging models: `mlflow run`:

```bash
mlflow run . -e training --env-manager local
```

`mlflow run` requires an `MLproject` file specifying training specific options. As a bare minimum the `MLproject` must specify a training entrypoint. 

## :computer: Computational environments

The above experiments are all run in the active local environment. This means maximum flexibility on the developer side, which is great, but it also implies minimum reproducibility of the results.

### `virtualenv` environment

```bash
mlflow run . -e training --env-manager virtualenv
```

Uses `pyenv`.

### `conda` environment

```bash
mlflow run . -e training --env-manager conda
```

### Docker container

MLflow also has support for training a model in a Docker environment (as opposed to Conda). This allows for capturing non-Python dependencies, e.g. Java libraries.

See [this project](https://github.com/smaakage85/mlflowdocker) for an example.
