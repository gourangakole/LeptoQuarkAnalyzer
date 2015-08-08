import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-900_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/6CE3B6A3-FC03-E511-97AA-0025905B85EE.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-900_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/96E2DD2A-FD03-E511-8F21-842B2B768127.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-900_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/EEB44864-FC03-E511-8E9F-0025905A6094.root' ] );


secFiles.extend( [
               ] )
