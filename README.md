# Training and logging w/[MLflow](https://mlflow.org/)

## :candy: Model flavors

### Built-in

Training a model with one of the MLflow [built-in model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) is easy:

```bash
python train.py
```

### Custom

Training a model with a custom model flavor requires more footwork:

```bash
python train_custom.py --n_obs 15000
```

The user must define a model wrapper inheriting from the `mlflow.pyfunc.PythonModel` class (:arrow_right: ``./model_wrapper.py``).

## :shell: `mlflow run` CLI

MLflow offers a convenient built-in command-line interface for training and logging models: `mlflow run`. 

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










