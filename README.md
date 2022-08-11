# datascience-template

[![Source Code Check](https://github.com/icoxfog417/datascience-template/actions/workflows/ci.yml/badge.svg)](https://github.com/icoxfog417/datascience-template/actions/workflows/ci.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-blue)](https://github.com/python/mypy)

Data science project template.

[![Open in SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/icoxfog417/datascience-template/blob/main/notebooks/example.ipynb)

## Project Structure

```bash
.
├── data
│   ├── external                    # data from third party sources.
│   ├── processed                   # data after processing
│   ├── interim                     # data that transformed
│   └── raw                         # raw data
├── models                          # store models
├── notebooks                       # store notebooks
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── scripts                         # store source code used in notebook
│   └── __init__.py                 # make src a Python module
└── tests                           # store tests
    └── __init__.py                 # make tests a Python module
```

## Getting Started

Create the repository from this [template](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

After creating the repository, customize the following points.

* `environment.yml`: Please specify the packages and versions. As a default, no version is specified.
* `.pre-commit-config.yaml`: Please check the `rev` to check the code.
* Change the Notebook url for `Open in Studio Lab`.
