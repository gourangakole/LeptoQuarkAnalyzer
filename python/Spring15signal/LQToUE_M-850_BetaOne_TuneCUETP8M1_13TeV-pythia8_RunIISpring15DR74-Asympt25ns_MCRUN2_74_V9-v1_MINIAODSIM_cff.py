import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/20A1861D-8704-E511-88FA-00259073E4F4.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/24BF2A20-8704-E511-A9F1-BCAEC528225F.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/266C3F2F-8704-E511-91B2-00266CFC3B0C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/48E36CA0-8604-E511-89E7-002590A4FFA2.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/58253306-8604-E511-9462-0025907B50CA.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/82401A9D-8604-E511-B346-90B11C2AB44B.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/8E04AA1E-8704-E511-93AB-0002C94CDAF4.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/9E463520-8A04-E511-BD11-0026B9278692.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/D45AB94F-8704-E511-B96D-0CC47A0107D0.root' ] );


secFiles.extend( [
               ] )
