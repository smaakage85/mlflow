# Findings

- Poor documentation for Docker Container integration
- Only found one official example (that did not run)
- Identified critical bug in mlflow (concerning!) Docker container integration
- Identified bug in mlflow run: mlflow.set_tracking_uri does not work (tested w/conda)
- Identified bug in mlflow run: virtualenv conflict with python_env.yaml
- Identified bug: Fips?
- Do they test their code?
- Only runs if image is built ex ante
- Unlike when env_manager is set to 'virtualenv' or 'conda'
- Seems mlflow developers do not put much effort into (R) integration
- Do not like python built-ins: conda > pip and virtualenv > venv
- draws upon 'virtualenv' and 'pyenv'
- svag dokumentation R log_model, mlflow.pyfunc.PythonModel
- support R + docker
- mlflow kommer ikke til at begrænse os ift. træning og logging
- bidrag til at strømline model/kode-udvikling
- fed funktionalitet
- 'conda' indtil fornylig default environment manager. Nu fraråder de eksplicit 'conda' og har indført 'pip' + 'virtualenv' som default.
