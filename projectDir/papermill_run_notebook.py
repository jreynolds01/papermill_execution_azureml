import os
import papermill as pm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--kernel-name", type=str, 
                    default='python3',
                    help="kernel name used to execute the notebook")
parser.add_argument("-i", "--input", type=str, 
                    default="hello_world.ipynb",
                    help="input notebook to execute")
parser.add_argument("-o", "--output", type=str, 
                    default="outputs/hello_world_output.ipynb",
                    help="output notebook to write to")
## parameters for hello_world
parser.add_argument("-x", type=int, 
                    default=1,
                    help="value of x parameter in notebook")
parser.add_argument("-y", type=int, 
                    default=1,
                    help="value of y parameter in notebook")

args = parser.parse_args()

KERNEL_NAME = args.kernel_name

OUTPUT_NOTEBOOK = args.output

## make sure output directory exists
outdir = os.path.dirname(OUTPUT_NOTEBOOK)

if outdir is "":
    outdir = os.getcwd()

if not os.path.isdir(outdir):
    print("output directory", outdir, "does not exist. Creating.")
    os.makedirs(outdir)

notebooks = {
    "hello_world": args.input
}

notebook_path = notebooks["hello_world"]
pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        kernel_name=KERNEL_NAME,
        parameters=dict(
            x=args.x,
            y=args.y
        )
)


nb = pm.read_notebook(OUTPUT_NOTEBOOK)

## Now log thing via AML 
try:
    from azureml.core import Run
    run = Run.get_context()
except ImportError:
    run = None

print('*** run value is:', run)

def _log(metric, value):
    if run is not None:
        print('logging variables with AML logging functions.')
        if type(value) == list and len(value) > 0 and (type(value[0]) == int or type(value[0]) == float):
            run.log_list(metric, value)
        else:
            run.log(metric, str(value))
    else:
        print("Not logging with AML logging functions. Just printing them.")
    print(metric, "=", value)

for m, v in nb.data.items():
    _log(m, v)

## for checking the script has changed and what is being logged.
_log('msg2', 'run1')