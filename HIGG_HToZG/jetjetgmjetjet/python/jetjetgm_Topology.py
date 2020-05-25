
# coding: utf-8

# In[2]:


class jetjetgm_Topology():
    def __init__(self):
        self.__xsec = {}
        self.__BR = {}
        self.__lumi = {}
        #--------------------------------------
        # Luminosity --- units = fb^-1
        self.__lumi = {}
        self.__lumi['2016'] = 37.80 
        #--------------------------------------
        self.__xsec["Muon"]     = 1
        
        # Crossection of H = 125.5 GeV @ 13 TeV --- units = pb        
        self.__xsec["TT"]     = 831.76 
        self.__xsec["WH"]     = 1.362  
        
        self.__xsec['DYJets'] = 5765.4 #D YJetsToLL_M-50_amcatnlo 5765.4
        self.__xsec['WZTo2L2Q'] = 5.595
        self.__xsec['WZTo1L1Nu2Q'] = 10.71
        
        self.__xsec['ZZTo2L2Q'] = 3.22
        
        self.__xsec["WWTo2L2Nu"]    = 12.178
        self.__xsec["WWToLNuQQ"]    = 49.997
        
        self.__xsec["WZ"]           = 0.8594 
        self.__xsec["WZTo3LNu"]     = 4.42965
        self.__xsec["WZTo1L3Nu"]    = 3.033
        self.__xsec["WZTo1L1Nu2Q"]  = 10.71
        self.__xsec["WZTo2L2Q"]     = 5.595
        
        self.__xsec['ggF']    = 43.62  
        self.__xsec['VBF']    = 3.727  
        self.__xsec['W1Jets'] = 9493.0
        self.__xsec['W2Jets'] = 3120.0 
        self.__xsec['W3Jets'] = 942.3
        self.__xsec['W4Jets'] = 524.1
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
        

