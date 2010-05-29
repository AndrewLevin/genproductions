import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.untracked.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  libDir    = cms.untracked.string('SherpaRun'),
  resultDir = cms.untracked.string('Result'),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "Run"),
                              Run = cms.vstring(
				"(run){",
				" EVENTS          = 10000",
				" NUM_ACCURACY    = 1.e-10",
				" OUTPUT          = 2",
				" ANALYSIS        = 1",
				" EVENT_MODE      = HepMC",
				" RANDOM_SEED     = 15732 27621",
				"}(run)",
				"(beam){",
				" BEAM_1             = 2212",
				" BEAM_ENERGY_1      = 3500.",
				" BEAM_POL_1         = 0.",
				" BEAM_SPECTRUM_1    = Monochromatic",
				" K_PERP_MEAN_1      = 0.2",
				" K_PERP_SIGMA_1     = 0.8",
				" BEAM_2             = 2212",
				" BEAM_ENERGY_2      = 3500.",
				" BEAM_POL_2         = 0.",
				" BEAM_SPECTRUM_2    = Monochromatic",
				" K_PERP_MEAN_2      = 0.2",
				" K_PERP_SIGMA_2     = 0.8",
				" BEAM_SMIN          = 1.e-10",
				" BEAM_SMAX          = 1.0",
				" E_LASER_1          = 1.17e-9",
				" P_LASER_1          = 0.",
				" E_LASER_2          = 1.17e-9",
				" P_LASER_2          = 0.",
				" LASER_MODE         = 0",
				" LASER_ANGLES       = Off",
				" LASER_NONLINEARITY = On",
				"}(beam)",
				"(isr){",
				" BUNCH_1         = 2212",
				" ISR_1           = On",
				" BUNCH_2         = 2212",
				" ISR_2           = On",
				" ISR_SMIN        = 1.e-10",
				" ISR_SMAX        = 1.0",
				" ISR_E_ORDER     = 1",
				" ISR_E_SCHEME    = 2",
				" PDF_SET         = cteq6ll.LHpdf",
				" PDF_SET_VERSION = 1",
				" PDF_GRID_PATH   = PDFsets",
				"}(isr)",
				"(model){",
				" MODEL                 = ADD",
				" EW_SCHEME             = 0",
				" ALPHAS(MZ)            = 0.118",
				" ALPHAS(default)       = 0.0800",
				" ORDER_ALPHAS          = 1",
				" 1/ALPHAQED(0)         = 137.036",
				" 1/ALPHAQED(default)   = 132.51",
				" SIN2THETAW            = 0.2222",
				" VEV                   = 246.",
				" LAMBDA                = 0.47591",
				" CKMORDER              = 0",
				" CABIBBO               = 0.22",
				" A                     = 0.85",
				" RHO                   = 0.50",
				" ETA                   = 0.50",
				" SLHA_INPUT            = LesHouches_SPS1A.dat",
				" N_ED                  = 2",
				" G_NEWTON              = 6.707e-39",
				" M_S                   = 1.0e3",
				" M_CUT                 = 1.0e3",
				" KK_CONVENTION         = 5",
				" STABLE[15]=0",
				"}(model)",
				"(me){",
				" ME_SIGNAL_GENERATOR   = Amegic",
				" EVENT_GENERATION_MODE = Unweighted",
				" COUPLING_SCHEME       = Running_alpha_S",
				" YUKAWA_MASSES         = Fixed",
				" YUKAWA_MASSES_FACTOR  = 1.",
				" SCALE_SCHEME          = CKKW",
				" KFACTOR_SCHEME        = 1",
				" SUDAKOV_WEIGHT        = 1",
				" SCALE_FACTOR          = 1.",
				"}(me)",
				"(integration){",
				" ERROR =  1.e-2",
				" FINISH_OPTIMIZATION = On",
				" INTEGRATOR = 6",
				" VEGAS = On",
				"}(integration)",
				"(mi){",
				" MI_HANDLER   = Amisic",
				" CREATE_GRID 93 93 -> 93 93",
				" PS_ERROR            = 1.0e-2",
				" REGULATE_XS         = 0",
				" XS_REGULATION       = 2.225",
				" SCALE_MIN           = 2.225",
				" RESCALE_EXPONENT    = 0.16",
				" REFERENCE_SCALE     = 1800.0",
				" PROFILE_FUNCTION    = Gaussian",
				" PROFILE_PARAMETERS  = 1.0 0.5 0.5",
				"}(mi)",
				"(shower){",
				" SHOWER_GENERATOR  = Apacic",
				" FSR_SHOWER        = 1",
				" ISR_SHOWER        = 1",
				" IS_PT2MIN         = 4.",
				" FS_PT2MIN         = 1.",
				"}(shower)",
				"(fragmentation){",
				" FRAGMENTATION = Ahadic",
				" DECAYMODEL    = Hadrons",
				" YFS_MODE       = 2",
				" YFS_USE_ME     = 1",
				" YFS_IR_CUTOFF  = 1E-3",
				"}(fragmentation)",
				"(processes){",
				" Process : 93 93 -> 39 93",
				" End process",
				"}(processes)",
				"(selector){",
				" JetFinder   sqr(20/E_CMS) 1.",
				" ET 93 50 1000000",
				"}(selector)"
                                                  ),
                             )
)
