import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/06CEF839-EB03-E511-8F7C-00266CFCC23C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/647C5E13-EB03-E511-A8E7-0025905B861C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8024C123-EB03-E511-86AA-0025905A608E.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/9A2C5A4A-EB03-E511-A4C5-D4AE526A0455.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A65C027F-EB03-E511-A672-782BCB67826E.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/CC70344A-EB03-E511-A722-0CC47A4D9A42.root' ] );


secFiles.extend( [
               ] )

