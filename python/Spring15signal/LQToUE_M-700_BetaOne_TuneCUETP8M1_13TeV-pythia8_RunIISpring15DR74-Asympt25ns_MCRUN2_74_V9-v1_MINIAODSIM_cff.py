import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-700_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/647DBF46-3434-E511-AEFD-00259048A87C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-700_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F4EADE07-9E32-E511-920D-B499BAAC055E.root' ] );


secFiles.extend( [
               ] )
