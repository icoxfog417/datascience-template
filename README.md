# datascience-template

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
