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
                    dataset="file:/afs/cern.ch/user/b/bmahakud/public/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola_MINIAODSIM_PU20bx25_PHYS14_25_V1-v1.root",
                    globaltag="PHYS14_25_V2::All",
                    lostlepton=False,
                    numevents=500,
                    tagname="PAT",
                    geninfo=True,
                    jsonfile="",
                    applyjec=False

                    )

process.TreeMaker2.VectorRecoCand       = cms.vstring() 
process.TreeMaker2.VarsDouble           = cms.vstring()
process.TreeMaker2.VarsInt              = cms.vstring()
process.TreeMaker2.VarsBool             = cms.vstring()
process.TreeMaker2.VectorTLorentzVector = cms.vstring()
process.TreeMaker2.VectorDouble         = cms.vstring()
process.TreeMaker2.VectorString         = cms.vstring()
process.TreeMaker2.VectorInt            = cms.vstring()
process.TreeMaker2.VectorBool           = cms.vstring()

###  - - - - - - - - Lepton stuff - - - - - - - 

process.LeptonsNewTag.minElecPt        = cms.double(35)
process.LeptonsNewTag.maxElecEta       = cms.double(2.5)
process.LeptonsNewTag.minMuPt          = cms.double(10)
process.LeptonsNewTag.maxMuEta         = cms.double(2.4)
process.LeptonsNewTag.UseMiniIsolation = cms.bool(True)
process.LeptonsNewTag.muIsoValue       = cms.double(0.2)
process.LeptonsNewTag.elecIsoValue     = cms.double(0.1) # only has an effect when used with miniIsolation

process.TreeMaker2.VarsInt.extend(['LeptonsNew(Leptons)'])
process.TreeMaker2.VectorRecoCand.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])
process.TreeMaker2.VectorInt.extend(['LeptonsNew:MuonCharge(MuonCharge)','LeptonsNew:ElectronCharge(ElectronCharge)'])

###  - - - - - - - - Jet stuff - - - - - - - 

process.GoodJets.maxJetEta                 = cms.double(2.4)
process.GoodJets.maxMuFraction             = cms.double(2)
process.GoodJets.minNConstituents          = cms.double(2)
process.GoodJets.maxNeutralFraction        = cms.double(0.90)
process.GoodJets.maxPhotonFraction         = cms.double(0.95)
process.GoodJets.minChargedMultiplicity    = cms.double(0)
process.GoodJets.minChargedFraction        = cms.double(0)
process.GoodJets.maxChargedEMFraction      = cms.double(0.99)
process.GoodJets.jetPtFilter               = cms.double(45)
process.GoodJets.ExcludeLepIsoTrackPhotons = cms.bool(True)
process.GoodJets.JetConeSize               = cms.double(0.3)
process.GoodJets.MuonTag                   = cms.InputTag('LeptonsNew:IdIsoMuon')
process.GoodJets.ElecTag                   = cms.InputTag('LeptonsNew:IdIsoElectron')

process.TreeMaker2.VarsBool.extend(['GoodJets(JetID)'])
process.TreeMaker2.VectorRecoCand.extend(['GoodJets(Jets)'])

process.TreeMaker2.VectorDouble.extend(['JetsProperties:bDiscriminatorUser(Jets_bDiscriminatorCSV)',
                                            'JetsProperties:bDiscriminatorMVA(Jets_bDiscriminatorMVA)',
                                            'JetsProperties:chargedEmEnergyFraction(Jets_chargedEmEnergyFraction)',
                                            'JetsProperties:chargedHadronEnergyFraction(Jets_chargedHadronEnergyFraction)',
                                            'JetsProperties:jetArea(Jets_jetArea)',
                                            'JetsProperties:muonEnergyFraction(Jets_muonEnergyFraction)',
                                            'JetsProperties:neutralEmEnergyFraction(Jets_neutralEmEnergyFraction)',
                                            'JetsProperties:photonEnergyFraction(Jets_photonEnergyFraction)'])
process.TreeMaker2.VectorInt.extend(['JetsProperties:chargedHadronMultiplicity(Jets_chargedHadronMultiplicity)',
                                         'JetsProperties:electronMultiplicity(Jets_electronMultiplicity)',
                                         'JetsProperties:muonMultiplicity(Jets_muonMultiplicity)',
                                         'JetsProperties:neutralHadronMultiplicity(Jets_neutralHadronMultiplicity)',
                                         'JetsProperties:photonMultiplicity(Jets_photonMultiplicity)',
                                         'JetsProperties:flavor(Jets_flavor)'])

###  - - - - - - - - Event Filter stuff - - - - - - - 
process.TreeMaker2.VarsInt.extend(['METFilters'])
process.TreeMaker2.VarsInt.extend(['CSCTightHaloFilter'])
process.TreeMaker2.VarsInt.extend(['HBHENoiseFilter'])
process.TreeMaker2.VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])

###  - - - - - - - - Event Filter stuff - - - - - - - 

process.TriggerProducer.triggerNameList = cms.vstring( 'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v' )

process.TreeMaker2.VectorBool.extend(['TriggerProducer:TriggerPass'])
process.TreeMaker2.VectorInt.extend(['TriggerProducer:TriggerPrescales'])
process.TreeMaker2.VectorString.extend(['TriggerProducer:TriggerNames'])

###  - - - - - - - - Path stuff - - - - - - - 

process.Path = cms.Path( 
                        process.LeptonsNew *
                        process.GoodJets *
                        
                        process.METFilters *
                        process.CSCTightHaloFilter *
                        process.HBHENoiseFilter * 
                        process.EcalDeadCellTriggerPrimitiveFilter *

                        process.TriggerProducer *
                        
                        process.TreeMaker2
                        ) 



