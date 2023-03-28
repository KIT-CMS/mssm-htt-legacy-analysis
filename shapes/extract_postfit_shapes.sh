#!/bin/bash

ERA=$1
CHANNEL=$2
VARIABLE=$3

USE_MC=$4
[[ -z $4 ]] && USE_MC=0

source utils/setup_cmssw.sh

if [[ ! -d output/shapes/${ERA}-${CHANNEL}-control-datacard-shapes-prefit/ ]]
then
    mkdir -p output/shapes/${ERA}-${CHANNEL}-control-datacard-shapes-prefit/
fi

if [[ "${USEMC}" == "1" ]]; then
    PostFitShapesFromWorkspace -m 125 \
        -w output/workspaces/${ERA}-${CHANNEL}-${VARIABLE}-mc-control-workspace.root \
        -d output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-mc-control/_${VARIABLE}/${ERA}/htt_${CHANNEL}_300_${ERA}/combined.txt.cmb \
        -o output/shapes/${ERA}-${CHANNEL}-control-datacard-shapes-prefit/${ERA}-${CHANNEL}-${VARIABLE}-mc-control-datacard-shapes-prefit.root
else
    PostFitShapesFromWorkspace -m 125 \
        -w output/workspaces/${ERA}-${CHANNEL}-${VARIABLE}-control-workspace.root \
        -d output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-control/_${VARIABLE}/${ERA}/htt_${CHANNEL}_300_${ERA}/combined.txt.cmb \
        -o output/shapes/${ERA}-${CHANNEL}-control-datacard-shapes-prefit/${ERA}-${CHANNEL}-${VARIABLE}-control-datacard-shapes-prefit.root
fi
