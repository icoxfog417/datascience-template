# datascience-template

Data science project template

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
