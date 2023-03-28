#!/bin/bash

ERA=$1
CHANNEL=$2
TAG=$3
MODE=$4

if [[ ! -z $5 ]]
then
    IFS="," read -a VARIABLES <<< $5
else
    VARIABLES=(pt_1 pt_2 eta_1 eta_2 m_sv_puppi m_vis jpt_1 jpt_2 jeta_1 jeta_2 dijetpt jdeta mjj njets_red nbtag_red bpt_1 bpt_2 mTdileptonMET_puppi mt_1_puppi mt_2_puppi pZetaPuppiMissVis ptvis pt_tt_puppi puppimet)
fi

case $MODE in

    "postprocess-shapes")
        # Merge the shapes.
        bash submit/merge_outputs.sh $ERA $CHANNEL $TAG 1

        # Produce the different estimations.
        bash shapes/do_estimations.sh $ERA output/shapes/${ERA}-${CHANNEL}-control-shapes-${TAG}/shapes-control-${ERA}-${CHANNEL}.root 1

        # Convert them to synced shapes,
        bash shapes/convert_to_synced_shapes.sh $ERA $CHANNEL dummy $TAG 1
        ;;

    "prepare-plots")
        for VAR in ${VARIABLES[@]}
        do
            for USEMC in 0
            do
                # Produce the datacards.
                bash datacards/produce_gof_datacard.sh $ERA $CHANNEL $VAR $TAG $USEMC
                # Produce the workspaces.
                bash datacards/produce_gof_workspace.sh $ERA $CHANNEL $VAR $USEMC
                # Produce the prefit shapes.
                bash shapes/extract_postfit_shapes.sh $ERA $CHANNEL $VAR $USEMC
            done
        done
        ;;

    "do-plot")
        for VAR in ${VARIABLES[@]}
        do
            for USEMC in 0
            do
                if [[ $USEMC == 1 ]]; then
                    bash plotting/plot_shapes_control_systematics.sh $ERA $CHANNEL $VAR 1 0
                else
                    bash plotting/plot_shapes_control_systematics.sh $ERA $CHANNEL $VAR 1 1
                fi
            done
        done
        ;;

    "do-gof")
        [[ ! -d output/gof ]] && mkdir -p output/gof
        [[ ! -d log/gof ]] && mkdir -p log/gof
        [[ -f output/gof/arguments-${ERA}-${CHANNEL}.txt ]] && rm output/gof/arguments-${ERA}-${CHANNEL}.txt
        # Modify template gof submit file for specific task
        cp gof/gof_submit.jdl output/gof/gof_submit_${ERA}-${CHANNEL}.jdl
        echo "queue a1,a2,a3,a4,a5 from output/gof/arguments-${ERA}-${CHANNEL}.txt" >> output/gof/gof_submit_${ERA}-${CHANNEL}.jdl
        # Write out arguments file containing the arguments to the gof executable
        for VAR in ${VARIABLES[@]}; do
            echo "${PWD} $ERA $CHANNEL $VAR saturated" >> output/gof/arguments-${ERA}-${CHANNEL}.txt
        done
        # Submit the gof jobs
        condor_submit output/gof/gof_submit_${ERA}-${CHANNEL}.jdl
        ;;

    *)
        echo -e "\033[0;31m[ERROR]\033[0m Given mode $MODE not known.\n Choose from 'postprocess-shapes', 'prepare-plots', 'do-plot'."
        exit 42
        ;;
esac
