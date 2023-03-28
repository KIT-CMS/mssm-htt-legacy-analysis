#!/bin/bash

source utils/setup_cmssw.sh

[[ ! -z $1  && ! -z $2 && ! -z $3 ]] || ( echo Invalid number of arguments; exit 1  )
ERA=$1
CHANNEL=$2
VARIABLE=$3
TAG=$4

USE_MC=$5
if [[ -z $5 ]]
then
    USE_MC=0
fi
outfolder=output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-control/
[[ "${USE_MC}" == "1" ]] && outfolder=output/datacards/${ERA}-${CHANNEL}-${VARIABLE}-mc-control/

MorphingCatVariables --base-path=output/shapes/${ERA}-${CHANNEL}-${TAG}-gof-synced_shapes/ \
		     --category=${CHANNEL}_${VARIABLE} \
		     --variable=${VARIABLE} \
	    	     --verbose=1 \
	    	     --output_folder=${outfolder} \
                     --use_mc=${USE_MC} \
                     --manual_rebinning=1 \
                     --sm_gg_fractions ${CMSSW_BASE}/src/CombineHarvester/MSSMvsSMRun2Legacy/data/higgs_pt_reweighting_fullRun2.root \
	    	     --era=${ERA}
