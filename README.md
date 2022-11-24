# Training and logging w/[MLflow](https://mlflow.org/)

## :candy: Model flavors

### Built-in flavor

Training a model with one of the MLflow [built-in model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) is easy:

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

`mlflow run` requires an `MLproject` file that specifies certain training options like training entrypoint(s).

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










