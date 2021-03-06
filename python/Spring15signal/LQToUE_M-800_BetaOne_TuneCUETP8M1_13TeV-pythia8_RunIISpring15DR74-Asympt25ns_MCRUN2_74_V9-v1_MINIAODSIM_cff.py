import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-800_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/66868B7E-3704-E511-AD57-E0CB4E29C504.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-800_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/A2DA376A-3704-E511-98D3-0025905A6134.root' ] );


secFiles.extend( [
               ] )


