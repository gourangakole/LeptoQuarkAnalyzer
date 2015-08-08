import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/1E39F2C3-272F-E511-94C7-008CFA05E88C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/62B3C2F8-272F-E511-93BC-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/30000/AEB620F0-282F-E511-AEF0-00261894397B.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/401A110E-2237-E511-8644-00304865C2E8.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/B2A32E09-2237-E511-81A9-002590D9D8AA.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0660B96B-6D2F-E511-BD94-002618943981.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/2280CD0B-1E2F-E511-8021-20CF3019DF19.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/5211646C-FE31-E511-B69D-008CFA110C6C.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7EE56571-6D2F-E511-A590-0025905A6070.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8E994D5B-002F-E511-8979-001EC9AF1FF1.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/9A2EA07C-A02E-E511-97B1-0002C94CD310.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B47D9742-332F-E511-83AA-02163E00E7A0.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E8F11479-A02E-E511-8931-0002C90A340C.root' ] );


secFiles.extend( [
               ] )
