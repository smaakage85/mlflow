# Training and logging with [MLflow](https://mlflow.org/)

This project goes through exemplifies all of the alternatives MLflow has to offer with respect how to train and log machine learning models in Python.

To run all of the included examples, install: [Python](https://www.python.org/downloads/), [`miniconda`](https://docs.conda.io/en/latest/miniconda.html), [`virtualenv`](https://pypi.org/project/virtualenv/), [`docker`](https://docs.docker.com/get-docker/), [`pyenv`](https://github.com/pyenv/pyenv).

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

# Observations

RSTUDIO01, CONDA: 6½ minut
RSTUDIO01, VIRTUALENV + PIP: 1 minut
NORDRE DIGEVEJ 42, CONDA: 30 minutter
NORDRE DIGEVEJ 42, VIRTUALENV + PIP: ~5
Poor documentation for Docker Container integration
Only found one official example (that did not run)
Identified critical bug in mlflow (concerning!) Docker container integration
Identified bug in mlflow run: mlflow.set_tracking_uri does not work (tested w/conda)
Identified bug in mlflow run: virtualenv conflict with python_env.yaml
Only runs if image is built ex ante
Unlike when env_manager is set to 'virtualenv' or 'conda'
Seems mlflow developers do not put much effort into Docker Container (and R) integration
Do not like python built-ins: conda > pip and virtualenv > venv
draws upon 'virtualenv' and '
fordel ved docker: