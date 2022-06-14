import sys
import argparse
from pathlib import Path
import json
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("--gs_file", type=Path, help="gridsearch config")
parser.add_argument("--run_id", type=int,
                    help="the id of a specific configuration of hparams, (>=1)")
parser.add_argument("--count_runs", action='store_true',
                    help="only prints out the number of possible configurations in the gs_file")
parser.add_argument("--exp_type", type=str, default='full',
                    help="full or learning_alone")

params = parser.parse_args(sys.argv[1:])


gs_dict = json.load(('hyperparams' / params.gs_file).open('r'))
combinations = list(itertools.product(*gs_dict.values()))

if params.count_runs:
    print(len(combinations))
    exit()

assert params.exp_type in ('full', 'learning_alone')

gs_params = {k:v for k, v in zip(gs_dict.keys(), combinations[params.run_id-1])}
params_list = []
for k,v in gs_params.items():
    params_list.append(f"--{k}")
    params_list.append(str(v))

if params.exp_type == 'full':
    import train
    train.main(params_list)
else:
    from learning_alone import train
    train.main(params_list)
