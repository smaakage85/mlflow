# Findings

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
draws upon 'virtualenv' and 'pyenv'
svag dokumentation R log_model, mlflow.pyfunc.PythonModel