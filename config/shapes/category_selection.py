from ntuple_processor import Histogram
from ntuple_processor.utils import Selection

m_sv_hist = Histogram("m_sv_puppi", "m_sv_puppi", [i for i in range(0, 255, 5)])
mt_tot_hist = Histogram("mt_tot_puppi", "mt_tot_puppi", [i for i in range(0, 3900, 10)])


lt_categorization = [
    # Categorization targetting standard model processes.
    (Selection(name="NJets0_MTLt40",             cuts = [("njets==0&&mt_1_puppi<40", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJets0_MT40To70",           cuts = [("njets==0&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJetsGt0_DeltaRGt2p5",      cuts = [("njets>=1&&DiTauDeltaR>=2.5", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJets1_PTHLt120",           cuts = [("njets>=1&&DiTauDeltaR<2.5&&pt_tt_puppi<120", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJets1_PTH120To200",        cuts = [("njets>=1&&DiTauDeltaR<2.5&&pt_tt_puppi>=120&&pt_tt_puppi<200", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJets1_PTHGt200",           cuts = [("njets>=1&&DiTauDeltaR<2.5&&pt_tt_puppi>=200", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJetsGt1_MJJLt350",         cuts = [("njets>=2&&DiTauDeltaR<2.5&&mjj<350", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJetsGt1_MJJ350To1000",     cuts = [("njets>=2&&DiTauDeltaR<2.5&&mjj>=350&&mjj<1000", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    (Selection(name="NJetsGt1_MJJGt1000",        cuts = [("njets>=2&&DiTauDeltaR<2.5&&mjj>=1000", "category_selection"),
                                                        ("mt_1_puppi<70", "signal_region_cut"),
                                                        ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
            [m_sv_hist]),
    # Pure MSSM analysis categories.
    (Selection(name="Nbtag0_MTLt40",             cuts = [("nbtag==0&&mt_1_puppi<40", "category_selection")]),
            [mt_tot_hist]),
    (Selection(name="Nbtag0_MT40To70",           cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
            [mt_tot_hist]),
    # MSSM and SM analysis categories
    (Selection(name="Nbtag0_MTLt40_MHGt250",     cuts = [("nbtag==0&&mt_1_puppi<40&&m_sv_puppi>=250", "category_selection")]),
            [mt_tot_hist]),
    (Selection(name="Nbtag0_MT40To70_MHGt250",   cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70&&m_sv_puppi", "category_selection")]),
            [mt_tot_hist]),
    (Selection(name="NbtagGt1_MTLt40",           cuts = [("nbtag>=1&&mt_1_puppi<40", "category_selection")]),
            [mt_tot_hist]),
    (Selection(name="NbtagGt1_MT40To70",         cuts = [("nbtag>=1&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
            [mt_tot_hist]),
    # Control region.
    (Selection(name="MTGt70",                    cuts = [("mt_1_puppi>=70", "category_selection")]),
            [mt_tot_hist]),
]

categorization = {
    "et": lt_categorization,
    "mt": lt_categorization,
    "tt": [
            # Categorization targetting standard model processes.
            (Selection(name="Njets0_DeltaRLt3p2",                        cuts=[("njets==0&&DiTauDeltaR<3.2", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="Njets1_DeltaRLt2p5_PTHLt100",               cuts=[("njets==1&&DiTauDeltaR<2.5&&pt_tt_puppi<100", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="Njets1_DeltaR2p5To3p2_PTHLt100",            cuts=[("njets==1&&DiTauDeltaR>=2.5&&DiTauDeltaR<3.2&&pt_tt_puppi<100", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="Njets1_DeltaRLt3p2_PTHGt100",               cuts=[("njets==1&&DiTauDeltaR<3.2&&pt_tt_puppi>=100", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NjetsGt2_DeltaRLt2p5_MJJLt350",             cuts=[("njets>=2&&DiTauDeltaR<2.5&&mjj<350", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NjetsGt2_DeltaRLt2p5_MJJGt350_EtaJJLt4",    cuts=[("njets>=2&&DiTauDeltaR<2.5&&mjj>=350&&jdeta<4", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NjetsGt2_DeltaRLt2p5_MJJGt350_EtaJJGt4",    cuts=[("njets>=2&&DiTauDeltaR<2.5&&mjj>=350&&jdeta>=4", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NjetsLt2_DeltaRGt3p2_NjetsGt2_DeltaGt2p5",  cuts=[("(njets<2&&DiTauDeltaR>=3.2)||(njets>=2&&DiTauDeltaR>=2.5)", "category_selection"),
                                                                              ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0",                                    cuts=[("nbtag==0", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories.
            (Selection(name="Nbtag0_MHGt250",                            cuts=[("nbtag==0&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1",                                  cuts=[("nbtag>=1", "category_selection")]),
                    [mt_tot_hist]),
    ],
    "em": [
            # Categorization targetting standard model processes.
            (Selection(name="NJets0_DZetam35Tom10_PTHLt10",  cuts=[("njets==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10&&pt_tt_puppi<10", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets0_DZetam35Tom10_PTHGt10",  cuts=[("njets==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10&&pt_tt_puppi>=10", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets0_DZetamGtm10_PTHLt10",    cuts=[("njets==0&&pZetaPuppiMissVis>=-10&&pt_tt_puppi<10", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets0_DZetamGtm10_PTHGt10",    cuts=[("njets==0&&pZetaPuppiMissVis>=-10&&pt_tt_puppi>=10", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets1_PTHLt40",                cuts=[("njets==1&&pt_tt_puppi<40", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets1_PTH40To120",             cuts=[("njets==1&&pt_tt_puppi>=40&&pt_tt_puppi<120", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets1_PTH120To200",            cuts=[("njets==1&&pt_tt_puppi>=120&&pt_tt_puppi<200", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJets1_PTHGt200",               cuts=[("njets==1&&pt_tt_puppi>=200", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJetsGt2_MJJLt350",             cuts=[("njets>=2&&mjj<350", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            (Selection(name="NJetsGt2_MJJGt350",             cuts=[("njets>=2&&mjj>=350", "category_selection"),
                                                                  ("pZetaPuppiMissVis>=-35", "signal_region_cut"),
                                                                  ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [m_sv_hist]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0_DZetam35Tom10",          cuts=[("nbtag==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetam10To30",           cuts=[("nbtag==0&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetaGt30",              cuts=[("nbtag==0&&pZetaPuppiMissVis>=30", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories.
            (Selection(name="Nbtag0_DZetam35Tom10_MHGt250",  cuts=[("nbtag==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetam10To30_MHGt250",   cuts=[("nbtag==0&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetaGt30_MHGt250",      cuts=[("nbtag==0&&pZetaPuppiMissVis>=30&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetam35Tom10",        cuts=[("nbtag>=1&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetam10To30",         cuts=[("nbtag>=1&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetaGt30",            cuts=[("nbtag>=1&&pZetaPuppiMissVis>=30", "category_selection")]),
                    [mt_tot_hist]),
            # Control regions.
            (Selection(name="DZetaLtm35",                    cuts=[("pZetaPuppiMissVis<-35", "category_selection")]),
                    [mt_tot_hist]),
    ],
}

discr_str = ("(0.5"
             "+({channel}_qqh<0.35)*("
             "    0.0*({channel}_ggh<0.2)"
             "    +1.0*({channel}_ggh>=0.2&&{channel}_ggh<0.3)"
             "    +2.0*({channel}_ggh>=0.3&&{channel}_ggh<0.4)"
             "    +3.0*({channel}_ggh>=0.4&&{channel}_ggh<0.5)"
             "    +4.0*({channel}_ggh>=0.5&&{channel}_ggh<0.65)"
             "    +5.0*({channel}_ggh>=0.65&&{channel}_ggh<0.8)"
             "    +6.0*({channel}_ggh>=0.8)"
             ")"
             "+({channel}_qqh>=0.35&&{channel}_qqh<0.5)*("
             "    7.0*({channel}_ggh<0.2)"
             "    +8.0*({channel}_ggh>=0.2&&{channel}_ggh<0.3)"
             "    +9.0*({channel}_ggh>=0.3&&{channel}_ggh<0.4)"
             "    +10.0*({channel}_ggh>=0.4&&{channel}_ggh<0.5)"
             "    +11.0*({channel}_ggh>=0.5&&{channel}_ggh<0.65)"
             ")"
             "+({channel}_qqh>=0.5&&{channel}_qqh<0.6)*("
             "    12.0*({channel}_ggh<0.2)"
             "    +13.0*({channel}_ggh>=0.2&&{channel}_ggh<0.3)"
             "    +14.0*({channel}_ggh>=0.3&&{channel}_ggh<0.4)"
             "    +15.0*({channel}_ggh>=0.4&&{channel}_ggh<0.5)"
             ")"
             "+({channel}_qqh>=0.6&&{channel}_qqh<0.7)*("
             "    16.0*({channel}_ggh<0.2)"
             "    +17.0*({channel}_ggh>=0.2&&{channel}_ggh<0.3)"
             "    +18.0*({channel}_ggh>=0.3&&{channel}_ggh<0.4)"
             ")"
             "+({channel}_qqh>=0.7&&{channel}_qqh<0.8)*("
             "    19.0*({channel}_ggh<0.2)"
             "    +20.0*({channel}_ggh>=0.2&&{channel}_ggh<0.3)"
             ")"
             "+21.0*({channel}_qqh>=0.8&&{channel}_qqh<0.85)"
             "+22.0*({channel}_qqh>=0.85&&{channel}_qqh<0.9)"
             "+23.0*({channel}_qqh>=0.9&&{channel}_qqh<0.92)"
             "+24.0*({channel}_qqh>=0.92&&{channel}_qqh<0.94)"
             "+25.0*({channel}_qqh>=0.94&&{channel}_qqh<0.96)"
             "+26.0*({channel}_qqh>=0.96&&{channel}_qqh<0.98)"
             "+27.0*({channel}_qqh>=0.98))")

fine_binning = [0.0, 0.3, 0.4, 0.45, 0.5, 0.55,  0.6, 0.65, 0.7,
                0.75, 0.8, 0.85, 0.9, 0.92, 0.94, 0.96, 0.98, 1.]
et_hist = Histogram("et_max_score", "et_max_score", fine_binning)
mt_hist = Histogram("mt_max_score", "mt_max_score", fine_binning)
tt_hist = Histogram("tt_max_score", "tt_max_score", fine_binning)
em_hist = Histogram("em_max_score", "em_max_score", fine_binning)

nn_categorization = {
        "et": [
            (Selection(name="emb",  cuts=[("et_max_index=={index}".format(index=2), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [et_hist]),
            (Selection(name="tt",   cuts=[("et_max_index=={index}".format(index=3), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [et_hist]),
            (Selection(name="misc", cuts=[("et_max_index=={index}".format(index=4), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [et_hist]),
            (Selection(name="zll",  cuts=[("et_max_index=={index}".format(index=5), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [et_hist]),
            (Selection(name="ff",   cuts=[("et_max_index=={index}".format(index=6), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [et_hist]),
            (Selection(name="xxh",  cuts=[("(et_max_index=={index1}||et_max_index=={index2})".format(index1=0, index2=1), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [Histogram("stxs_stage0_2Ddiscr", discr_str.format(channel="et"), list(range(29)))]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0_MTLt40",             cuts = [("nbtag==0&&mt_1_puppi<40", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_MT40To70",           cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories
            (Selection(name="Nbtag0_MTLt40_MHGt250",     cuts = [("nbtag==0&&mt_1_puppi<40&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_MT40To70_MHGt250",   cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70&&m_sv_puppi", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_MTLt40",           cuts = [("nbtag>=1&&mt_1_puppi<40", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_MT40To70",         cuts = [("nbtag>=1&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
                    [mt_tot_hist]),
            # Control region.
            (Selection(name="MTGt70",                    cuts = [("mt_1_puppi>=70", "category_selection")]),
                    [mt_tot_hist]),
        ],
        "mt": [
            (Selection(name="emb",  cuts=[("mt_max_index=={index}".format(index=2), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [mt_hist]),
            (Selection(name="tt",   cuts=[("mt_max_index=={index}".format(index=3), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [mt_hist]),
            (Selection(name="misc", cuts=[("mt_max_index=={index}".format(index=4), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [mt_hist]),
            (Selection(name="zll",  cuts=[("mt_max_index=={index}".format(index=5), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [mt_hist]),
            (Selection(name="ff",   cuts=[("mt_max_index=={index}".format(index=6), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [mt_hist]),
            (Selection(name="xxh",  cuts=[("(mt_max_index=={index1}||mt_max_index=={index2})".format(index1=0, index2=1), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [Histogram("stxs_stage0_2Ddiscr", discr_str.format(channel="mt"), list(range(29)))]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0_MTLt40",             cuts = [("nbtag==0&&mt_1_puppi<40", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_MT40To70",           cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories
            (Selection(name="Nbtag0_MTLt40_MHGt250",     cuts = [("nbtag==0&&mt_1_puppi<40&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_MT40To70_MHGt250",   cuts = [("nbtag==0&&mt_1_puppi>=40&&mt_1_puppi<70&&m_sv_puppi", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_MTLt40",           cuts = [("nbtag>=1&&mt_1_puppi<40", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_MT40To70",         cuts = [("nbtag>=1&&mt_1_puppi>=40&&mt_1_puppi<70", "category_selection")]),
                    [mt_tot_hist]),
            # Control region.
            (Selection(name="MTGt70",                    cuts = [("mt_1_puppi>=70", "category_selection")]),
                    [mt_tot_hist]),
        ],
        "tt": [
            (Selection(name="emb",  cuts=[("tt_max_index=={index}".format(index=2), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [tt_hist]),
            (Selection(name="misc", cuts=[("tt_max_index=={index}".format(index=3), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [tt_hist]),
            (Selection(name="ff",   cuts=[("tt_max_index=={index}".format(index=4), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [tt_hist]),
            (Selection(name="xxh",  cuts=[("(tt_max_index=={index1}||tt_max_index=={index2})".format(index1=0, index2=1), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [Histogram("stxs_stage0_2Ddiscr", discr_str.format(channel="tt"), list(range(29)))]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0",                                    cuts=[("nbtag==0", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories.
            (Selection(name="Nbtag0_MHGt250",                            cuts=[("nbtag==0&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1",                                  cuts=[("nbtag>=1", "category_selection")]),
                    [mt_tot_hist]),
        ],
        "em": [
            (Selection(name="emb",  cuts=[("em_max_index=={index}".format(index=2), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [em_hist]),
            (Selection(name="tt",   cuts=[("em_max_index=={index}".format(index=3), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [em_hist]),
            (Selection(name="db",   cuts=[("em_max_index=={index}".format(index=4), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [em_hist]),
            (Selection(name="misc", cuts=[("em_max_index=={index}".format(index=5), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [em_hist]),
            (Selection(name="ss",   cuts=[("em_max_index=={index}".format(index=6), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [em_hist]),
            (Selection(name="xxh",  cuts=[("(em_max_index=={index1}||em_max_index=={index2})".format(index1=0, index2=1), "category_selection"),
                                         ("nbtag==0&&m_sv_puppi<250", "mssm_veto")]),
                    [Histogram("stxs_stage0_2Ddiscr", discr_str.format(channel="em"), list(range(29)))]),
            # Pure MSSM analysis categories.
            (Selection(name="Nbtag0_DZetam35Tom10",          cuts=[("nbtag==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetam10To30",           cuts=[("nbtag==0&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetaGt30",              cuts=[("nbtag==0&&pZetaPuppiMissVis>=30", "category_selection")]),
                    [mt_tot_hist]),
            # MSSM and SM analysis categories.
            (Selection(name="Nbtag0_DZetam35Tom10_MHGt250",  cuts=[("nbtag==0&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetam10To30_MHGt250",   cuts=[("nbtag==0&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="Nbtag0_DZetaGt30_MHGt250",      cuts=[("nbtag==0&&pZetaPuppiMissVis>=30&&m_sv_puppi>=250", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetam35Tom10",        cuts=[("nbtag>=1&&pZetaPuppiMissVis>=-35&&pZetaPuppiMissVis<-10", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetam10To30",         cuts=[("nbtag>=1&&pZetaPuppiMissVis>=-10&&pZetaPuppiMissVis<30", "category_selection")]),
                    [mt_tot_hist]),
            (Selection(name="NbtagGt1_DZetaGt30",            cuts=[("nbtag>=1&&pZetaPuppiMissVis>=30", "category_selection")]),
                    [mt_tot_hist]),
            # Control regions.
            (Selection(name="DZetaLtm35",                    cuts=[("pZetaPuppiMissVis<-35", "category_selection")]),
                    [mt_tot_hist]),
        ],
}
