# Goal

The goal of this repository is to show how one can use the `papermill` module to run notebooks with [AzureML-SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py).

## Using this repository

There are two main notebooks used:

- [simple-pm-run.ipynb](simple-pm-run.ipynb) shows how to run a notebook using papermill in a variety of computes using the `Experiment.submit()` method.
- [simple-pm-run-as-pipeline.ipynb](simple-pm-run-as-pipeline.ipynb) shows how to run a notebook using papermill in the context of a PythonScriptStep inside of a AzureML Pipeline, and how that differs. It still submits the pipeline using the `Experiment.submit()` method, but the construction of the pipeline has impacts on whether the submit gets updated.

## Requirements

The notebooks require that `azureml-sdk` is installed in the kernel environment. The notebook goes through
a few examples of how you can run a template script that runs notebooks. 

## Workload

In the case of this example, `simple-pm-run.ipynb` will submit the `papermill_run_notebook.py` script in the `./projectDir` directory, which will, in turn, execute the `hello_world.ipynb` notebook (also in the `./projectDir` directory).

This entry script (`papermill_run_notebook.py`) is intended as a simplified version of the one used in the [Microsoft/Recommenders repository](https://github.com/Microsoft/Recommenders/blob/staging/reco_utils/aml/wide_deep.py) so that I can show effects of parameters such as `hash_paths` in `PythonScriptStep()` and `regenerate_outputs` in `Experiment.submit()`. See [simple-pm-run-as-pipeline.ipynb](simple-pm-run-as-pipeline.ipynb) for details.
