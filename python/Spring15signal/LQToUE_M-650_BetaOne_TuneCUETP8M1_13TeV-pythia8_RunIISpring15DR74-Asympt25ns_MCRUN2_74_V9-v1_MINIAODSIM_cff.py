import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/08B1C5D1-E230-E511-B4E9-002590D9D894.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/2A2058FF-2330-E511-B142-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/463E51ED-1531-E511-8E91-00A0D1EE271C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/8060C6B5-4530-E511-883A-3417EBE64561.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/E6CFFD9B-0631-E511-94C8-003048F5970A.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/505689EF-5530-E511-9335-00266CF9ADA0.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/C2BABDE6-952F-E511-A4A4-0025901ABD2E.root' ] );


secFiles.extend( [
               ] )
