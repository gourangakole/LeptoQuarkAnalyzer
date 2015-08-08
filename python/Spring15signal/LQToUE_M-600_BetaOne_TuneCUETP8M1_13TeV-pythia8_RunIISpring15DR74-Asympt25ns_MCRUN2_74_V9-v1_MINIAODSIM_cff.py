import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/2EF235EC-6D31-E511-BD81-000F53273650.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/E23A2113-6E31-E511-B32E-002590FD5A52.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0E5CF9A0-CD32-E511-9BFB-842B2B182385.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/3432D9B3-4733-E511-95BA-001E4F1B8E39.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/36972528-F832-E511-833F-D4AE526A11F3.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/4E5F4F97-E733-E511-AB30-00304867FD63.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/565BB927-0D33-E511-93E3-008CFA0648E0.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/720C6535-1833-E511-952B-001E6878FB21.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/B84D559A-CD32-E511-95FA-000F532734B4.root' ] );


secFiles.extend( [
               ] )
