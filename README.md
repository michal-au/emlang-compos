This code implements the experiments reported in the following paper:

* *Defending Compositionality in Emergent Languages*. Michal Auersperger, Pavel Pecina. NAACL SRW 2022. [[arxiv]](https://arxiv.org/abs/2206.04751)

# Edit
The code has been merged to the official [EGG toolkit repository](https://github.com/facebookresearch/EGG). You can find it along other experiments in the `egg/zoo` directory: [egg/zoo/compo_vs_generalization_ood](https://github.com/facebookresearch/EGG/tree/main/egg/zoo/compo_vs_generalization_ood) and ignore this repository.
_______________________________

### Installation
The code uses the [EGG toolkit](https://github.com/facebookresearch/EGG), which can be installed like this:

`pip install git+ssh://git@github.com/facebookresearch/EGG.git`

### Running experiments
A single experiment of the full communication game can be run as follows:

```bash
python train  --n_values=50 --n_attributes=2 --vocab_size=50 --max_len=3  --receiver=ModifReceiver --sender=ModifSender --hidden=50 --batch_size=64 --random_seed=1
```

To run an experiment with a single agent on half of the problem only (i.e., a *learning alone* experiment from the paper), run e.g.: 
```bash
python -m learning_alone.train  --n_values=50 --n_attributes=2 --vocab_size=50 --max_len=5 --archpart=sender --model=OrigSenderDeterministic --hidden=50 --batch_size=64 --random_seed=1 
```

See the article for further details.

The scripts log information to STDOUT. 


#### Hyperparameters

To replicate the *full experiments*, use the hyperparameters in `./hyperparams/modified_arch.json` and `./hyperparams/orig_arch.json`.

To replicate the *learning alone experiments*, use the hyperparameters in `./hyperparams/learning_alone/receiver.json` and `./hyperparams/learning_alone/sender.json`.

We use a simple `gs.py` script to process the hyperparameter jsons.
This selects a specific configuration of the hyperparameters from a hyperparams file based on a `run_id`
that we get from the job scheduler at our computational cluster. E.g.,
```bash
python gs.py --gs_file learning_alone/sender.json --count_runs
```
returns the number of runs defined by the json (40) and
```bash
python gs.py --gs_file learning_alone/sender.json --exp_type learning_alone --run_id 1
```
runs the first one.



#### Processing the log files
For convenience, we attach the log files of our full experiment runs in `results/orig_arch/220520T115546` and `results/modified_arch/220517T231916`. The notebook `ntb-results-full.ipynb` processes the logs and produces Table 2 and Figure 1 from the paper.

