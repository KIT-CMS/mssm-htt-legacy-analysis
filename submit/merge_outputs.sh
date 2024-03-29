#!/bin/bash

ERA=$1
IFS="," read -r -a CHANNELS <<< $2
TAG=$3

PREFIX="analysis"
if [[ "$4" == 1 ]]
then
    PREFIX="control"
fi

# Load submit splits of susy samples.
source utils/setup_susy_samples.sh $ERA
source utils/bashFunctionCollection.sh
source utils/setup_root.sh

BASE="output/shapes"

for CH in ${CHANNELS[@]}; do
    DIRNAME=${BASE}/${ERA}-${CH}-${PREFIX}-shapes-${TAG}
    echo "[INFO] Creating output dir $DIRNAME..."
    mkdir $DIRNAME
    if [[ "$PREFIX" =~ "analysis" ]]; then
        echo "[INFO] Adding outputs of background and sm signal jobs..."
        # hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string data,emb,ttj,ttl,ttt,vvj,vvl,vvt,w,zj,zl,ztt,ggh,gghww,qqh,qqhww,tth,wh,whww,zh,zhww)/*.root
        if [[ "$CH" == "et" || "$CH" == "mt" ]]; then
            hadd -n 600 -f ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string data,emb,ttl,ttt,vvl,vvt,zl,ztt,ggh,ggh95,qqh,qqh95,wh,zh)/*.root
        elif [[ "$CH" == "tt" ]]; then
            hadd -n 600 -f ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string data,emb,ttl,ttt,vvl,vvt,w,zl,ztt,ggh,ggh95,qqh,qqh95,wh,zh)/*.root
        else
            hadd -n 600 -f ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string data,emb,ttl,ttt,vvl,vvt,w,zl,ztt,ggh,ggh95,qqh,qqh95,wh,zh,gghww,qqhww,whww,zhww)/*.root
        fi
        # echo "[INFO] Adding outputs of background jobs..."
        # hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-data,emb,ttj,ttl,ttt,vvj,vvl,vvt,w,zj,zl,ztt/*.root
        # echo "[INFO] Adding outputs of sm signal jobs..."
        # hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-sm_signals.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-ggh,gghww,qqh,qqhww,tth,wh,whww,zh,zhww/*.root
        # echo "[INFO] Adding outputs of mssm bbh signal jobs..."
        # hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_bbh.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-bbh*/*.root
        # echo "[INFO] Adding outputs of mssm ggh signal jobs..."
        # hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_ggh.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_SAMPLES_SPLIT1})/*.root \
        #                                                                          output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_SAMPLES_SPLIT2})/*.root \
        #                                                                          output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_SAMPLES_SPLIT3})/*.root
        hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_bbhpowheg.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-bbhpowheg*/*.root
        echo "[INFO] Adding outputs of mssm ggh signal jobs..."
        hadd -j 5 -n 600 ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_gghpowheg.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_POWHEG_SPLIT1})/*.root \
                                                                                 output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_POWHEG_SPLIT2})/*.root \
                                                                                 output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string ${GGH_POWHEG_SPLIT3})/*.root
        echo "[INFO] Adding intermediate merge files to final merged file..."
        hadd ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}.root ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root \
                                                           ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_gghpowheg.root \
                                                           ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_bbhpowheg.root
        #                                                    ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_ggh.root \
        #                                                    ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-mssm_bbh.root
                                                           # ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-sm_signals.root \
    else
        echo "[INFO] Adding outputs of background and sm signal jobs..."
        hadd ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root output/shapes/${PREFIX}_unit_graphs-${ERA}-${CH}-$(sort_string data,emb,ttl,ttt,vvl,vvt,zl,ztt,ggh,qqh,wh,zh,gghpowheg100,gghpowheg1200)/*.root
        mv ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}-bkg_sm.root ${DIRNAME}/shapes-${PREFIX}-${ERA}-${CH}.root
    fi
done
