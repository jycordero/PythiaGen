
# coding: utf-8

# In[2]:


class jetjetgm_HelperV2():
    def __init__(self):
        __ranges = {
                  'mlep2':{'':[80,100]},
                  'm2'   :{'':[50,125]},
                  'm3'   :{'':[100,140]},
                  'pt'   :{ 'gm'     :[0,80],
                            'lepton1':[0,140],
                            'lepton2':[0,120],
                            'jet1'   :[0,150],
                            'jet2'   :[0,100],
                            'dijet'  :[0,300],
                            'dijetgm':[0,300]
                           },
                  'eta'   :{ 'gm'     :[-np.pi,np.pi],
                             'lepton1':[-np.pi,np.pi],
                             'lepton2':[-np.pi,np.pi],
                             'jet1'   :[-5,5],
                             'jet2'   :[-5,5],
                             'dijet'  :[-5,5],
                             'dijetgm':[-5,5],
                           },
                  'phi':{'gm'     :[-np.pi,np.pi],
                         'lepton1':[-np.pi,np.pi],
                         'lepton2':[-np.pi,np.pi],
                         'jet1'   :[-np.pi,np.pi],
                         'jet2'   :[-np.pi,np.pi],
                         'dijet'  :[-np.pi,np.pi],
                         'dijetgm':[-np.pi,np.pi],
                       },
                  'Deta':{
                         "$\Delta \eta(j_1 j_2)$"   :[-np.pi,np.pi],
                         "$\Delta \eta(\mu \gamma)$":[-np.pi,np.pi],
                         "$\Delta \eta(j_1 gm)$"    :[-np.pi,np.pi],
                         "$\Delta \eta(j_2 gm)$"    :[-np.pi,np.pi],
                         "$\Delta \eta(j_1 \mu)$"   :[-np.pi,np.pi],
                         "$\Delta \eta(j_2 \mu)$"   :[-np.pi,np.pi],
                       },
                  'Dphi' : {
                         "$\Delta \phi(j_1 j_2)$"   :[0,np.pi],
                         "$\Delta \phi(\mu \gamma)$":[0,np.pi],
                         "$\Delta \phi(j_1 gm)$"    :[0,np.pi],
                         "$\Delta \phi(j_2 gm)$"    :[0,np.pi],
                         "$\Delta \phi(j_1 \mu)$"   :[0,np.pi],
                         "$\Delta \phi(j_2 \mu)$"   :[0,np.pi],
                         },
                  'DR' : {
                         "$\Delta R(j_1 j_2)$"   : [0,6.5],
                         "$\Delta R(\mu \gamma)$": [0,6.5],
                         "$\Delta R(j_1 gm)$"    : [0,6.5],
                         "$\Delta R(j_2 gm)$"    : [0,6.5],
                         "$\Delta R(j_1 \mu)$"   : [0,6.5],
                         "$\Delta R(j_2 \mu)$"   : [0,6.5]
                         },
                  'nMuons'    :{'':[0,5]},
                  'nElectrons':{'':[0,5]},
                  'nBJets'    :{'':[0,5]},
                  'nPV'       :{'':[0,35]},
                 }

        __bins   = {
                    'mlep2':{'':20},
                    'm2'   :{'':15},
                    'm3'   :{'':15},
                    'pt'   :{
                            'gm'     :40,
                            'lepton1':40,
                            'lepton2':40,
                            'jet1'   :40,
                            'jet2'   :40,
                            'dijet'  :40,
                            'dijetgm':40,
                           },
                    'eta'   :{'gm'    :15,
                             'lepton1':15,
                             'lepton2':15,
                             'jet1'   :15,
                             'jet2'   :15,
                             'dijet'  :15,
                             'dijetgm':15,
                           },
                    'phi'   :{'gm'   :15,
                             'lepton1':15,
                             'lepton2':15,
                             'jet1'   :15,
                             'jet2'   :15,
                             'dijet'  :15,
                             'dijetgm':15,
                       },
                    'Deta'   :{
                             "$\Delta \eta(j_1 j_2)$"   :30,
                             "$\Delta \eta(\mu \gamma)$":30,
                             "$\Delta \eta(j_1 gm)$"    :30,
                             "$\Delta \eta(j_2 gm)$"    :30,
                             "$\Delta \eta(j_1 \mu)$"   :30,
                             "$\Delta \eta(j_2 \mu)$"   :30,
                           },
                    'Dphi'   :{
                             "$\Delta \phi(j_1 j_2)$"   :30,
                             "$\Delta \phi(\mu \gamma)$":30,
                             "$\Delta \phi(j_1 gm)$"    :30,
                             "$\Delta \phi(j_2 gm)$"    :30,
                             "$\Delta \phi(j_1 \mu)$"   :30,
                             "$\Delta \phi(j_2 \mu)$"   :30,
                             },
                    'DR'     :{
                             "$\Delta R(j_1 j_2)$"   :30,
                             "$\Delta R(\mu \gamma)$":30,
                             "$\Delta R(j_1 gm)$"    :30,
                             "$\Delta R(j_2 gm)$"    :30,
                             "$\Delta R(j_1 \mu)$"   :30,
                             "$\Delta R(j_2 \mu)$"   :30,
                             },
                    'nMuons'    :{'': 5},
                    'nElectrons':{'': 5},
                    'nBJets'    :{'': 5},
                    'nPV'       :{'':35},
                 }
        
        self.ranges  = __ranges
        self.bins    = __bins
        
        self.options = [
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
        self.part    = [
                        'gm',
                        'lepton1','lepton2',
                        'jet1','jet2',
                        'dijet','dijetgm',
                        ]
        self.var1    = [
                        'mlep2','m2','m3','pt','eta','phi',
                        'Deta','Dphi','DR',
                        'nMuons','nElectrons',
                        'nBJets','nPV',
                        ]
        self.var2    = {
                        'Deta':[
                                 "$\Delta \eta(j_1 j_2)$"   ,
                                 "$\Delta \eta(\mu \gamma)$",
                                 "$\Delta \eta(j_1 gm)$"    ,
                                 "$\Delta \eta(j_2 gm)$"    ,
                                 "$\Delta \eta(j_1 \mu)$"   ,
                                 "$\Delta \eta(j_2 \mu)$"   ,            
                                 ],
                        'Dphi':[
                                 "$\Delta \phi(j_1 j_2)$"   ,
                                 "$\Delta \phi(\mu \gamma)$",
                                 "$\Delta \phi(j_1 gm)$"    ,
                                 "$\Delta \phi(j_2 gm)$"    ,
                                 "$\Delta \phi(j_1 \mu)$"   ,
                                 "$\Delta \phi(j_2 \mu)$"   ,
                                 ],
                         'DR':[
                                 "$\Delta R(j_1 j_2)$"   ,
                                 "$\Delta R(\mu \gamma)$",
                                 "$\Delta R(j_1 gm)$"    ,
                                 "$\Delta R(j_2 gm)$"    ,
                                 "$\Delta R(j_1 \mu)$"   ,
                                 "$\Delta R(j_2 \mu)$"   ,
                                 ],
                    }
        
        self.var_1   = ['mlep2','m2','m3','nMuons','nElectrons','nBJets','nPV']
        self.var_2   = ['pt''eta','phi']
        self.var_3   = ['Deta','Dphi','DR',]
        
        self.plotOps= {}
        self.plotOps['muon_2016'] = {
                            'color'    : 'k',
                            'linewidth': 1.2,
                            'linestyle': 'o',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'SingleMuon',
                            'normed'   : False,
                            'stacked'  : True,
                            }
        
        self.plotOps['WplusH'] = {
                            'color'    : 'b',
                            'linewidth': 1.8,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WH',
                            'normed'   : False,
                            'stacked'  : False,    
                            }
        self.plotOps['WminusH'] = {
                            'color'    : 'b',
                            'linewidth': 1.8,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WH',
                            'normed'   : False,
                            'stacked'  : False,    
                            }
        self.plotOps['WH'] = {
                            'color'    : 'b',
                            'linewidth': 1.8,
                            'linestyle': '-',
                            'histtype' : 'step',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WH',
                            'normed'   : False,
                            'stacked'  : False,    
                            }
        
        self.plotOps['TT'] = {
                            'color'    : 'magenta',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'TT',
                            'normed'   : False,
                            'stacked'  : True,        
                            }
        
        self.plotOps['DYJets'] = {
                            'color'    : 'cyan',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'DYJets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        
        self.plotOps['ZZTo2L2Q'] = {
                            'color'    : 'grey',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'ZZTo2L2Q',
                            'normed'   : False,
                            'stacked'  : False,        
                            }         
        self.plotOps['WZTo1L1Nu2Q'] = {
                            'color'    : 'teal',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WZTo1L1Nu2Q',
                            'normed'   : False,
                            'stacked'  : False,        
                            }    
        self.plotOps['WZTo2L2Q'] = {
                            'color'    : 'purple',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WZTo2L2Q',
                            'normed'   : False,
                            'stacked'  : False,        
                            }         
        self.plotOps['VV'] = {
                            'color'    : 'r',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'WZTo2L2Q',
                            'normed'   : False,
                            'stacked'  : True,        
                            }         
        
        self.plotOps['W1Jets']      = {
                            'color'    : 'r',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W1Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W2Jets']      = {
                            'color'    : 'g',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W2Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W3Jets']      = {
                            'color'    : 'orange',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W3Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W4Jets']      = {
                            'color'    : 'magenta',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W4Jets',
                            'normed'   : False,
                            'stacked'  : False,        
                            }    
        self.plotOps['W1JetsToLNu'] = {
                            'color'    : 'r',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W1JetsToLNu',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W2JetsToLNu'] = {
                            'color'    : 'g',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W2JetsToLNu',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W3JetsToLNu'] = {
                            'color'    : 'orange',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W3JetsToLNu',
                            'normed'   : False,
                            'stacked'  : False,        
                            }
        self.plotOps['W4JetsToLNu'] = {
                            'color'    : 'magenta',
                            'linewidth': 1.2,
                            'linestyle': '-',
                            'histtype' : 'stepfilled',
                            'bins'     : __bins,
                            'range'    : __ranges,
                            'label'    : 'W4JetsToLNu',
                            'normed'   : False,
                            'stacked'  : False,        
                            }    
        self.plotOps['WJets']       = {
                                        #'color'    : 'teal',
                                        'color'    : 'limegreen',
                                        'linewidth': 1.2,
                                        'linestyle': '-',
                                        'histtype' : 'stepfilled',
                                        'bins'     : __bins,
                                        'range'    : __ranges,
                                        'label'    : 'W+Jets',
                                        'normed'   : False,
                                        'stacked'  : True,        
                                        }    


        self.plotOpsAll = [
                            self.plotOps['TT'], 
                            self.plotOps['DYJets'],
                            self.plotOps['VV'],
                            self.plotOps['WJets'],
                            self.plotOps['WH'],
                            self.plotOps['muon_2016'],
                          ]    
        self.Opt = {}
        self.Opt['W2Jets'] = {
                                'isData' : False,
                                'isSigMC': False,
                                }
        
    def joinData(self, datas, var, part = None):
        out = []
        for d in datas:
            out += d.GetHistVal(var,part)
        return out
    
    def AndCuts(self,cuts):
        t = cuts[0]
        for i in range(1,len(cuts)):
            temp = t
            t    = np.logical_and(temp,cuts[i])
        return t


# In[4]:


def find_eff_interval(k,N):
    if k>N:
        return [0,0,0]
    
    tempa,tempb = 0,1

    alpha = stats.beta.rvs(k+1,N-k+1,size=100)
    beta  = stats.beta.rvs(k+1,N-k+1,size=100)
    alpha.sort()
    beta.sort()
    
    for i in range(len(alpha)):
        for j in range(len(beta)):
            if beta[j] > alpha[i]:
                K=(betainc(k+1,N-k+1,beta[j]))-(betainc(k+1,N-k+1,alpha[i]))
                if K > 0.67 and K < 0.69:
                    if tempb-tempa > beta[j]-alpha[i]:
                        tempa = alpha[i]
                        tempb = beta[j]
                        
    return [k/N,tempb-k/N,k/N-tempa]

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def delta_phi(obj1,obj2):
    d_phi =  obj1 - obj2
    #if d_phi >= 2*np.pi: d_phi -= 2*np.pi
    #elif d_phi < 0: d_phi += 2*np.pi
    if d_phi > np.pi: 
        d_phi = 2*np.pi - d_phi
    elif d_phi < -np.pi: 
        d_phi = 2*np.pi + d_phi
    return d_phi

def cut_indices_out(data,MIN,MAX):
    data =  np.array(data)
    return np.logical_or( data < MIN, data > MAX)

def cut_indices(data,MIN,MAX):
    data =  np.array(data)
    return np.logical_and( data > MIN, data < MAX)

def strIntersection(s1, s2):
    out = ""
    for c in s1:
        if c in s2 and not c in out:
            out += c

    return out

def GetName(s1):
    out = ''
    for l in s1:
        if l.isupper():
            out += l
    return out

def gauss(x,*a):
    return a[0]*np.exp(-(x-a[1])**2/(2*a[2]**2))


# In[7]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:




