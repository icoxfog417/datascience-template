# datascience-template

[![Source Code Check](https://github.com/icoxfog417/datascience-template/actions/workflows/ci.yml/badge.svg)](https://github.com/icoxfog417/datascience-template/actions/workflows/ci.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-blue)](https://github.com/python/mypy)

Well structured and tested data science project template. You can use this [template](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) when creating the data sicence repository.


📁 **Organized**: The project structure is refereed to [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)

🚀 **Prepared**: Major libraries are prepared in `environment.yml`. If you are familiar with [Colaboratory](https://colab.research.google.com/?utm_source=scs-index) environment, please use `environment-colab.yml` .

✅ **Tested**: `scripts` are checked by common linter when [pre-commit](https://pre-commit.com/).

Here is the notebook link to provide the quick access to your analysis. You can create the conda environment by Right click `Build Conda Environment` or `conda create -f environment.yml` in Studio Lab.

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

## Customization

* `environment.yml`: Please specify the packages and versions. As a default, no version is specified.
* `.pre-commit-config.yaml`: Please check the `rev` to check the code.
* Change the Notebook url for `Open in Studio Lab`.
