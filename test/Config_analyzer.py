import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

process = cms.Process("analysis")


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery


## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

###############
# tree maker
###############

from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
                    outfile="ReducedSelection",
                    reportfreq=50,
                    dataset="file:/uscms_data/d3/bmahakud/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola_MINIAODSIM_PU20bx25_PHYS14_25_V1-v1.root",
                    globaltag="PHYS14_25_V2::All",
                    lostlepton=False,
                    numevents=500,
                    tagname="PAT",
                    geninfo=True,
                    jsonfile="",
                    applyjec=False

                    )

