#!/usr/bin/env python

import json
import sys
import os

# print usage
if len(sys.argv)<2:
   print "usage: bankSplit.py coatjavahipobankfolder (e.g. coatjava/etc/bankdefs/hipo4/)"
   sys.exit()

# hipo schema directory
hipodirectory = sys.argv[1] +  "/"
os.chdir(hipodirectory)

# single jsons directory
workdirectory   = "singles/"
singledirectory = "full/"
os.mkdir(workdirectory)	    
os.mkdir(workdirectory + singledirectory)	    

# create schema directory
def createdirandlinks(dirname, banklist):
    os.mkdir(workdirectory + dirname)
    os.chdir(workdirectory + dirname)
    for bank in banklist:
        os.symlink("../" + singledirectory + bank + ".json", bank + ".json")
    os.chdir("../../")
    print("Json file links created in " + workdirectory + dirname)

    
# for each json file in hipo schema folder
for filename in os.listdir("./"):
    if filename.endswith(".json"):
		
        #Read JSON data into the datastore variable
        f = open(filename)
        try:
            datastore = json.load(f)
        except:
            print 'Invalid JSON:  '+filename
            sys.exit(1)
        # loop over banks in the json file
	for bank in datastore:
	    bankname = bank['name']
	    file = open(workdirectory + singledirectory + bankname + ".json", 'w')
	    file.write(json.dumps([bank], sort_keys=True, indent=4))
	    file.close
print("Single json files saved in " + workdirectory + singledirectory)

# create dst, calibration and monitoring directories
# copy the file from coatjava6b.1.1 defined at https://github.com/JeffersonLab/clas12-offline-software/blob/6b.1.1/etc/bankdefs/util/bankSplit.py
#new dst schema will add "BAND::adc","BAND::tdc","BAND::hits","CND::hits","RAW::epics","HEL::online",
#new calib schema will add "RAW::epics","HEL::online"
#new mon schema will add "RAW::epics","HEL::online","HEL::adc"

#dst = ["RUN::config","RAW::scaler","REC::Event","REC::Particle","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::ForwardTagger","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RICH::tdc","RUN::scaler","HEL::flip","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True"]
dst = ["BAND::adc","BAND::tdc","BAND::hits","CND::hits","RAW::epics","HEL::online","RUN::config","RAW::scaler","REC::Event","REC::Particle","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::ForwardTagger","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RICH::tdc","RUN::scaler","HEL::flip","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True"]
#calibration = ["BAND::adc","BAND::tdc","BAND::hits","CND::adc","CND::hits","CND::tdc","CTOF::adc","CTOF::hits","CTOF::tdc","CVTRec::Tracks","ECAL::adc","ECAL::calib","ECAL::clusters","ECAL::peaks","ECAL::tdc","FT::particles","FTCAL::adc","FTCAL::clusters","FTCAL::hits","FTHODO::adc","FTHODO::clusters","FTHODO::hits","FTOF::adc","FTOF::hits","FTOF::tdc","HEL::flip","HTCC::adc","HTCC::rec","LTCC::adc","LTCC::clusters","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True","RAW::scaler","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::Event","REC::ForwardTagger","REC::Particle","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RF::adc","RF::tdc","RICH::tdc","RUN::config","RUN::rf","RUN::scaler","RUN::trigger","TimeBasedTrkg::TBCrosses","TimeBasedTrkg::TBHits","TimeBasedTrkg::TBSegments","TimeBasedTrkg::TBSegmentTrajectory","TimeBasedTrkg::TBTracks","TimeBasedTrkg::Trajectory"]
calibration = ["RAW::epics","HEL::online","BAND::adc","BAND::tdc","BAND::hits","CND::adc","CND::hits","CND::tdc","CTOF::adc","CTOF::hits","CTOF::tdc","CVTRec::Tracks","ECAL::adc","ECAL::calib","ECAL::clusters","ECAL::peaks","ECAL::tdc","FT::particles","FTCAL::adc","FTCAL::clusters","FTCAL::hits","FTHODO::adc","FTHODO::clusters","FTHODO::hits","FTOF::adc","FTOF::hits","FTOF::tdc","HEL::flip","HTCC::adc","HTCC::rec","LTCC::adc","LTCC::clusters","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True","RAW::scaler","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::Event","REC::ForwardTagger","REC::Particle","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RF::adc","RF::tdc","RICH::tdc","RUN::config","RUN::rf","RUN::scaler","RUN::trigger","TimeBasedTrkg::TBCrosses","TimeBasedTrkg::TBHits","TimeBasedTrkg::TBSegments","TimeBasedTrkg::TBSegmentTrajectory","TimeBasedTrkg::TBTracks","TimeBasedTrkg::Trajectory"]
#monitoring = ["BAND::adc","BAND::tdc","BAND::hits","BMT::adc","BMTRec::Clusters","BMTRec::Crosses","BMTRec::Hits","BMTRec::LayerEffs","BST::adc","BSTRec::Clusters","BSTRec::Crosses","BSTRec::Hits","BSTRec::LayerEffs","CND::adc","CND::clusters","CND::hits","CND::tdc","CTOF::adc","CTOF::hits","CTOF::tdc","CVTRec::Tracks","CVTRec::Trajectory","ECAL::adc","ECAL::calib","ECAL::clusters","ECAL::hits","ECAL::peaks","ECAL::tdc","FT::particles","FTCAL::adc","FTCAL::clusters","FTCAL::hits","FTHODO::adc","FTHODO::clusters","FTHODO::hits","FTOF::adc","FTOF::hits","FTOF::tdc","HEL::flip","HitBasedTrkg::HBTracks","HTCC::adc","HTCC::rec","LTCC::adc","LTCC::clusters","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True","RAW::scaler","RAW::vtp","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::Event","REC::ForwardTagger","REC::Particle","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RECHB::Calorimeter","RECHB::Cherenkov","RECHB::Event","RECHB::ForwardTagger","RECHB::Particle","RECHB::Scintillator","RECHB::Track","RF::adc","RF::tdc","RICH::tdc","RUN::config","RUN::rf","RUN::scaler","RUN::trigger","TimeBasedTrkg::TBCrosses","TimeBasedTrkg::TBHits","TimeBasedTrkg::TBSegments","TimeBasedTrkg::TBSegmentTrajectory","TimeBasedTrkg::TBTracks","TimeBasedTrkg::Trajectory"]
"BMTRec::Hits, BSTRec::Hits, BMTRec::LayerEffs, and BSTRec::LayerEffs"
monitoring = ["RAW::epics","HEL::online","HEL::adc","BAND::adc","BAND::tdc","BAND::hits","BMT::adc","BMTRec::Clusters","BMTRec::Crosses","BMTRec::Hits","BMTRec::LayerEffs","BST::adc","BSTRec::Clusters","BSTRec::Crosses","BSTRec::Hits","BSTRec::LayerEffs","CND::adc","CND::clusters","CND::hits","CND::tdc","CTOF::adc","CTOF::hits","CTOF::tdc","CVTRec::Tracks","CVTRec::Trajectory","ECAL::adc","ECAL::calib","ECAL::clusters","ECAL::hits","ECAL::peaks","ECAL::tdc","FT::particles","FTCAL::adc","FTCAL::clusters","FTCAL::hits","FTHODO::adc","FTHODO::clusters","FTHODO::hits","FTOF::adc","FTOF::hits","FTOF::tdc","HEL::flip","HitBasedTrkg::HBTracks","HTCC::adc","HTCC::rec","LTCC::adc","LTCC::clusters","MC::Event","MC::Header","MC::Lund","MC::Particle","MC::True","RAW::scaler","RAW::vtp","REC::Calorimeter","REC::Cherenkov","REC::CovMat","REC::Event","REC::ForwardTagger","REC::Particle","REC::Scintillator","REC::Track","REC::Traj","RECFT::Event","RECFT::Particle","RECHB::Calorimeter","RECHB::Cherenkov","RECHB::Event","RECHB::ForwardTagger","RECHB::Particle","RECHB::Scintillator","RECHB::Track","RF::adc","RF::tdc","RICH::tdc","RUN::config","RUN::rf","RUN::scaler","RUN::trigger","TimeBasedTrkg::TBCrosses","TimeBasedTrkg::TBHits","TimeBasedTrkg::TBSegments","TimeBasedTrkg::TBSegmentTrajectory","TimeBasedTrkg::TBTracks","TimeBasedTrkg::Trajectory"]
createdirandlinks("dst/", dst)
createdirandlinks("calibration/", calibration)
createdirandlinks("monitoring/",  monitoring)
    

