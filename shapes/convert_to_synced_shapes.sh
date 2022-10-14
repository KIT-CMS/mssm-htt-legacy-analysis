#!/bin/bash

ERA=$1
CHANNEL=$2
VARIABLE=$3
TAG=$4

CONTROL=$5
MC=$6

[[ ! -z $5 ]] || CONTROL=0
[[ ! -z $6 ]] || MC=0

source utils/bashFunctionCollection.sh
source utils/setup_root.sh

if [[ $CONTROL == 0 ]]
then
    for PROC in bkg_sm mssm_gghpowheg mssm_bbhpowheg
    do 
        if [[ $MC == 0 ]]; then
            logandrun python shapes/convert_to_synced_shapes.py -e $ERA \
                                                                -i output/shapes/${ERA}-${CHANNEL}-analysis-shapes-${TAG}/shapes-analysis-${ERA}-${CHANNEL}-${PROC}.root \
                                                                -o output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC} \
                                                                --variable-selection ${VARIABLE} \
                                                                -n 12
            OUTFILE=output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC}.root
            echo "[INFO] Adding written files to single output file $OUTFILE..."
            logandrun hadd -f $OUTFILE output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC}/*.root
        elif [[ $MC == 1 ]]; then
            logandrun python shapes/convert_to_synced_shapes.py -e $ERA \
                                                                -i output/shapes/${ERA}-${CHANNEL}-analysis-shapes-${TAG}/shapes-analysis-${ERA}-${CHANNEL}-${PROC}.root \
                                                                -o output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC} \
                                                                --variable-selection ${VARIABLE} \
                                                                -n 12 \
                                                                --mc
            OUTFILE=output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC}_mc.root
            echo "[INFO] Adding written files to single output file $OUTFILE..."
            logandrun hadd -f $OUTFILE output/shapes/${ERA}-${CHANNEL}-${TAG}-synced_shapes_${VARIABLE}-${PROC}_mc/*.root
        else
            echo "[ERROR] Given MC option not known. Choose between 0 and 1."
            exit 1
        fi
    done
else
    logandrun python shapes/convert_to_synced_shapes.py -e $ERA \
                                                        -i output/shapes/${ERA}-${CHANNEL}-control-shapes-${TAG}/shapes-control-${ERA}-${CHANNEL}.root \
                                                        -o output/shapes/${ERA}-${CHANNEL}-${TAG}-gof-synced_shapes \
                                                        --gof \
                                                        -n 12
fi
