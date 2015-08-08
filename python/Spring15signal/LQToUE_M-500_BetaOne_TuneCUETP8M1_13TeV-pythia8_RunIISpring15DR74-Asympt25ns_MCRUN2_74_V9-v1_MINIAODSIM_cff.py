import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/6AD57365-492F-E511-9740-00259074AE7E.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/FCA23DC3-492F-E511-9B88-0025907DC9D6.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/288F85F2-5A2F-E511-BD9E-002590D4FC42.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/84DAB16E-5B2F-E511-B6AB-0025905A6090.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/B8ABB871-5B2F-E511-9A1A-6CC2173BB810.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/BC7A8419-5B2F-E511-836A-02163E0133A4.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/EE0A376D-5B2F-E511-9CC2-B499BAAC02CA.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/70EF4A54-D22E-E511-AEC7-D4AE526A1687.root' ] );


secFiles.extend( [
               ] )
