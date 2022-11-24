# Training and logging with [MLflow](https://mlflow.org/)

This project goes through all of the alternatives MLflow has to offer with respect to training and logging machine learning models. 

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

See [this project](https://github.com/smaakage85/mlflowdocker).










