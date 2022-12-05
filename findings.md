# Findings

**Overall functionality**
- Cool functionality for logging models and experiment meta data
- Flexible functionality for implementing custom model flavors
- Will contribute to standardization of the model code and model development workflow
- We found 4 bugs ìn `mlflow` in just one week; is the code properly tested?
  - Raises concerns for the code quality/stability of `mlflow`
- Documentation is pretty bad, in some cases even for core functionality:
  - Docker integration, R integration, custom model flavors (e.g. `mlflow.pyfunc.PythonModel)
- `mlflow` only has half-hearted support for R (and maybe even no support in the future?)
- `mlflow` discourage the use of `conda`. This suggests, that `conda` might not be supported in the future.

**Docker integration**
- Poor documentation
- Only one official example available
  - The run!
  - It seems like, the docker integration works differently from the flow described in the example
    - Only runs if the docker image is build ex ante (unlike `virtualenv` and `conda` flows)

**R integration**
- Seems `mlflow` developers do not put much effort into R integration
  - Core functionality like `log_model()` is not documented
  - New flagship functionality like `MLflow Recipes` is not even implemented in R
    - `mlflow` clearly a 'python-first' strategy

**Identified bugs**
- R: `FIPS`
- `mlflow run` crashes, when env_manager is set to 'conda' and python_env.yaml exists
- `mlflow.set_tracking_uri` does not work together with `mlflow run`
- Docker example does not run (and works quite differently from the flow described in the documentation)

**Misc**
- env_manager="virtualenv" uses python package `virtualenv` together with `pyenv`
  - 'venv' is not supported
- 'mlflow' team seems to not have a preference built-ins: `conda` > `pip` and `virtualenv` > `venv`
- 'conda' was the default mlflow environment manager until R.0 release. Now `mlflow` advices the user NOT to use `conda`. Instead they now recommend `virtualenv` + `pip` (=new default).
