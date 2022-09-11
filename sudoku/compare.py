import glob
import io
from contextlib import redirect_stdout
from pprint import pprint
import importlib
import difflib
import sys

filenames = {filename.removesuffix('.py') for filename in glob.glob('*.py')} - {'compare'}

def collect_stdout(name):
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.import_module(name)
    return f.getvalue()


results = {name: collect_stdout(name) for name in filenames}

# print(*results.keys())
if len(set(v for v in results.values())) != 1:
    correct = results['norvig']
    wrong_ones = {k:v for k,v in results.items() if v != correct}

    # print(wrong_ones)
    # exit()
    if len(wrong_ones) == 1:
        wrong_one = ''.join(wrong_ones.keys())
        with open(wrong_one+'.out', 'w') as f:
            f.write(results[wrong_one])
        command = f'diff {wrong_one}.out norvig.out'
        print(command)
        # a = results[wrong_one]
        # b = results['norvig']
        # # sys.stdout.writelines(difflib.ndiff(a, b))
        # # sys.stdout.writelines(difflib.unified_diff(a, b, fromfile=f'{wrong_one}.out', tofile='norvig.out', lineterm='\n'))
        # # sys.stdout.writelines(difflib.context_diff(a, b, fromfile=f'{wrong_one}.out', tofile='norvig.out', lineterm=''))
    else:
        print(f"{wrong_ones.keys()} are wrong")
