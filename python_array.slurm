#!/bin/bash

####### Reserve computing resources #######
#SBATCH --nodes=1 
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --mem=20G
#SBATCH --partition=cpu2019

# Email settings 
#SBATCH --mail-user=maria.masolivervila@ucalgary.ca
#SBATCH --mail-type=ALL

# Set where you want the standard our and standard error to go
#SBATCH --output=./Report/M-%x.%j.out
#SBATCH --error=./Report/M-%x.%j.err

# Name of the matlab function to be called
MAIN="RNN_two_sup_chimera_lorenz"

# Define key parameters for the example calculation.
# $SLURM_ARRAY_TASK_ID is the variable containing the value passed in by sbatch --array=

S0=$SLURM_ARRAY_TASK_ID
# Name of results file or directory
RESULTS_FILE=./Results

ARGS=" $RESULTS_FILE $S0"
MAIN_WITH_ARGS=${MAIN}.py${ARGS}

echo "Calling python function: ${MAIN_WITH_ARGS}"

echo "Starting run at $(date)"
echo "Running on compute node $(hostname)"
echo "Running from directory $(pwd)"

# Load modules you require ex. python
module load python/anaconda3-2018.12

# Can now use conda to load enviroments and modules  
echo "Using python version: $(which python)"

#### Actual Job Call ####
python ${MAIN_WITH_ARGS} > ./Out/${MAIN}_Py_${SLURM_JOB_ID}.out 2>&1

echo "Finished run at $(date)"

