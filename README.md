# Training and logging w/[MLflow](https://mlflow.org/)

- virtualenv
- miniconda 
- docker

## :candy: Model flavors


### Built-in flavors

MLflow provides support several standard [Model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) meaning either model frameworks (e.g. `pytorch`, `torch`, `scikit-learn`) or specific algorithms (`CatBoost`, `xgboost`, `LightGBM`) out-of-the-box. Training a model with one of the these is straightforward:

```bash
python train.py
```

### Custom flavor

Training a model with a custom model flavor requires more footwork:

```bash
python train_custom.py --n_obs 15000
```

Note, the user must define a model wrapper inheriting from the `mlflow.pyfunc.PythonModel`.

## :shell: `mlflow run` CLI

MLflow offers a convenient built-in command-line interface for training and logging models: `mlflow run`. 

`mlflow run` requires an `MLproject` file specifying certain experiment specific options like training entrypoint(s) and environment requirements.

```bash
mlflow run . -e training --env-manager local
```

## :computer: Environments

### `conda` environment

```bash
mlflow run . -e training --env-manager conda
```

### `virtualenv` environment (w/`pyenv`)

```bash
mlflow run . -e training --env-manager virtualenv
```

### Docker container

See [this project](https://github.com/smaakage85/mlflowdocker).










