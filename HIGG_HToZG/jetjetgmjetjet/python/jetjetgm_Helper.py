
# coding: utf-8

# In[1]:


class jetjetgm_Helper():
    def __init__(self):
        __ranges = {
                  'mlep2':{'':[80,100]},
                  'm':{
                      'dijet'   :{'':[50,125]},
                      'dijetgm'   :{'':[100,140]},      
                      },
                  'm2'   :{'':[50,125]},
                  'm3'   :{'':[100,140]},
                  #'m2'   :{'':[30,140]},
                  #'m3'   :{'':[80,160]},
                  'E'   :{ 'photon'     :[0,100],
                           'lepton'   :[0,300],
                           'jet1'   :[0,500],
                           'jet2'   :[0,300],
                           'dijet'  :[0,800],
                           'dijetgm':[0,800]
                           },
                  'pt'   :{ 'photon'     :[0,80],
                            'lepton'   :[0,140],
                            'jet1'   :[0,150],
                            'jet2'   :[0,100],
                            'dijet'  :[0,300],
                            'dijetgm':[0,300]
                           },
                  'eta'   :{ 'photon'     :[-np.pi,np.pi],
                             'lepton'   :[-np.pi,np.pi],
                             'jet1'   :[-5,5],
                             'jet2'   :[-5,5],
                             'dijet'  :[-5,5],
                             'dijetgm':[-5,5],
                           },
                  'phi':{'photon'     :[-np.pi,np.pi],
                         'lepton'   :[-np.pi,np.pi],
                         'jet1'   :[-np.pi,np.pi],
                         'jet2'   :[-np.pi,np.pi],
                         'dijet'  :[-np.pi,np.pi],
                         'dijetgm':[-np.pi,np.pi],
                       },
                  'D_eta':{
                            'MuGm'      :[-np.pi,np.pi],
                            'dijet'     :[-np.pi,np.pi], 
                            'Jet1Gm'    :[-np.pi,np.pi],
                            'Jet2Gm'    :[-np.pi,np.pi],
                            'Jet1Mu'    :[-np.pi,np.pi],
                            'Jet2Mu'    :[-np.pi,np.pi],
                            'dijet_gm'  :[-np.pi,np.pi], 
                            'dijet_lep' :[-np.pi,np.pi],
                       },
                  'D_phi' : {
                            'MuGm'      :[0,np.pi],
                            'dijet'     :[0,np.pi], 
                            'Jet1Gm'    :[0,np.pi],
                            'Jet2Gm'    :[0,np.pi],
                            'Jet1Mu'    :[0,np.pi],
                            'Jet2Mu'    :[0,np.pi],
                            'dijet_gm'  :[0,np.pi], 
                            'dijet_lep' :[0,np.pi],
                         },
                  'D_R' : {
                            'MuGm'      :[0,4.5],
                            'dijet'     :[0,4.5], 
                            'Jet1Gm'    :[0,4.5],
                            'Jet2Gm'    :[0,4.5],
                            'Jet1Mu'    :[0,5.5],
                            'Jet2Mu'    :[0,6],
                            'dijet_gm'  :[0,4.5], 
                            'dijet_lep' :[0,4.5],
                         },
                  'nMuons'    :{'':[0,5]},
                  'nElectrons':{'':[0,5]},
                  'nBJets'    :{'':[0,5]},
                  'nPV'       :{'':[0,35]},
                 }

        __bins   = {
                    'mlep2':{'':20},
                    'm':{
                        'dijet'   :{'':15},
                        'dijetgm'   :{'':15},
                    },
                    'm2'   :{'':15},
                    'm3'   :{'':15},
                    'E'   :{
                            'photon'     :40,
                            'lepton'   :40,
                            'jet1'   :40,
                            'jet2'   :40,
                            'dijet'  :40,
                            'dijetgm':40,
                           },                        
                    'pt'   :{
                            'photon'     :40,
                            'lepton'   :40,
                            'jet1'   :40,
                            'jet2'   :40,
                            'dijet'  :40,
                            'dijetgm':40,
                           },
                    'eta'   :{'photon'    :15,
                             'lepton'   :15,
                             'jet1'   :15,
                             'jet2'   :15,
                             'dijet'  :15,
                             'dijetgm':15,
                           },
                    'phi'   :{'photon'    :15,
                             'lepton'   :15,
                             'jet1'   :15,
                             'jet2'   :15,
                             'dijet'  :15,
                             'dijetgm':15,
                       },
                    'D_eta'   :{
                                'MuGm'      :30,
                                'dijet'     :30, 
                                'Jet1Gm'    :30,
                                'Jet2Gm'    :30,
                                'Jet1Mu'    :30,
                                'Jet2Mu'    :30,
                                'dijet_gm'  :30, 
                                'dijet_lep' :30,
                           },
                    'D_phi'   :{
                                'MuGm'      :30,
                                'dijet'     :30, 
                                'Jet1Gm'    :30,
                                'Jet2Gm'    :30,
                                'Jet1Mu'    :30,
                                'Jet2Mu'    :30,
                                'dijet_gm'  :30, 
                                'dijet_lep' :30,
                             },
                    'D_R'     :{
                                'MuGm'      :30,
                                'dijet'     :30, 
                                'Jet1Gm'    :30,
                                'Jet2Gm'    :30,
                                'Jet1Mu'    :30,
                                'Jet2Mu'    :30,
                                'dijet_gm'  :30, 
                                'dijet_lep' :30,
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
                        'photon',
                        'lepton',
                        'jet1','jet2',
                        'dijet','dijetgm',
                        ]
        self.part_D = [
                        'MuGm',
                        'dijet', 
                        'Jet1Gm',
                        'Jet2Gm',
                        'Jet1Mu',
                        'Jet2Mu',
                        'dijet_gm', 
                        'dijet_lep',
                        ]
        #self.part    = [
        #                'gm',
        #                'muon',
        #                'jet1','jet2',
        #                'dijet','dijetgm',
        #                ]
        self.var1    = [
                        'm2','m3','pt','eta','phi',
                        'D_eta','D_phi','D_R',
                        'nMuons','nElectrons',
                        'nBJets','nPV',
                        ]
        self.var2    = {
                        'D_eta':[
                                 "$\Delta \eta(j_1 j_2)$"   ,
                                 "$\Delta \eta(\mu \gamma)$",
                                 "$\Delta \eta(j_1 gm)$"    ,
                                 "$\Delta \eta(j_2 gm)$"    ,
                                 "$\Delta \eta(j_1 \mu)$"   ,
                                 "$\Delta \eta(j_2 \mu)$"   ,            
                                 ],
                        'D_phi':[
                                 "$\Delta \phi(j_1 j_2)$"   ,
                                 "$\Delta \phi(\mu \gamma)$",
                                 "$\Delta \phi(j_1 gm)$"    ,
                                 "$\Delta \phi(j_2 gm)$"    ,
                                 "$\Delta \phi(j_1 \mu)$"   ,
                                 "$\Delta \phi(j_2 \mu)$"   ,
                                 ],
                         'D_R':[
                                 "$\Delta R(j_1 j_2)$"   ,
                                 "$\Delta R(\mu \gamma)$",
                                 "$\Delta R(j_1 gm)$"    ,
                                 "$\Delta R(j_2 gm)$"    ,
                                 "$\Delta R(j_1 \mu)$"   ,
                                 "$\Delta R(j_2 \mu)$"   ,
                                 ],
                    }
        
        self.var_A   = ['nMuons','nElectrons','nBJets','nPV']
        self.var_B   = ['m','pt','eta','phi']
        self.var_C   = ['D_eta','D_phi','D_R',]
        
        self.var_1   = ['m2','m3','nMuons','nElectrons','nBJets','nPV']
        self.var_2   = ['pt','eta','phi']
        self.var_3   = ['D_eta','D_phi','D_R',]
        
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

        self.plotOps['VBFHToZG_ZToJJ'] = {
                                            'color'    : 'b',
                                            'linewidth': 1.8,
                                            'linestyle': '-',
                                            'histtype' : 'step',
                                            'bins'     : __bins,
                                            'range'    : __ranges,
                                            'label'    : 'VBFH',
                                            'normed'   : False,
                                            'stacked'  : False,    
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
        self.plotOps['V V'] = {
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
                            self.plotOps['V V'],
                            self.plotOps['WJets'],
                            self.plotOps['WH'],
                            self.plotOps['VBFHToZG_ZToJJ'],
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


# In[2]:


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
    #d_phi =  obj1 - obj2
    #if   d_phi >= 2*np.pi: d_phi -= 2*np.pi
    #elif d_phi <        0: d_phi += 2*np.pi
    #if d_phi > np.pi: 
    #    d_phi = 2*np.pi - d_phi
    #elif d_phi < -np.pi: 
    #    d_phi = 2*np.pi + d_phi
    
    d_phi =  np.abs(obj1 - obj2)
    if d_phi > np.pi:
        d_phi = 2*np.pi - d_phi
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
    return a[0]*np.exp(-(x-a[1])**2/(2*a[2]**2)) + a[3]

def crystal_ball(x,*params):
    x = x+0j 
    N, a, n, xb, sig = params
    if a < 0:
        a = -a
    if n < 0:
        n = -n
    aa = abs(a)
    A = (n/aa)**n * np.exp(- aa**2 / 2)
    B = n/aa - aa
    total = 0.*x
    total += ((x-xb)/sig  > -a) * N * np.exp(- (x-xb)**2/(2.*sig**2))
    total += ((x-xb)/sig <= -a) * N * A * (B - (x-xb)/sig)**(-n)
    try:
        return total.real
    except:
        return totat
    return total

def binCenters(h):
    return (h[1][:-1] + h[1][1:])/2


# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:




