import FWCore.ParameterSet.Config as cms

particleFlowRecHitHGCEE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string("PFRecHitHGCEENavigator"),
        topologySource = cms.string("HGCalEESensitive"),
    ),
    producers = cms.VPSet(
           cms.PSet(
             name = cms.string("PFHGCEERecHitCreator"),
             src  = cms.InputTag("HGCalRecHit:HGCEERecHits"),
             geometryInstance = cms.string("HGCalEESensitive"),
             qualityTests = cms.VPSet( 
                cms.PSet(
                  name = cms.string("PFRecHitQTestThresholdInMIPs"),
                  thresholdInMIPs = cms.double(0.40),
                  mipValueInkeV = cms.double(55.1),
                  recHitEnergyIs_keV = cms.bool(True),
                  recHitEnergyMultiplier = cms.double(12.0)
                  ),
                )
           )          
    )          
)
