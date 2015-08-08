import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/787ED7C1-272F-E511-AD33-008CFA0A5A10.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/E2201423-282F-E511-AA93-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/2AC39C33-0533-E511-B29D-00259075D6B4.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1ABDD78B-6D2F-E511-BCC3-0025905A48D0.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1EC8EA8C-6D2F-E511-9378-0025905B8582.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A0501B26-802F-E511-8694-F45214C748D0.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/BE79BC4A-D32E-E511-869D-842B2B7680A2.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/BE918946-332F-E511-88A6-001E675825D4.root' ] );


secFiles.extend( [
               ] )
