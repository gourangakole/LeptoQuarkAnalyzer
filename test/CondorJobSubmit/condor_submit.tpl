universe = vanilla
Executable            = run_<JOBNAME>_<INDEX>.sh
x509userproxy = <PROXY>
Requirements          = Memory >= 199 &&OpSys == "LINUX"&& (Arch != "DUMMY" )&& Disk > 1000000
Should_Transfer_Files = YES
transfer_input_files=../Config_analyzer.py,../commandLineParameters.py,../../../../TreeMaker/TreeMaker/test/PHYS14_V4_MC.db
WhenToTransferOutput  = ON_EXIT_OR_EVICT
Output = out_<JOBNAME>_$(Cluster).stdout
Error  = out_<JOBNAME>_$(Cluster).stderr
Log    = out_<JOBNAME>_$(Cluster).log
Notification    = Error
notify_user     = bmahakud@cern.ch
Queue 1
