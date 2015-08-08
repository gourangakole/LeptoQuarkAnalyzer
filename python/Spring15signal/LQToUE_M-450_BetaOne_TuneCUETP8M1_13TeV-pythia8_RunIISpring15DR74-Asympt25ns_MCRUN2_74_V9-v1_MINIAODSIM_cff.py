import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/3ED68E76-A108-E511-8092-842B2B7680A2.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/26DF4CBC-E308-E511-929A-0002C94D54CC.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3C78D8CE-EB08-E511-84DF-002590D9D9FC.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4009CF4F-5308-E511-885B-008CFA197C10.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4AEA9E88-C407-E511-8185-001EC9AE27F4.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/726CCAA6-ED08-E511-AD10-008CFA1CBA20.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7E234071-A408-E511-92C5-D4AE526A0B29.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/86C7B23D-5A08-E511-BF4C-28924A38DC1E.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9CB1BBC3-B608-E511-A9E6-B083FED03632.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B805AF16-4208-E511-A268-002590D6004A.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B80B23D3-B008-E511-AC3C-6C3BE5B58058.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E4871AB5-3E08-E511-ACF5-842B2B42D35D.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F04822B6-9F08-E511-8AAA-001E675050FD.root',
       '/store/mc/RunIISpring15DR74/LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC44B667-ED08-E511-9BBC-0002C94CDA06.root' ] );


secFiles.extend( [
               ] )

