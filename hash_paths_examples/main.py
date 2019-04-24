from helper1 import helper1
from helper2 import helper2

out1 = helper1()
out2 = helper2()
main_value = 1

## print it out...
print('msg1={}'.format(out1))
print('msg2={}'.format(out2))

try:
    from azureml.core import Run
    run = Run.get_context()
except ImportError:
    run = None

if run is not None:
    run.log('main_value', main_value)
    run.log('msg1', out1)
    run.log('msg2', out2)

