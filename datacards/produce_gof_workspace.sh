#!/bin/bash

source utils/setup_cmssw.sh

ERA=$1
CHANNEL=$2
VARIABLE=$3

USE_MC=$4
[[ -z $4 ]] && USE_MC=0

if [[ ! -d ${PWD}/output/workspaces/ ]]
then
    mkdir -p ${PWD}/output/workspaces/
fi

if [[ "${USEMC}" == "1" ]]; then
    combineTool.py -M T2W \
        -o ${PWD}/output/workspaces/${ERA}-${CHANNEL}-${VARIABLE}-mc-control-workspace.root 
        -i output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-mc-control/_${VARIABLE}/${ERA}/htt_${CHANNEL}_300_${ERA}/
else
    combineTool.py -M T2W \
        -o ${PWD}/output/workspaces/${ERA}-${CHANNEL}-${VARIABLE}-control-workspace.root 
        -i output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-control/_${VARIABLE}/${ERA}/htt_${CHANNEL}_300_${ERA}/
fi
