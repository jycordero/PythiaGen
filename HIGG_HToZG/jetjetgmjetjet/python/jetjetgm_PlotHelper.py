
# coding: utf-8

# In[ ]:


class jetjetgm_PlotHelper():
    def __init__(self):#color = 'k', linestyle = '-', linewidth = 1.5, isData = False, isSignalMC = False):
        #self.color     = color
        #self.linestyle = linestyle
        #self.linewidth = linewidth 
        #self.isData    = isData
        #self.isSignal  = isSignalMC
        #self.hist = plt.hist(None,
        #                    color     = self.color
        #                    linestyle = self.linestyle
        #                    linewidth = self.linewidth
        #                    )
        
        
        __ranges = {
                  'm2':[50,125],
                  'm3':[100,180],
                  'pt':{'gm'     :[0,80],
                        'muon'   :[0,140],
                        'jet1'   :[0,150],
                        'jet2'   :[0,100],
                        'dijet'  :[0,300],
                        'dijetgm':[0,300]
                       },
                  'eta':{'gm'     :[-np.pi,-np.pi],
                         'muon'   :[-np.pi,-np.pi],
                         'jet1'   :[-5,5],
                         'jet2'   :[-5,5],
                         'dijet'  :[-5,5],
                         'dijetgm':[-5,5],
                       },
                  'phi':{'gm'     :[-np.pi,-np.pi],
                         'muon'   :[-np.pi,-np.pi],
                         'jet1'   :[-np.pi,-np.pi],
                         'jet2'   :[-np.pi,-np.pi],
                         'dijet'  :[-np.pi,-np.pi],
                         'dijetgm':[-np.pi,-np.pi],
                       },
                  'Deta':{
                         "$\Delta \eta(j_1 j_2)$"   :[-np.pi,-np.pi],
                         "$\Delta \eta(\mu \gamma)$":[-np.pi,-np.pi],
                         "$\Delta \eta(j_1 gm)$"    :[-np.pi,-np.pi],
                         "$\Delta \eta(j_2 gm)$"    :[-np.pi,-np.pi],
                         "$\Delta \eta(j_1 \mu)$"   :[-np.pi,-np.pi],
                         "$\Delta \eta(j_2 \mu)$"   :[-np.pi,-np.pi],
                       },
                  'Dphi' : {
                         "$\Delta \phi(j_1 j_2)$"   :[-np.pi,-np.pi],
                         "$\Delta \phi(\mu \gamma)$":[-np.pi,-np.pi],
                         "$\Delta \phi(j_1 gm)$"    :[-np.pi,-np.pi],
                         "$\Delta \phi(j_2 gm)$"    :[-np.pi,-np.pi],
                         "$\Delta \phi(j_1 \mu)$"   :[-np.pi,-np.pi],
                         "$\Delta \phi(j_2 \mu)$"   :[-np.pi,-np.pi],
                         },
                  'DR' : {
                         "$\Delta R(j_1 j_2)$"   : [0,6],
                         "$\Delta R(\mu \gamma)$": [0,6],
                         "$\Delta R(j_1 gm)$"    : [0,6],
                         "$\Delta R(j_2 gm)$"    : [0,6],
                         "$\Delta R(j_1 \mu)$"   : [0,6],
                         "$\Delta R(j_2 \mu)$"   : [0,6]
                         },
                 }

        __bins   = {'m2':10,
                  'm3':10,
                  'pt':{'gm'     :40,
                        'muon'   :40,
                        'jet1'   :40,
                        'jet2'   :40,
                        'dijet'  :40,
                        'dijetgm':40,
                       },
                  'eta':{'gm'     :10,
                         'muon'   :10,
                         'jet1'   :10,
                         'jet2'   :10,
                         'dijet'  :10,
                         'dijetgm':10,
                       },
                  'phi':{'gm'     :10,
                         'muon'   :10,
                         'jet1'   :10,
                         'jet2'   :10,
                         'dijet'  :10,
                         'dijetgm':10,
                       },
                  'Deta':{
                         "$\Delta \eta(j_1 j_2)$"   :100,
                         "$\Delta \eta(\mu \gamma)$":100,
                         "$\Delta \eta(j_1 gm)$"    :100,
                         "$\Delta \eta(j_2 gm)$"    :100,
                         "$\Delta \eta(j_1 \mu)$"   :100,
                         "$\Delta \eta(j_2 \mu)$"   :100,
                       },
                  'Dphi' : {
                         "$\Delta \phi(j_1 j_2)$"   :100,
                         "$\Delta \phi(\mu \gamma)$":100,
                         "$\Delta \phi(j_1 gm)$"    :100,
                         "$\Delta \phi(j_2 gm)$"    :100,
                         "$\Delta \phi(j_1 \mu)$"   :100,
                         "$\Delta \phi(j_2 \mu)$"   :100,
                         },
                  'DR' : {
                         "$\Delta R(j_1 j_2)$"   :100,
                         "$\Delta R(\mu \gamma)$":100,
                         "$\Delta R(j_1 gm)$"    :100,
                         "$\Delta R(j_2 gm)$"    :100,
                         "$\Delta R(j_1 \mu)$"   :100,
                         "$\Delta R(j_2 \mu)$"   :100,
                         },
                 }
        self.plotOps= {}
        self.options =[
                    'color',
                    'linewidth',
                    'linestyle',
                    'histtype' ,
                    'bins'     ,
                    'range'    ,
                    'label'    ,
                    'normed'   ,
                    'stacked'  ,
                    ]
        self.part = ['gm','muon1','jet1','jet2','dijet','dijetgm']
        self.var1 = ['m2','m3','pt','eta','phi','Deta','Dphi','DR']
        self.var2 = [
                     "$\Delta R(j_1 j_2)$"   ,
                     "$\Delta R(\mu \gamma)$",
                     "$\Delta R(j_1 gm)$"    ,
                     "$\Delta R(j_2 gm)$"    ,
                     "$\Delta R(j_1 \mu)$"   ,
                     "$\Delta R(j_2 \mu)$"   ,
                    ]
        self.plotOps['SingleMuon'] = {
                            'color'    : 'k',
                            'linewidth': 1.2,
                            'linestyle': 'o',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WH',
                            'normed'   : False,
                            'stacked'  : True,
                            }
        self.plotOps['WH'] = {
                            'color'    : 'brown',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WH',
                            'normed'   : False,
                            'stacked'  : False,    
                            }
        self.plotOps['TT'] = {
                            'color'    : 'b',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'TT',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['DYJets'] = {
                            'color'    : 'r',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'DYJets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }

        self.plotOps['W1Jets'] = {
                            'color'    : 'r',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W1Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W2Jets'] = {
                            'color'    : 'g',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W2Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }

        self.plotOps['W3Jets'] = {
                            'color'    : 'orange',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W3Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W4Jets'] = {
                            'color'    : 'magenta',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W4Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }    


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:




