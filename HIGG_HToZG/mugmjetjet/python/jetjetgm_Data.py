
# coding: utf-8

# In[1]:


class jetjetgm_Data(object):
    def __init__(self, folderFile='',nameFile='',trigger='',data=False,flag=False):
        self.folder = folderFile
        self.name = nameFile
        self.trigger = trigger
        self.data = data
        self.flag = flag
        
        self.Topo = jetjetgm_Topology()
        self.Help = jetjetgm_Helper()
        
        self.weights = None
        self.eventWeight = []
        self.genWeight   = []
        self.cuts = []
        
        if data:
            print('----------------- DATA --------------------------')
            print('Opening    tree::'   +"   tree_" + self.name + self.trigger)
            print('Opening Gentree::'   +"Gentree_" + self.name + self.trigger)
            print('Opening Bugtree::'   +"Bugtree_" + self.name + self.trigger)
            print('-------------------------------------------------')
            
            self.file = TFile(folderFile + "output_" + self.name +"_v.root",'read')
                              #self.name + self.trigger +"_v.root",'read')
            self.tree    = self.file.Get("tree_" + self.name + self.trigger)
            self.gentree = self.file.Get("Gentree_" + self.name + self.trigger)
            self.bugtree = self.file.Get("Bugtree_" + self.name + self.trigger)
        else :
            if flag:
                print('-------------------- MC -----------------------')
                print('Opening    File::' + folderFile + "output_" + self.name + self.trigger + "_0.root")
                print('Opening    tree::' + "   tree_" + self.name + self.trigger)           
                print('Opening Gentree::' + "Gentree_" + self.name + self.trigger)
                print('Opening Bugtree::' + "Bugtree_" + self.name + self.trigger)
                print('-----------------------------------------------')            
                
                self.file    = TFile(folderFile + "output_" + self.name + self.trigger + "_0.root",'read')
                self.tree    = self.file.Get("tree_" + self.name + self.trigger)
                self.gentree = self.file.Get("Gentree_" + self.name + self.trigger)
                self.bugtree = self.file.Get("Bugtree_" + self.name + self.trigger)            
            else :
                print('-------------------- MC -----------------------')
                print('Opening    File::' + folderFile + "output_" + self.name + self.trigger + "_0.root")
                print('Opening    tree::' + "   tree_" + self.name.lower())# + self.trigger)
                print('Opening Gentree::' + "Gentree_" + self.name.lower())# + self.trigger)
                print('Opening Bugtree::' + "Bugtree_" + self.name.lower())# + self.trigger)
                print('-----------------------------------------------')            
                
                self.file    = TFile(folderFile + "output_" + self.name + self.trigger + "_0.root",'read')
                self.tree    = self.file.Get("tree_" + self.name.lower()) #+ self.trigger)
                self.gentree = self.file.Get("Gentree_" + self.name.lower() )#+ self.trigger)
                self.bugtree = self.file.Get("Bugtree_" + self.name.lower() )#+ self.trigger)

        self.TotalEventBin = 31       
        self.TotalEvent    = [0 for _ in range(self.TotalEventBin)]
        self.TotalEvent_SF = [0 for _ in range(self.TotalEventBin)]
        self.numEvents     = 0
        #------------------------------------------------------------ Multiplicity
        self.nElectrons      =  []
        self.nMuons          =  []
        self.nBJets          =  []
        self.nJets           =  []
        self.nPV             =  []
        #------------------------------------------------------------ M
        self.lepton_m        =  []
        self.photon_m        =  []
        self.jet1_m          =  []
        self.jet2_m          =  []

        self.dilep_m         =  []
        self.dilepgm_m       =  []

        self.dijet_m         =  []
        self.dijetgm_m       =  []
        #------------------------------------------------------------ E
        self.lepton_E        =  []
        self.photon_E        =  []
        self.jet1_E          =  []
        self.jet2_E          =  []

        self.dilep_E         =  []
        self.dilepgm_E       =  []

        self.dijet_E         =  []
        self.dijetgm_E       =  []
        #------------------------------------------------------------ PT
        self.photon_pt       =  []
        self.lepton_pt       =  []
        #self.muon1_pt        =  []
        #self.muon2_pt        =  []
        self.jet1_pt         =  []
        self.jet2_pt         =  []

        self.dilep_pt        =  []
        self.dilepgm_pt      =  []
        self.dijet_pt        =  []
        self.dijetgm_pt      =  []
        #------------------------------------------------------------ ETA
        self.photon_eta      =  []
        self.lepton_eta      =  []
        #self.muon1_eta       =  []
        #self.muon2_eta       =  []
        self.jet1_eta        =  []
        self.jet2_eta        =  []

        self.dilep_eta       =  []
        self.dilepgm_eta     =  []
        self.dijet_eta       =  []
        self.dijetgm_eta     =  []
        #------------------------------------------------------------ PHI
        self.photon_phi      =  []
        self.lepton_phi      =  []
        #self.muon1_phi       =  []
        #self.muon2_phi       =  []
        self.jet1_phi        =  []
        self.jet2_phi        =  []

        self.dilep_phi       =  []
        self.dilepgm_phi     =  []
        self.dijet_phi       =  []
        self.dijetgm_phi     =  []
        #------------------------------------------------------------ MT2
        self.lep1_Mt2        =  []
        #------------------------------------------------------------ MET
        self.MET             =  []
        self.MET_phi         =  []
        self.Mt              =  []
        self.ht              =  []
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        self.dilep_D_eta     =  []

        self.dilep_gm_D_eta  =  []
        self.dijet_D_eta     =  []

        self.MuGm_D_eta      =  []
        self.MuGm_D_eta      =  []
        self.dijet_D_eta     =  []
        self.Jet1Gm_D_eta    =  []
        self.Jet2Gm_D_eta    =  []
        self.Jet1Mu_D_eta    =  []
        self.Jet2Mu_D_eta    =  []
        
        #------More Variables
        self.dijet_gm_D_eta  =  [] 
        self.dijet_lep_D_eta =  [] 
        self.dijetgm_lep_D_eta = []
        
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        self.dilep_D_phi     =  []

        self.dilep_gm_D_phi  =  []
        self.dijet_D_phi     =  []

        self.MuGm_D_phi      =  []
        self.MuGm_D_phi      =  []
        self.dijet_D_phi     =  []
        self.Jet1Gm_D_phi    =  []
        self.Jet2Gm_D_phi    =  []
        self.Jet1Mu_D_phi    =  []
        self.Jet2Mu_D_phi    =  []
        
        #------More Variables
        self.dijet_gm_D_phi  =  [] 
        self.dijet_lep_D_phi =  []
        self.dijetgm_lep_D_phi = []
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        self.dilep_D_R       =  []

        self.dijet_D_R       =  []
        self.MuGm_D_R        =  []
        self.Jet1Gm_D_R      =  []
        self.Jet2Gm_D_R      =  []
        self.Jet1Mu_D_R      =  []
        self.Jet2Mu_D_R      =  []
        
        #------More Variables
        self.dijet_gm_D_R    =  [] 
        self.dijet_lep_D_R   =  [] 
        self.dijetgm_lep_D_R = []
        #------------------------------------------------------------ Jets
        
        #-------------------
        #------- GEN -------
        #-------------------
        self.genlepton_m     =  []
        self.genphoton_m     =  []
        self.genlepton_m     =  []
        self.genjet1_m       =  []
        self.genjet2_m       =  []

        self.digenjet_m      =  []
        self.digenjetgm_m    =  []
        #------------------------------------------------------------ PT
        self.genphoton_pt    =  []
        self.genlepton_pt    =  []
        self.genjet1_pt      =  []
        self.genjet2_pt      =  []

        self.digenjet_pt     =  []
        self.digenjetgm_pt   =  []
        #------------------------------------------------------------ ETA
        self.genphoton_eta   =  []
        self.genlepton_eta   =  []
        self.genjet1_eta     =  []
        self.genjet2_eta     =  []

        self.digenjet_eta    =  []
        self.digenjetgm_eta  =  []
        #------------------------------------------------------------ PHI
        self.genphoton_phi   =  []
        self.genlepton_phi   =  []
        self.genjet1_phi     =  []
        self.genjet2_phi     =  []

        self.digenjet_phi    =  []
        self.digenjetgm_phi  =  []
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        self.genMuGm_D_eta   =  []
        self.digenjet_D_eta  =  []
        self.genJet1Gm_D_eta =  []
        self.genJet2Gm_D_eta =  []
        self.genJet1Mu_D_eta =  []
        self.genJet2Mu_D_eta =  []
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        self.genMuGm_D_phi   =  []
        self.digenjet_D_phi  =  []
        self.genJet1Gm_D_phi =  []
        self.genJet2Gm_D_phi =  []
        self.genJet1Mu_D_phi =  []
        self.genJet2Mu_D_phi =  []
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        self.digenjet_D_R    =  []
        self.genMuGm_D_R     =  []
        self.genJet1Gm_D_R   =  []
        self.genJet2Gm_D_R   =  []
        self.genJet1Mu_D_R   =  []
        self.genJet2Mu_D_R   =  []   
        
    def _assign(self, Tree):
        self.eventWeight    .append(Tree.eventWeight)
        self.genWeight      .append(Tree.genWeight)
        #------------------------------------------------------------ Cut Flow
        for i in range(self.TotalEventBin):
            self.TotalEvent[i]    = self.TotalEvents(i)
            self.TotalEvent_SF[i] = self.TotalEvents(i)*self.ScaleFactor()*self.eventWeight[-1]*self.genWeight[-1]
        #------------------------------------------------------------ Add Cut 
        self.cuts           .append(True)
        #------------------------------------------------------------ Multiplicity
        self.nElectrons     .append(Tree.nElectrons)
        self.nMuons         .append(Tree.nMuons)
        self.nBJets         .append(Tree.nBJets)
        self.nJets          .append(Tree.nJets)
        self.nPV            .append(Tree.nPV)
        #------------------------------------------------------------ MASS
        self.lepton_m       .append(Tree.leptonOneP4.M())            
        self.photon_m       .append(Tree.photonOneP4.M())            
        self.jet1_m         .append(Tree.jetOneP4.M())            
        self.jet2_m         .append(Tree.jetTwoP4.M())                    

        #self.dilep_m        .append((Tree.leptonOneP4+Tree.leptonTwoP4).M())
        #self.dilepgm_m      .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).M())

        self.dijet_m        .append((Tree.jetOneP4+Tree.jetTwoP4).M())
        self.dijetgm_m      .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).M())
        #------------------------------------------------------------ MASS
        self.lepton_E       .append(Tree.leptonOneP4.Energy())
        self.photon_E       .append(Tree.photonOneP4.Energy())
        self.jet1_E         .append(Tree.jetOneP4.Energy())
        self.jet2_E         .append(Tree.jetTwoP4.Energy())

        #self.dilep_E        .append((Tree.leptonOneP4+Tree.leptonTwoP4).Energy())
        #self.dilepgm_E      .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Energy())

        self.dijet_E        .append((Tree.jetOneP4+Tree.jetTwoP4).Energy())
        self.dijetgm_E      .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).Energy())
        #------------------------------------------------------------ PT
        self.photon_pt      .append(Tree.photonOneP4.Pt())
        self.lepton_pt      .append(Tree.leptonOneP4.Pt())
        #self.muon1_pt       .append(Tree.leptonOneP4.Pt())
        #self.muon2_pt       .append(Tree.leptonTwoP4.Pt())
        self.jet1_pt        .append(Tree.jetOneP4.Pt())
        self.jet2_pt        .append(Tree.jetTwoP4.Pt())

        #self.dilep_pt       .append((Tree.leptonOneP4+Tree.leptonTwoP4).Pt())
        #self.dilepgm_pt     .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Pt())
        self.dijet_pt       .append((Tree.jetOneP4+Tree.jetTwoP4).Pt())
        self.dijetgm_pt     .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).Pt())
        #------------------------------------------------------------ ETA
        self.photon_eta     .append(Tree.photonOneP4.Eta())
        self.lepton_eta     .append(Tree.leptonOneP4.Eta())
        #self.muon1_eta      .append(Tree.leptonOneP4.Eta())
        #self.muon2_eta      .append(Tree.leptonTwoP4.Eta())
        self.jet1_eta       .append(Tree.jetOneP4.Eta())
        self.jet2_eta       .append(Tree.jetTwoP4.Eta())

        #self.dilep_eta      .append((Tree.leptonOneP4+Tree.leptonTwoP4).Eta())
        #self.dilepgm_eta    .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Eta())
        self.dijet_eta       .append((Tree.jetOneP4+Tree.jetTwoP4).Eta())
        self.dijetgm_eta     .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).Eta())
        #------------------------------------------------------------ PHI
        self.photon_phi     .append(Tree.photonOneP4.Phi())
        self.lepton_phi     .append(Tree.leptonOneP4.Phi())
        #self.muon1_phi      .append(Tree.leptonOneP4.Phi())
        #self.muon2_phi      .append(Tree.leptonTwoP4.Phi())
        self.jet1_phi       .append(Tree.jetOneP4.Phi())
        self.jet2_phi       .append(Tree.jetTwoP4.Phi())

        #self.dilep_phi      .append((Tree.leptonOneP4+Tree.leptonTwoP4).Phi())
        #self.dilepgm_phi    .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Phi())
        self.dijet_phi       .append((Tree.jetOneP4+Tree.jetTwoP4).Phi())
        self.dijetgm_phi     .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).Phi())
        #------------------------------------------------------------ MT2
        self.lep1_Mt2       .append(Tree.leptonOneP4.Mt2())
        #------------------------------------------------------------ MET
        self.MET            .append(Tree.met)
        self.MET_phi        .append(Tree.metPhi)
        self.Mt             .append(np.sqrt(2*self.lepton_pt[-1]*self.MET[-1]*(1-np.cos(delta_phi(self.lepton_phi[-1], self.MET_phi[-1])) )))
        self.ht             .append(Tree.ht)
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        self.MuGm_D_eta     .append(self.lepton_eta[-1]  - self.photon_eta[-1]  )
        self.dijet_D_eta    .append(self.jet1_eta  [-1]  - self.jet2_eta  [-1]  )
        self.Jet1Gm_D_eta   .append(self.jet1_eta  [-1]  - self.photon_eta[-1]  )
        self.Jet2Gm_D_eta   .append(self.jet2_eta  [-1]  - self.photon_eta[-1]  )
        self.Jet1Mu_D_eta   .append(self.jet1_eta  [-1]  - self.lepton_eta[-1]  )
        self.Jet2Mu_D_eta   .append(self.jet2_eta  [-1]  - self.lepton_eta[-1]  )            
        
        self.dijet_gm_D_eta    .append(self.dijet_eta [-1] - self.photon_eta[-1]  )          
        self.dijet_lep_D_eta   .append(self.dijet_eta  [-1]  - self.lepton_eta[-1]  )          
        self.dijetgm_lep_D_eta .append(self.dijetgm_eta  [-1]  - self.lepton_eta[-1]  )   
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        self.MuGm_D_phi     .append(delta_phi(self.lepton_phi[-1]  , self.photon_phi[-1]  ))
        self.dijet_D_phi    .append(delta_phi(self.jet1_phi  [-1]  , self.jet2_phi  [-1]  ))
        self.Jet1Gm_D_phi   .append(delta_phi(self.jet1_phi  [-1]  , self.photon_phi[-1]  ))
        self.Jet2Gm_D_phi   .append(delta_phi(self.jet2_phi  [-1]  , self.photon_phi[-1]  ))
        self.Jet1Mu_D_phi   .append(delta_phi(self.jet1_phi  [-1]  , self.lepton_phi[-1]  ))
        self.Jet2Mu_D_phi   .append(delta_phi(self.jet2_phi  [-1]  , self.lepton_phi[-1]  ))            
        
        self.dijet_gm_D_phi    .append(delta_phi(self.dijet_phi  [-1]  , self.photon_phi[-1]  ))            
        self.dijet_lep_D_phi   .append(delta_phi(self.dijet_phi  [-1]  , self.lepton_phi[-1]  ))            
        self.dijetgm_lep_D_phi .append(delta_phi(self.dijetgm_phi  [-1]  , self.lepton_phi[-1]  )) 
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        self.MuGm_D_R       .append(np.sqrt(self.MuGm_D_phi  [-1]  **2 + self.MuGm_D_eta  [-1]  **2))
        self.dijet_D_R      .append(np.sqrt(self.dijet_D_phi [-1]  **2 + self.dijet_D_eta [-1]  **2))
        self.Jet1Gm_D_R     .append(np.sqrt(self.Jet1Gm_D_phi[-1]  **2 + self.Jet1Gm_D_eta[-1]  **2))
        self.Jet2Gm_D_R     .append(np.sqrt(self.Jet2Gm_D_phi[-1]  **2 + self.Jet2Gm_D_eta[-1]  **2))
        self.Jet1Mu_D_R     .append(np.sqrt(self.Jet1Mu_D_phi[-1]  **2 + self.Jet1Mu_D_eta[-1]  **2))
        self.Jet2Mu_D_R     .append(np.sqrt(self.Jet2Mu_D_phi[-1]  **2 + self.Jet2Mu_D_eta[-1]  **2))        

        self.dijet_gm_D_R   .append(np.sqrt(self.dijet_gm_D_phi[-1]**2  + self.dijet_gm_D_eta[-1]**2  ))
        self.dijet_lep_D_R  .append(np.sqrt(self.dijet_lep_D_phi[-1]**2  + self.dijet_lep_D_eta[-1]**2  )) 
    def _assignGenSplit(self, Tree):
        #------------------------------------------------------------ MASS
        self.genlepton_m       .append(Tree.leptonOneP4.M())            
        self.genphoton_m       .append(Tree.photonOneP4.M())            
        self.genjet1_m         .append(Tree.jetOneP4.M())            
        self.genjet2_m         .append(Tree.jetTwoP4.M())                    

        #self.digenlep_m        .append((Tree.leptonOneP4+Tree.leptonTwoP4).M())
        #self.digenlepgm_m      .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).M())

        self.digenjet_m        .append((Tree.jetOneP4+Tree.jetTwoP4).M())
        self.digenjetgm_m      .append((Tree.jetOneP4+Tree.jetTwoP4+Tree.photonOneP4).M())
        #------------------------------------------------------------ MT2
        self.lep1_Mt2       .append(Tree.leptonOneP4.Mt2())
        #------------------------------------------------------------ PT
        self.genphoton_pt      .append(Tree.photonOneP4.Pt())
        self.genlepton_pt       .append(Tree.leptonOneP4.Pt())
        #self.genmuon2_pt       .append(Tree.leptonTwoP4.Pt())
        self.genjet1_pt        .append(Tree.jetOneP4.Pt())
        self.genjet2_pt        .append(Tree.jetTwoP4.Pt())

        #self.digenlep_pt       .append((Tree.leptonOneP4+Tree.leptonTwoP4).Pt())
        #self.digenlepgm_pt     .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Pt())
        self.digenjet_pt       .append((Tree.jetOneP4+Tree.jetTwoP4).Pt())
        #------------------------------------------------------------ ETA
        self.genphoton_eta     .append(Tree.photonOneP4.Eta())
        self.genlepton_eta      .append(Tree.leptonOneP4.Eta())
        #self.genmuon2_eta      .append(Tree.leptonTwoP4.Eta())
        self.genjet1_eta       .append(Tree.jetOneP4.Eta())
        self.genjet2_eta       .append(Tree.jetTwoP4.Eta())

        #self.digenlep_eta      .append((Tree.leptonOneP4+Tree.leptonTwoP4).Eta())
        #self.digenlepgm_eta    .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Eta())
        self.digenjet_eta      .append((Tree.jetOneP4+Tree.jetTwoP4).Eta())
        #------------------------------------------------------------ PHI
        self.genphoton_phi     .append(Tree.photonOneP4.Phi())
        self.genlepton_phi      .append(Tree.leptonOneP4.Phi())
        #self.genmuon2_phi      .append(Tree.leptonTwoP4.Phi())
        self.genjet1_phi       .append(Tree.jetOneP4.Phi())
        self.genjet2_phi       .append(Tree.jetTwoP4.Phi())

        #self.digenlep_phi      .append((Tree.leptonOneP4+Tree.leptonTwoP4).Phi())
        #self.digenlepgm_phi    .append((Tree.leptonOneP4+Tree.leptonTwoP4+Tree.photonOneP4).Phi())
        self.digenjet_phi      .append((Tree.jetOneP4+Tree.jetTwoP4).Phi())
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        #self.digenlep_D_eta    .append(muon1_eta   - muon2_eta   )

        #self.digenlep_gm_D_eta .append(dilep_eta   - photon_eta  ) # Ups - gamma
        self.digenjet_D_eta    .append(self.genjet1_eta[-1]    - self.genjet2_eta[-1]    )

        self.genMuGm_D_eta     .append(self.genlepton_eta[-1]  - self.genphoton_eta[-1]  )
        self.genMuGm_D_eta     .append(self.genlepton_eta[-1]  - self.genphoton_eta[-1]  )
        self.digenjet_D_eta    .append(self.genjet1_eta[-1]    - self.genjet2_eta[-1]    )
        self.genJet1Gm_D_eta   .append(self.genjet1_eta[-1]    - self.genphoton_eta[-1]  )
        self.genJet2Gm_D_eta   .append(self.genjet2_eta[-1]    - self.genphoton_eta[-1]  )
        self.genJet1Mu_D_eta   .append(self.genjet1_eta[-1]    - self.genlepton_eta[-1]   )
        self.genJet2Mu_D_eta   .append(self.genjet2_eta[-1]    - self.genlepton_eta[-1]   )            
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        #self.digenlep_D_phi    .append(delta_phi(muon1_phi   , muon2_phi   ))

        #self.digenlep_gm_D_phi .append(delta_phi(dilep_phi   , photon_phi  )) 
        self.digenjet_D_phi    .append(delta_phi(self.genjet1_phi[-1]    , self.genjet2_phi[-1]    ))

        self.genMuGm_D_phi     .append(delta_phi(self.genlepton_phi[-1]  , self.genphoton_phi[-1]  ))
        self.genMuGm_D_phi     .append(delta_phi(self.genlepton_phi[-1]  , self.genphoton_phi[-1]  ))
        self.digenjet_D_phi    .append(delta_phi(self.genjet1_phi[-1]    , self.genjet2_phi[-1]    ))
        self.genJet1Gm_D_phi   .append(delta_phi(self.genjet1_phi[-1]    , self.genphoton_phi[-1]  ))
        self.genJet2Gm_D_phi   .append(delta_phi(self.genjet2_phi[-1]    , self.genphoton_phi[-1]  ))
        self.genJet1Mu_D_phi   .append(delta_phi(self.genjet1_phi[-1]    , self.genlepton_phi[-1]   ))
        self.genJet2Mu_D_phi   .append(delta_phi(self.genjet2_phi[-1]    , self.genlepton_phi[-1]   ))            
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        #self.digenlep_D_R      .append(np.sqrt(dilep_D_phi   **2 + dilep_D_eta  **2))

        self.digenjet_D_R      .append(np.sqrt(self.digenjet_D_phi[-1]   **2 + self.digenjet_D_eta[-1]   **2))
        self.genMuGm_D_R       .append(np.sqrt(self.genMuGm_D_phi[-1]    **2 + self.genMuGm_D_eta[-1]    **2))
        self.genJet1Gm_D_R     .append(np.sqrt(self.genJet1Gm_D_phi[-1]  **2 + self.genJet1Gm_D_eta[-1]  **2))
        self.genJet2Gm_D_R     .append(np.sqrt(self.genJet2Gm_D_phi[-1]  **2 + self.genJet2Gm_D_eta[-1]  **2))
        self.genJet1Mu_D_R     .append(np.sqrt(self.genJet1Mu_D_phi[-1]  **2 + self.genJet1Mu_D_eta[-1]  **2))
        self.genJet2Mu_D_R     .append(np.sqrt(self.genJet2Mu_D_phi[-1]  **2 + self.genJet2Mu_D_eta[-1]  **2))
        
    def _assignGen(self, Tree):
        self.genlepton_m     .append(Tree.genLeptonP4.M())   
        self.genphoton_m     .append(Tree.genPhotonP4.M())            
        self.genjet1_m       .append(Tree.genJetOneP4.M())            
        self.genjet2_m       .append(Tree.genJetTwoP4.M())            

        self.digenjet_m      .append((Tree.genJetOneP4 + Tree.genJetTwoP4).M())
        self.digenjetgm_m    .append((Tree.genJetOneP4 + Tree.genJetTwoP4 + Tree.genPhotonP4).M())
        #------------------------------------------------------------ PT
        self.genphoton_pt    .append(Tree.genPhotonP4.Pt())
        self.genlepton_pt    .append(Tree.genLeptonP4.Pt())
        self.genjet1_pt      .append(Tree.genJetOneP4.Pt())
        self.genjet2_pt      .append(Tree.genJetTwoP4.Pt())

        self.digenjet_pt     .append((Tree.genJetOneP4+Tree.genJetTwoP4).Pt())
        #------------------------------------------------------------ ETA
        self.genphoton_eta   .append(Tree.genPhotonP4.Eta())
        self.genlepton_eta   .append(Tree.genLeptonP4.Eta())
        self.genjet1_eta     .append(Tree.genJetOneP4.Eta())
        self.genjet2_eta     .append(Tree.genJetTwoP4.Eta())

        self.digenjet_eta    .append((Tree.genJetOneP4+Tree.genJetTwoP4).Eta())
        #------------------------------------------------------------ PHI
        self.genphoton_phi   .append(Tree.genPhotonP4.Phi())
        self.genlepton_phi   .append(Tree.genLeptonP4.Phi())
        self.genjet1_phi     .append(Tree.genJetOneP4.Phi())
        self.genjet2_phi     .append(Tree.genJetTwoP4.Phi())

        self.digenjet_phi    .append((Tree.genJetOneP4+Tree.genJetTwoP4).Phi())
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        #genMuGm_D_eta   .append(lepton_eta   - photon_eta     )
        self.genMuGm_D_eta   .append(self.genlepton_eta[-1]   - self.genphoton_eta[-1]  )            
        self.digenjet_D_eta  .append(self.genjet1_eta[-1]     - self.genjet2_eta[-1]    )
        self.genJet1Gm_D_eta .append(self.genjet1_eta[-1]     - self.genphoton_eta[-1]  )
        self.genJet2Gm_D_eta .append(self.genjet2_eta[-1]     - self.genphoton_eta[-1]  )
        self.genJet1Mu_D_eta .append(self.genjet1_eta[-1]     - self.genlepton_eta[-1]  )
        self.genJet2Mu_D_eta .append(self.genjet2_eta[-1]     - self.genlepton_eta[-1]  )            
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        #genMuGm_D_phi   .append(delta_phi(muon1_phi   , photon_phi  ))
        self.genMuGm_D_phi   .append(delta_phi(self.genlepton_phi[-1]   , self.genphoton_phi[-1]  ))           
        self.digenjet_D_phi  .append(delta_phi(self.genjet1_phi[-1]     , self.genjet2_phi[-1]    ))
        self.genJet1Gm_D_phi .append(delta_phi(self.genjet1_phi[-1]     , self.genphoton_phi[-1]  ))
        self.genJet2Gm_D_phi .append(delta_phi(self.genjet2_phi[-1]     , self.genphoton_phi[-1]  ))
        self.genJet1Mu_D_phi .append(delta_phi(self.genjet1_phi[-1]     , self.genlepton_phi[-1]  ))
        self.genJet2Mu_D_phi .append(delta_phi(self.genjet2_phi[-1]     , self.genlepton_phi[-1]  ))            
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        self.digenjet_D_R  .append(np.sqrt(self.digenjet_D_phi[-1]   **2 + self.digenjet_D_eta[-1]   **2))
        self.genMuGm_D_R   .append(np.sqrt(self.genMuGm_D_phi[-1]    **2 + self.genMuGm_D_eta[-1]    **2))
        self.genJet1Gm_D_R .append(np.sqrt(self.genJet1Gm_D_phi[-1]  **2 + self.genJet1Gm_D_eta[-1]  **2))
        self.genJet2Gm_D_R .append(np.sqrt(self.genJet2Gm_D_phi[-1]  **2 + self.genJet2Gm_D_eta[-1]  **2))
        self.genJet1Mu_D_R .append(np.sqrt(self.genJet1Mu_D_phi[-1]  **2 + self.genJet1Mu_D_eta[-1]  **2))
        self.genJet2Mu_D_R .append(np.sqrt(self.genJet2Mu_D_phi[-1]  **2 + self.genJet2Mu_D_eta[-1]  **2))

    def __add__(self,other):
        Other = jetjetgm_Data()
        Other.name = other.name
        
        Other.data = self.data 
        Other.cuts = self.cuts  + other.cuts
        
        Other.eventWeight = self.eventWeight + other.eventWeight
        Other.genWeight   = self.genWeight   + other.genWeight
        #------------------------------------------------------------ Events  
        for i in range(self.TotalEventBin):
            Other.TotalEvent[i]    = self.TotalEvent[i]    + other.TotalEvent[i]
            Other.TotalEvent_SF[i] = self.TotalEvent_SF[i] + other.TotalEvent_SF[i]
        
        
        Other.nJets        = self.nJets  + other.nJets   
        Other.nElectrons   = self.nElectrons + other.nElectrons
        Other.nMuons       = self.nMuons + other.nMuons
        Other.nBJets       = self.nBJets + other.nBJets
        Other.nPV          = self.nPV    + other.nPV   
        #------------------------------------------------------------ MASS        
        Other.lepton_m     = self.lepton_m + other.lepton_m
        Other.photon_m     = self.photon_m + other.photon_m
        Other.jet1_m       = self.jet1_m   + other.jet1_m
        Other.jet2_m       = self.jet2_m   + other.jet2_m

        Other.dijet_m      = self.dijet_m   + other.dijet_m
        Other.dijetgm_m    = self.dijetgm_m + other.dijetgm_m
        #------------------------------------------------------------ MASS        
        Other.lepton_E     = self.lepton_E + other.lepton_E
        Other.photon_E     = self.photon_E + other.photon_E
        Other.jet1_E       = self.jet1_E   + other.jet1_E
        Other.jet2_E       = self.jet2_E   + other.jet2_E

        Other.dijet_E      = self.dijet_E   + other.dijet_E
        Other.dijetgm_E    = self.dijetgm_E + other.dijetgm_E
        #------------------------------------------------------------ MT2
        Other.lep1_Mt2     = self.lep1_Mt2  + other.lep1_Mt2
        #------------------------------------------------------------ MET
        Other.MET          = self.MET  + other.MET
        Other.MET_phi      = self.MET_phi  + other.MET_phi
        Other.Mt           = self.Mt  + other.Mt
        Other.ht           = self.MET  + other.ht
        #------------------------------------------------------------ PT
        Other.lepton_pt    = self.lepton_pt + other.lepton_pt
        Other.photon_pt    = self.photon_pt + other.photon_pt
        Other.jet1_pt      = self.jet1_pt   + other.jet1_pt
        Other.jet2_pt      = self.jet2_pt   + other.jet2_pt

        Other.dijet_pt     = self.dijet_pt   + other.dijet_pt
        Other.dijetgm_pt   = self.dijetgm_pt + other.dijetgm_pt
        #------------------------------------------------------------ ETA
        Other.lepton_eta   = self.lepton_eta + other.lepton_eta
        Other.photon_eta   = self.photon_eta + other.photon_eta
        Other.jet1_eta     = self.jet1_eta   + other.jet1_eta
        Other.jet2_eta     = self.jet2_eta   + other.jet2_eta

        Other.dijet_eta    = self.dijet_eta   + other.dijet_eta
        Other.dijetgm_eta  = self.dijetgm_eta + other.dijetgm_eta
        #------------------------------------------------------------ PHI
        Other.lepton_phi   = self.lepton_phi  + other.lepton_phi
        Other.photon_phi   = self.photon_phi  + other.photon_phi
        Other.jet1_phi     = self.jet1_phi    + other.jet1_phi
        Other.jet2_phi     = self.jet2_phi    + other.jet2_phi

        Other.dijet_phi    = self.dijet_phi   + other.dijet_phi
        Other.dijetgm_phi  = self.dijetgm_phi + other.dijetgm_phi
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        Other.dijet_D_eta  = self.dijet_D_eta  + other.dijet_D_eta
        Other.MuGm_D_eta   = self.MuGm_D_eta   + other.MuGm_D_eta
        Other.dijet_D_eta  = self.dijet_D_eta  + other.dijet_D_eta
        Other.Jet1Gm_D_eta = self.Jet1Gm_D_eta + other.Jet1Gm_D_eta
        Other.Jet2Gm_D_eta = self.Jet2Gm_D_eta + other.Jet2Gm_D_eta
        Other.Jet1Mu_D_eta = self.Jet1Mu_D_eta + other.Jet1Mu_D_eta
        Other.Jet2Mu_D_eta = self.Jet2Mu_D_eta + other.Jet2Mu_D_eta         
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        Other.dijet_D_phi  = self.dijet_D_phi  + other.dijet_D_phi
        Other.MuGm_D_phi   = self.MuGm_D_phi   + other.MuGm_D_phi
        Other.dijet_D_phi  = self.dijet_D_phi  + other.dijet_D_phi
        Other.Jet1Gm_D_phi = self.Jet1Gm_D_phi + other.Jet1Gm_D_phi
        Other.Jet2Gm_D_phi = self.Jet2Gm_D_phi + other.Jet2Gm_D_phi
        Other.Jet1Mu_D_phi = self.Jet1Mu_D_phi + other.Jet1Mu_D_phi
        Other.Jet2Mu_D_phi = self.Jet2Mu_D_phi + other.Jet2Mu_D_phi           
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        Other.dijet_D_R    = self.dijet_D_R  + other.dijet_D_R
        Other.MuGm_D_R     = self.MuGm_D_R   + other.MuGm_D_R
        Other.dijet_D_R    = self.dijet_D_R  + other.dijet_D_R
        Other.Jet1Gm_D_R   = self.Jet1Gm_D_R + other.Jet1Gm_D_R
        Other.Jet2Gm_D_R   = self.Jet2Gm_D_R + other.Jet2Gm_D_R
        Other.Jet1Mu_D_R   = self.Jet1Mu_D_R + other.Jet1Mu_D_R
        Other.Jet2Mu_D_R   = self.Jet2Mu_D_R + other.Jet2Mu_D_R           
        #------------------------------------------------------------ Jets   
        #-----------------------------------------------
        #----------- GEN -------------------------------
        #------------------------------------------------------------ MASS        
        Other.genlepton_m     = self.genlepton_m + other.genlepton_m
        Other.genphoton_m     = self.genphoton_m + other.genphoton_m
        Other.genjet1_m       = self.genjet1_m   + other.genjet1_m
        Other.genjet2_m       = self.genjet2_m   + other.genjet2_m

        Other.digenjet_m      = self.digenjet_m   + other.digenjet_m
        Other.digenjetgm_m    = self.digenjetgm_m + other.digenjetgm_m
        #------------------------------------------------------------ PT
        Other.genlepton_pt    = self.genlepton_pt + other.genlepton_pt
        Other.genphoton_pt    = self.genphoton_pt + other.genphoton_pt
        Other.genjet1_pt      = self.genjet1_pt   + other.genjet1_pt
        Other.genjet2_pt      = self.genjet2_pt   + other.genjet2_pt

        Other.digenjet_pt     = self.digenjet_pt   + other.digenjet_pt
        Other.digenjetgm_pt   = self.digenjetgm_pt + other.digenjetgm_pt
        #------------------------------------------------------------ ETA
        Other.genlepton_eta   = self.genlepton_eta + other.genlepton_eta
        Other.genphoton_eta   = self.genphoton_eta + other.genphoton_eta
        Other.genjet1_eta     = self.genjet1_eta   + other.genjet1_eta
        Other.genjet2_eta     = self.genjet2_eta   + other.genjet2_eta

        Other.digenjet_eta    = self.digenjet_eta   + other.digenjet_eta
        Other.digenjetgm_eta  = self.digenjetgm_eta + other.digenjetgm_eta
        #------------------------------------------------------------ PHI
        Other.genlepton_phi   = self.genlepton_phi + other.genlepton_phi
        Other.genphoton_phi   = self.genphoton_phi + other.genphoton_phi
        Other.genjet1_phi     = self.genjet1_phi   + other.genjet1_phi
        Other.genjet2_phi     = self.genjet2_phi   + other.genjet2_phi

        Other.digenjet_phi    = self.digenjet_phi   + other.digenjet_phi
        Other.digenjetgm_phi  = self.digenjetgm_phi + other.digenjetgm_phi
        #------------------------------------------------------------ DELTAS
        #------------------------------------------------------------ DELTA ETA 
        Other.digenjet_D_eta  = self.digenjet_D_eta  + other.digenjet_D_eta
        Other.genMuGm_D_eta   = self.genMuGm_D_eta   + other.genMuGm_D_eta
        Other.digenjet_D_eta  = self.digenjet_D_eta  + other.digenjet_D_eta
        Other.genJet1Gm_D_eta = self.genJet1Gm_D_eta + other.genJet1Gm_D_eta
        Other.genJet2Gm_D_eta = self.genJet2Gm_D_eta + other.genJet2Gm_D_eta
        Other.genJet1Mu_D_eta = self.genJet1Mu_D_eta + other.genJet1Mu_D_eta
        Other.genJet2Mu_D_eta = self.genJet2Mu_D_eta + other.genJet2Mu_D_eta         
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA PHI 
        Other.digenjet_D_phi  = self.digenjet_D_phi  + other.digenjet_D_phi
        Other.genMuGm_D_phi   = self.genMuGm_D_phi   + other.genMuGm_D_phi
        Other.digenjet_D_phi  = self.digenjet_D_phi  + other.digenjet_D_phi
        Other.genJet1Gm_D_phi = self.genJet1Gm_D_phi + other.genJet1Gm_D_phi
        Other.genJet2Gm_D_phi = self.genJet2Gm_D_phi + other.genJet2Gm_D_phi
        Other.genJet1Mu_D_phi = self.genJet1Mu_D_phi + other.genJet1Mu_D_phi
        Other.genJet2Mu_D_phi = self.genJet2Mu_D_phi + other.genJet2Mu_D_phi           
        #------------------------------------------------------------
        #------------------------------------------------------------ DELTA R                
        Other.digenjet_D_R    = self.digenjet_D_R  + other.digenjet_D_R
        Other.genMuGm_D_R     = self.genMuGm_D_R   + other.genMuGm_D_R
        Other.digenjet_D_R    = self.digenjet_D_R  + other.digenjet_D_R
        Other.genJet1Gm_D_R   = self.genJet1Gm_D_R + other.genJet1Gm_D_R
        Other.genJet2Gm_D_R   = self.genJet2Gm_D_R + other.genJet2Gm_D_R
        Other.genJet1Mu_D_R   = self.genJet1Mu_D_R + other.genJet1Mu_D_R
        Other.genJet2Mu_D_R   = self.genJet2Mu_D_R + other.genJet2Mu_D_R           
        
        return Other
    
#    def cut(self,condition):
#        if condition == True:
    
    def assign(self,choose):
        if(choose == 'Split'):
            for tree in self.tree:
                if(tree.flagGen):
                    self._assign(tree)
                else:    
                    if not self.data:
                        self._assignGenSplit(tree)
        else:
            for tree in self.tree:
                self._assign(tree)
            if not self.data:
                for gentree in self.gentree:
                    self._assignGen(gentree)
         
    def TotalEvents(self,n):
        if n == '':
            return self.file.Get("TotalEvents_"+self.name.lower())
        elif self.data:
            return self.file.Get("TotalEvents_"+self.name+self.trigger).GetBinContent(n)
        else: 
            if self.flag:
                return self.file.Get("TotalEvents_" + self.name + self.trigger).GetBinContent(n)
            else:
                return self.file.Get("TotalEvents_" + self.name.lower()).GetBinContent(n)
              
    def ScaleFactor(self):
        return self.Topo.GetSF( self.N(), '2016',self.name,self.data) 
    
    def N(self):
        return self.TotalEvent[1] - 2*self.TotalEvent[30]
    
    def Weights(self):
        if self.data:
            self.weights = [    1              for _ in range(len(self.dijet_m))]   
        else :
            #self.weights = [self.ScaleFactor() for _ in range(len(self.dijet_m))]   
            self.weights = np.array(self.genWeight)*np.array(self.eventWeight)*np.array([self.ScaleFactor() for _ in range(len(self.dijet_m))])
        return self.weights

    def Hist(self, var = 'm2', part = ''):
        self.Weights() # Initialize weights
        
        if   var == 'm2':
            data = self.dijet_m
        elif var == 'm3':
            data = self.dijetgm_m
        elif var == 'pt':
            if   part == 'muon': 
                data = self.lepton_pt
            elif part == 'gm'  : 
                data = self.photon_pt
            elif part == 'jet1': 
                data = self.jet1_pt
            elif part == 'jet2': 
                data = self.jet2_pt 
            elif part == 'dijet':
                data = self.dijet_pt                 
            elif part == 'dijetgm':
                data = self.dijetgm_pt                
        elif var == 'eta':
            if   part == 'muon': 
                data = self.lepton_eta
            elif part == 'gm'  : 
                data = self.photon_eta
            elif part == 'jet1': 
                data = self.jet1_eta
            elif part == 'jet2': 
                data = self.jet2_eta   
            elif part == 'dijet':
                data = self.dijet_eta
            elif part == 'dijetgm':
                data = self.dijetgm_eta   
        elif var == 'phi':
            if   part == 'muon': 
                data = self.lepton_phi
            elif part == 'gm'  : 
                data = self.photon_phi
            elif part == 'jet1': 
                data = self.jet1_phi
            elif part == 'jet2': 
                data = self.jet2_phi   
            elif part == 'dijet':
                data = self.dijet_phi                
            elif part == 'dijetgm':
                data = self.dijetgm_phi  
        
        elif var == 'Deta':
            if part == "$\Delta \eta(j_1 j_2)$"     : 
                data = self.dijet_D_eta
            elif part == "$\Delta \eta(\mu \gamma)$": 
                data = self.MuGm_D_eta
            elif part == "$\Delta \eta(j_1 gm)$"    : 
                data = self.Jet1Gm_D_eta
            elif part == "$\Delta \eta(j_2 gm)$"    : 
                data = self.Jet2Gm_D_eta
            elif part == "$\Delta \eta(j_1 \mu)$"   : 
                data = self.Jet1Mu_D_eta
            elif part == "$\Delta \eta(j_2 \mu)$"   : 
                data = self.Jet2Mu_D_eta
        elif var == 'Dphi':
            if   part == "$\Delta \phi(j_1 j_2)$"   : 
                data = self.dijet_D_phi
            elif part == "$\Delta \phi(\mu \gamma)$": 
                data = self.MuGm_D_phi
            elif part == "$\Delta \phi(j_1 gm)$"    : 
                data = self.Jet1Gm_D_phi
            elif part == "$\Delta \phi(j_2 gm)$"    : 
                data = self.Jet2Gm_D_phi
            elif part == "$\Delta \phi(j_1 \mu)$"   : 
                data = self.Jet1Mu_D_phi
            elif part == "$\Delta \phi(j_2 \mu)$"   : 
                data = self.Jet2Mu_D_phi
        elif var == 'DR':
            if   part == "$\Delta R(j_1 j_2)$"   : 
                data = self.dijet_D_R
            elif part == "$\Delta R(\mu \gamma)$": 
                data = self.MuGm_D_R
            elif part == "$\Delta R(j_1 gm)$"    : 
                data = self.Jet1Gm_D_R
            elif part == "$\Delta R(j_2 gm)$"    : 
                data = self.Jet2Gm_D_R
            elif part == "$\Delta R(j_1 \mu)$"   : 
                data = self.Jet1Mu_D_R
            elif part == "$\Delta R(j_2 \mu)$"   : 
                data = self.Jet2Mu_D_R                

        elif var == 'nMuons': 
            data = self.nMuons
        elif var == 'nElectrons': 
            data = self.nElectrons
        elif var == 'nBJets': 
            data = self.nBJets
        elif var == 'nPV'   : 
            data = self.nPV  

        hist = np.histogram(np.array(data)[self.cuts],
                            range     = self.Help.plotOps[self.name][     'range'][var][part],
                            bins      = self.Help.plotOps[self.name][      'bins'][var][part],
                            weights   = np.array(self.weights)[self.cuts]
                           );                
        return hist

    def GetHistVal(self, var, part = ''):
        if var == 'nEvents':
            h = [self.TotalEvent, np.arange(0,self.TotalEventBin)]
        else:
            h = self.Hist(var,part)          
        
        x = (h[1][:-1] + h[1][1:])/2
        
        y = []
        for i in range(len(h[0])):
            for j in range(int(h[0][i])):
                y.append(x[i])
        
        return y
    
    def AddCuts(self,cuts):
        self.cuts = np.logical_and(self.cuts,cuts)
        
    def ResetCuts(self):
        self.cuts = [True for _ in self.cuts]
        


# In[2]:


class jetjetgm_Topology():
    def __init__(self):
        self.__xsec = {}
        self.__BR = {}
        self.__lumi = {}
        #--------------------------------------
        # Luminosity --- units = fb^-1
        self.__lumi = {}
        #self.__lumi['2016'] = 37.80 
        self.__lumi['2016'] = 35.922 # After Lumi Mask 
        
        #--------------------------------------
        # Branchin Ratio
        self.__BR["All"] = 1
        self.__BR["H2ZGm"] = 1.54e-3

        ### W Branching
        self.__BR["W2e"]   = 0.108
        self.__BR["W2mu"]  = 0.106
        self.__BR["W2tau"] = 0.112
        #self.__BR["W2ud"] = 0.676/3
        #self.__BR["W2sc"] = 0.676/3

        ### Z Branching
        self.__BR["Z2ee"]     = 0.0363
        self.__BR["Z2mumu"]   = 0.0366
        self.__BR["Z2tautau"] = 0.0367
        self.__BR["Z2jj"]     = 0.692
        self.__BR["Z2bbbar"]  = 0.156
        self.__BR["Z2ddbar"]  = 0.156
        self.__BR["Z2ssbar"]  = 0.156
        self.__BR["Z2uubar"]  = 0.116
        self.__BR["Z2ccbar"]  = 0.116

        # Top to Wb
        self.__BR["t2Wb"] = 0.91
        
        #--------------------------------------
        self.__xsec["Muon"]     = 1
        
        # Crossection of H = 125.5 GeV @ 13 TeV --- units = pb        
        self.__xsec["TT"]          = 831.76 
        self.__xsec["WplusH"]         = 0.831*self.__BR['H2ZGm']*self.__BR['Z2jj']
        self.__xsec["WminusH"]        = 0.527*self.__BR['H2ZGm']*self.__BR['Z2jj']
        self.__xsec["WH"]             = 1.358*self.__BR['H2ZGm']*self.__BR['Z2jj']  
        # Note
        # --xsec[W+H]=2/3* xsec["WH"]
        # --xsec[W-H]=1/3* xsec["WH"]
        # -----Br[H->Z+gm] = 0.002
        # -----Br[Z->j+j]  = 0.72
        
        self.__xsec['DYJets']      = 5765.4 #D YJetsToLL_M-50_amcatnlo 5765.4
        self.__xsec['WZTo2L2Q']    = 5.595
        self.__xsec['WZTo1L1Nu2Q'] = 10.71
        
        self.__xsec['ZZTo2L2Q']    = 3.22
        
        self.__xsec["WWTo2L2Nu"]   = 12.178
        self.__xsec["WWToLNuQQ"]   = 49.997
        
        self.__xsec["WZ"]          = 0.8594 
        self.__xsec["WZTo3LNu"]    = 4.42965
        self.__xsec["WZTo1L3Nu"]   = 3.033
        self.__xsec["WZTo1L1Nu2Q"] = 10.71
        self.__xsec["WZTo2L2Q"]    = 5.595
        
        self.__xsec['ggF']         = 43.62  
        self.__xsec['VBF']         = 3.727  
        self.__xsec['W1Jets']      = 9493.0
        self.__xsec['W2Jets']      = 3120.0 
        self.__xsec['W3Jets']      = 942.3
        self.__xsec['W4Jets']      = 524.1
        
        self.__xsec['W1JetsToLNu'] = 9493.0
        self.__xsec['W2JetsToLNu'] = 3120.0 
        self.__xsec['W3JetsToLNu'] = 942.3
        self.__xsec['W4JetsToLNu'] = 524.1
        

    def _GetXsec(self, process):
        if type(process) == str:
            return(self.__xsec[process])
        else :
            return(np.prod([self.__xsec[p] for p in process]))

    def _GetBR(self, process):
        if type(process) == str:
            return(self.__BR[process])
        else: 
            return(np.prod([self.__BR[p] for p in process]))

    def _GetLumi(self, process):
        return(self.__lumi[process])

    def GetSF(self, N,lumName,xsecName,data=False):
        if(N != 0 and not data):
            return(1e3*self._GetXsec(xsecName)*self._GetLumi(lumName)/N)
        else: 
            return(1)
        


# In[3]:


from ROOT import TFile
import matplotlib.pyplot as plt
#from jetjetgm_functions import *
from jetjetgm_Helper import *

