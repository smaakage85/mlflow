# Findings

**Overall functionality**
- Cool functionality for logging models and experiment meta data
- Flexible functionality for implementing custom model flavors
- Will contribute to standardization of the model code and model development workflow
- We found 4 bugs ìn `mlflow` in just one week; is the code properly tested?
  - *Raises concerns for the code quality/stability of `mlflow`*
- Documentation is pretty bad, in some cases even for core functionality:
  - Docker integration, R integration, custom model flavors (e.g. `mlflow.pyfunc.PythonModel)
- `mlflow` only has half-hearted support for R (and maybe no support in the future?)

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
    - `mlflow` must have a 'python-first' strategy

**Identified bugs**
- R: `FIPS`
- `mlflow run` crashes, when env_manager is set to 'conda' and python_env.yaml exists
- `mlflow.set_tracking_uri` does not work together with `mlflow run`
- Docker example does not run


- Unlike when env_manager is set to 'virtualenv' or 'conda'
- Do not like python built-ins: conda > pip and virtualenv > venv
- draws upon 'virtualenv' and 'pyenv'
- svag dokumentation R log_model, mlflow.pyfunc.PythonModel
- support R + docker
- mlflow kommer ikke til at begrænse os ift. træning og logging
- bidrag til at strømline model/kode-udvikling
- fed funktionalitet
- 'conda' indtil fornylig default environment manager. Nu fraråder de eksplicit 'conda' og har indført 'pip' + 'virtualenv' som default.
- godkendt support af custom modeller
- har ikke beskæftiget mig med "model registry" og model deployment
