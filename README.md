# Graphene Experiments

## Environment

```bash
export GR_EXP_HOME=$HOME/Documents/graphene-experiments
export PYTHON_HOME=$HOME/virtualenvs/PyExp
export PYTHONPATH=$GR_EXP_HOME
```

## Initialization

```bash
pyvenv-3.5 $PYTHON_HOME
source $PYTHON_HOME/bin/activate
pip install -r resources/requirements.txt
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
```
