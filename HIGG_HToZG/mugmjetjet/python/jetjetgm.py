
# coding: utf-8

# In[1]:


# Python dependencies 
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import erf, betainc, gamma
from scipy import asarray as ar,exp
from numpy.random import uniform
from scipy import stats
#import scipy.integrate as integrate
from scipy.integrate import simps


# External Dependencies
from ROOT import TFile, TTree

# My Dependencies
from jetjetgm_Data import *
from jetjetgm_Topology import *
from jetjetgm_functions import *


# # JetJetLepGm

# In[2]:


# --------------------------------------
#  Data
run = ['B','C','D','E','F','G','H']
#for r in run:
#    MuonData = jetjetgm_Data("Data/","muon_2016",r,data=True)
MuonData = [jetjetgm_Data("Data/","muon_2016",r,data=True) for r in run]

trigger = "HLT_IsoMu24B_v"
# ---------------------------------------
# Signal
WminusH = jetjetgm_Data("WminusH_HToZG_WToAll/", "WminusH_",trigger)
WplusH  = jetjetgm_Data("WplusH_HToZG_WToAll/" , "WplusH_",trigger)

# ---------------------------------------
# Background
trigger = "HLT_IsoMu24B_v"
TT     = jetjetgm_Data("TT_powheg/"  , "TT_",trigger)
W2Jets = jetjetgm_Data("W2JetsToLNu/", "W2Jets_",trigger)
W3Jets = jetjetgm_Data("W3JetsToLNu/", "W3Jets_",trigger)

# ---------------------------------------
# Understanding the Z Peak
ZPeak = jetjetgm_Data("ZPeak_WminusH_HToZG_WToAll/", "ZPeak_WminusH_","HLT_IsoMu24_v")


# In[9]:


#[M.assign('') for M in MuonData]
#Muon = MuonData[0] + MuonData[1] + MuonData[2] + MuonData[3] + MuonData[4] + MuonData[5] + MuonData[6] 
MuonData[0].assign('')
MuonData[1].assign('')
MuonData[2].assign('')
MuonData[3].assign('')
MuonData[4].assign('')
MuonData[5].assign('')
MuonData[6].assign('')
#print(MuonData[0].file)
#print(MuonData[0].tree)
#print("tree_" + MuonData[0].name + MuonData[0].trigger)


#print(MuonData.folder+MuonData.name)
#print(MuonData.file)
#print(MuonData.tree)
#MuonData.assign('')
#print(MuonData.jet1_pt)


# In[4]:


SF = jetjetgm_Topology()
figpath = "/home/jcordero/Pictures/CMS/bbbar/"


# In[5]:


label_part = ['gm','muon1','jet1','jet2','dijet','dijetgm']
max_ranges = [ 80,     140,   150,   100,    300,      300]
pt_bins    = [  40,     40,    40,    40,     40,       40]


# In[7]:


#--------------------------
#Muon.assign('')
[MuonData[0].assign('')
#--------------------------
ZPeak.assign('')
WminusH.assign('')
WplusH.assign('')
WH = WminusH + WplusH

TT.assign('')
W2Jets.assign('')
W3Jets.assign('')

#--------------------------

data        = [ WH,  TT,  W2Jets,  W3Jets,  Muon]
listSamples = ["WH","TT","W2Jets",'W3Jets','Muon'] # for xsec calc
#data        = [ ZPeak]#, WH, TT, W2Jets,  W3Jets]
#listSamples = ["WH"]#, "WH","TT","W2Jets",'W3Jets'] # for xsec calc
colors = ['r','b',    'g','orange','k']


# In[6]:




#import plotly.plotly as py
#import plotly.graph_objs as go

#trace = go.Table(
#    header=dict(values=['A Scores', 'B Scores']),
#    cells=dict(values=[[100, 90, 80, 90],
#                       [95, 85, 75, 95]]))

#table = [trace] 
#py.iplot(table, filename = 'basic_table')



N = [ d.TotalEvents(1) for d in data]
w = [SF.GetSF(N[i],'2016',listSamples[i]) if N[i] != 0 else 1 for i in range(len(N))]


# In[7]:


for i in range(12):    
    print(i,WminusH.TotalEvents(i), WplusH.TotalEvents(i),TT.TotalEvents(i),W2Jets.TotalEvents(i),W3Jets.TotalEvents(i) )


# In[8]:


#----------- BINS
pt_bin1 = [0,5,10,15,20,25,30,35,40,46,53,65, 82,110,150] 
pt_bin2 = [0,5,10,15,20,25,30,35,40,47,57,78,105,130,150]
pt_bin3 = [0,3 ,6, 9,12,15,18,21,24,27,31,37, 45, 50, 60,90]#80,100,120] # [i*2 for i in range(100)]
          
#pt_bins = [40,40,40,40,40.40,40]
#pt_bins = [40,40,40,40]
#pt_bins = [pt_bin1,pt_bin2,pt_bin3]

m_bins = 10
eta_bins = 30
phi_bins = 30

d_eta_bins = 60
d_phi_bins = 60

jet_bins = 10
#------------ CUTS
dilepM_min = 70
dilepM_max = 110

d_phi_min = -0.075
d_phi_max = 0.075

d_eta_min = -0.1
d_eta_max = 0.1        


# In[9]:


jet1pt   = [d.jet1_pt for d in data]
jet2pt   = [d.jet2_pt for d in data]
leptonpt = [d.lepton_pt for d in data]
photonpt = [d.photon_pt for d in data]

jet1m   = [d.jet1_m for d in data]
jet2m   = [d.jet2_m for d in data]
leptonm = [d.lepton_m for d in data]
photonm = [d.photon_m for d in data]


jet1eta   = [d.jet1_eta for d in data]
jet2eta   = [d.jet2_eta for d in data]
leptoneta = [d.lepton_eta for d in data]
photoneta = [d.photon_eta for d in data]

jet1phi   = [d.jet1_phi for d in data]
jet2phi   = [d.jet2_phi for d in data]
leptonphi = [d.lepton_phi for d in data]
photonphi = [d.photon_phi for d in data]

dijetm   = [d.dijet_m for d in data]
dijetgmm = [d.dijetgm_m for d in data]
dijetpt  = [d.dijet_pt for d in data]
dijetgmpt  = [d.dijet_pt for d in data]


pt    = [photonpt  , leptonpt  , jet1pt  , jet2pt, dijetpt, dijetgmpt]
m     = [photonm   , leptonm   ,  jet1m   , jet2m , dijetm , dijetgmm ]
eta   = [photoneta , leptoneta , jet1eta , jet2eta]
phi   = [photonphi , leptonphi , jet1phi , jet2phi]


MuGm_D_eta   = [d.MuGm_D_eta  for d in data]
dijet_D_eta  = [d.dijet_D_eta for d in data]
Jet1Gm_D_eta = [d.Jet1Gm_D_eta for d in data]
Jet2Gm_D_eta = [d.Jet2Gm_D_eta for d in data]
Jet1Mu_D_eta = [d.Jet1Mu_D_eta for d in data]
Jet2Mu_D_eta = [d.Jet2Mu_D_eta for d in data]

MuGm_D_phi   = [d.MuGm_D_phi  for d in data]
dijet_D_phi  = [d.dijet_D_phi for d in data]
Jet1Gm_D_phi = [d.Jet1Gm_D_phi for d in data]
Jet2Gm_D_phi = [d.Jet2Gm_D_phi for d in data]
Jet1Mu_D_phi = [d.Jet1Mu_D_phi for d in data]
Jet2Mu_D_phi = [d.Jet2Mu_D_phi for d in data]

MuGm_D_R   = [d.MuGm_D_R  for d in data]
dijet_D_R  = [d.dijet_D_R for d in data]
Jet1Gm_D_R = [d.Jet1Gm_D_R for d in data]
Jet2Gm_D_R = [d.Jet2Gm_D_R for d in data]
Jet1Mu_D_R = [d.Jet1Mu_D_R for d in data]
Jet2Mu_D_R = [d.Jet2Mu_D_R for d in data]


d_eta = [
         dijet_D_eta, 
         MuGm_D_eta, 
         Jet1Gm_D_eta, 
         Jet2Gm_D_eta, 
         Jet1Mu_D_eta,
         Jet2Mu_D_eta
        ]
title_d_eta = [
                "$\Delta \eta(j_1 j_2)$",
               "$\Delta \eta(\mu \gamma)$",
               "$\Delta \eta(j_1 gm)$",
               "$\Delta \eta(j_2 gm)$",
               "$\Delta \eta(j_1 \mu)$",
               "$\Delta \eta(j_2 \mu)$"
              ]

d_phi = [
        dijet_D_phi, 
        MuGm_D_phi, 
        Jet1Gm_D_phi, 
        Jet2Gm_D_phi, 
        Jet1Mu_D_phi,
        Jet2Mu_D_phi
        ]
title_d_phi = [
                "$\Delta \phi(j_1 j_2)$",
               "$\Delta \phi(\mu \gamma)$",
               "$\Delta \phi(j_1 gm)$",
               "$\Delta \phi(j_2 gm)$",
               "$\Delta \phi(j_1 \mu)$",
               "$\Delta \phi(j_2 \mu)$"
              ]

d_R = [    
        dijet_D_R, 
        MuGm_D_R, 
        Jet1Gm_D_R, 
        Jet2Gm_D_R, 
        Jet1Mu_D_R,
        Jet2Mu_D_R
        ]
title_d_R = [
                "$\Delta R(j_1 j_2)$",
               "$\Delta R(\mu \gamma)$",
               "$\Delta R(j_1 gm)$",
               "$\Delta R(j_2 gm)$",
               "$\Delta R(j_1 \mu)$",
               "$\Delta R(j_2 \mu)$"
              ]


# # BBBAR mass spectrum

# In[10]:


#plt.figure(figsize = (15,15))
plt.figure(figsize = (15,10))

nx,ny = 1,2
sizeLeg = 10

for i in range(len(jet1pt)):
    n = 1
    plt.subplot(nx,ny,n)
    M_J       = jet1m[i]
    legend_lab = listSamples[i]
    title_lab  = "jet 1"
    COL        = colors[i]
    weight     = np.array([w[i] for ii in range(len(M_J))])

    ax = plt.gca()
    ax.hist(
            M_J,
            #bins      = m_bins,
            #range     = [5.5,12],
            range     = [0,40],
            histtype  = 'step',
            color     = COL,
            weights   = weight,
            label     = legend_lab,
            #linestyle = line_style[k],
            linewidth = 1.2
            )
    ax.legend(prop={'size': sizeLeg})
    ax.set_title(title_lab)
    ax.set_xlabel(r"$m(jet)[GeV]$")
    ax.grid(linestyle='--')
    
    n = 2
    plt.subplot(nx,ny,n)
    M_J       = jet2m[i]
    legend_lab = listSamples[i]
    title_lab  = "jet 2"
    COL        = colors[i]
    weight     = np.array([w[i] for ii in range(len(M_J))])

    ax = plt.gca()
    ax.hist(
            M_J,
            #bins      = m_bins,
            range     = [0,20],
            histtype  = 'step',
            color     = COL,
            weights   = weight,
            label     = legend_lab,
            #linestyle = line_style[k],
            linewidth = 1.2
            )
    ax.legend(prop={'size': sizeLeg})
    ax.set_title(title_lab)
    ax.set_xlabel(r"$m(jet)[GeV]$")
    ax.grid(linestyle='--')

plt.show()


# In[11]:


def gauss(x,*a):
    return a[0]*np.exp(-(x-a[1])**2/(2*a[2]**2))


# In[12]:


fig = plt.figure(figsize = (16,8))
#h = [[np.array([0,0]) for _ in range(len(data))] for _ in range(len(label_trig[k][0]))]

nx,ny = 1,2
for i in range(len(data)):
    n = 1
    plt.subplot(nx,ny,n)
    M2         = dijetm[i]
    M3         = dijetgmm[i]
    legend_lab = listSamples[i]
    title_lab  = "2 body mass"
    COL        = colors[i]
    bHiggs     = 20
    rHiggs     = [80,200]
    weight     = np.array([w[i] for ii in range(len(M2))])

    ax = plt.gca()
    h = ax.hist(
            M2,
            bins      = m_bins,
            range     = [50,120],
            #range     = [0,200],
            histtype  = 'step',
            color     = COL,
            stacked = True,
            weights   = weight,
            label     = legend_lab,
            #linestyle = line_style[k],
            linewidth = 1.2
            )

    #if(KK == 0 and k==0 and i == 0 ):
    #    y2,x2 = h[0],h[1][1:]
    #    a = [800,90,10]
    #    fit2 = curve_fit(gauss,x2,y2,p0 =a)
    ax.legend(prop={'size': 10})
    ax.set_title(title_lab)
    ax.set_xlabel(r"$m(b+bbar)[GeV]$")
    ax.grid(linestyle='--')
    
    
    n = 2
    title_lab  = "3 body mass"
    plt.subplot(nx,ny,n)
    ax = plt.gca()
    h = ax.hist(
            M3,
            bins      = m_bins,
            range     = [100,140],
            histtype  = 'step',
            color     = COL,
            stacked   = True,
            weights   = weight,
            label     = legend_lab,
            #linestyle = line_style[k],
            linewidth = 1.2
            )

    #if(KK == 0 and k==0 and i == 0 ):
    #    y2,x2 = h[0],h[1][1:]
    #    a = [800,90,10]
    #    fit2 = curve_fit(gauss,x2,y2,p0 =a)
    ax.legend(prop={'size': 10})
    ax.set_title(title_lab)
    ax.set_xlabel(r"$m(b+bbar)[GeV]$")
    ax.grid(linestyle='--')
    
plt.show()
fig.savefig(figpath+"Mass.png")


# In[13]:


fig = plt.figure(figsize = (16,8))
#h = [[np.array([0,0]) for _ in range(len(data))] for _ in range(len(label_trig[k][0]))]

nx,ny = 1,2
n = 1
plt.subplot(nx,ny,n)
M2         = dijetm#[i]
M3         = dijetgmm#[i]
legend_lab = listSamples#[i]
title_lab  = "2 body mass"
COL        = colors[0:len(M2)]#[i]
bHiggs     = 20
rHiggs     = [80,200]
#weight     = np.array([w[i] for ii in range(len(M2))])
weight     = np.array([[w[ii] for i in range(len(M2[ii]))]for ii in range(len(M2))])

ax = plt.gca()
h = ax.hist(
        M2,
        bins      = m_bins,
        range     = [50,125],
        #range     = [0,200],
        histtype  = 'step',
        color     = COL,
        stacked = True,
        weights   = weight,
        label     = legend_lab,
        #linestyle = line_style[k],
        linewidth = 1.2
        )

#if(KK == 0 and k==0 and i == 0 ):
#    y2,x2 = h[0],h[1][1:]
#    a = [800,90,10]
#    fit2 = curve_fit(gauss,x2,y2,p0 =a)
ax.legend(prop={'size': 10})
ax.set_title(title_lab)
ax.set_xlabel(r"$m(b+bbar)[GeV]$")
ax.grid(linestyle='--')
  
    
n = 2
title_lab  = "3 body mass"
plt.subplot(nx,ny,n)
ax = plt.gca()
h = ax.hist(
        M3,
        bins      = m_bins,
        range     = [100,140],
        histtype  = 'step',
        color     = COL,
        stacked   = True,
        weights   = weight,
        label     = legend_lab,
        #linestyle = line_style[k],
        linewidth = 1.2
        )

#if(KK == 0 and k==0 and i == 0 ):
#    y2,x2 = h[0],h[1][1:]
#    a = [800,90,10]
#    fit2 = curve_fit(gauss,x2,y2,p0 =a)
ax.legend(prop={'size': 10})
ax.set_title(title_lab)
ax.set_xlabel(r"$m(b+bbar)[GeV]$")
ax.grid(linestyle='--')    

    
    
plt.show()
fig.savefig(figpath+"Mass.png")


# # Muon

# In[14]:


print("Transverse mass of W "+str(80**2)) # Transverse mass of Wp
print("Transverse mass of Mu "+str((0.105**2) + (80.0/2)**2)) # Transverse mass of mu, for Wpt = 0

plt.figure(figsize= (15,8))
for i in range(len(data)):
    plt.subplot(1,2,1)
    plt.hist(
            data[i].lep1_Mt2,
            range = [0,10000],
            bins = 40,
            histtype = 'step',
            linewidth = 1.2,
            label     = listSamples[i],
            color = colors[i]
            )
    plt.title(r"$\mu \  M_t^2$ from the W decay")
    plt.xlabel(r"$M_t^2$")
    plt.legend()
    plt.grid(True,linestyle = '--')

    plt.subplot(1,2,2)
    plt.hist(data[i].lepton_pt,
            range = [0,200],
            bins = 40,
            histtype = 'step',
            linewidth = 1.2,
            label     = listSamples[i],
            color = colors[i]
            )
    plt.title(r"$\mu \  p_t$ from the W decay")
    plt.xlabel(r"$p_t$")
    plt.legend()
    plt.grid(True,linestyle = '--')
    

plt.show()


# # BBBAR PT

# In[15]:




fig = plt.figure(figsize = (15, 20))
for i in range(len(data)):
    for j in range(len(pt)):
        nx,ny = 3,2
        plt.subplot(nx,ny,j+1)#j*2+1)   
        #print(k,0,j,i)                    
        PT = pt[j][i]
        title_lab = label_part[j]
        legend_lab = listSamples[i]
        weight = np.array([w[i] for _ in PT]) 
        COL = colors[i]

        ax = plt.gca()
        ax.hist(
                                    PT,
                                    bins      = pt_bins[j],
                                    histtype  = "step",
                                    range     = [0,max_ranges[j]],
                                    normed    = False,
                                    color     = COL,
                                    weights   = weight,
                                    label     = legend_lab,
                                    #linestyle = line_style[k],
                                    linewidth = 1.2
                                    )
        #ax.axvline(17,linestyle='--',color = 'r',alpha = 0.5)
        #ax.axvline(8,linestyle='--',color = 'r',alpha = 0.5)
        ax.set_title(title_lab)
        ax.set_xlabel(r'$p_t[GeV]$')
        ax.grid(linestyle='--')
        ax.legend(prop={'size':10})

plt.show()
fig.savefig(figpath+"PT.png")


# In[16]:




fig = plt.figure(figsize = (15, 20))
for i in range(len(data)):
    for j in range(len(pt)):
        nx,ny = 3,2
        plt.subplot(nx,ny,j+1)#j*2+1)   
        #print(k,0,j,i)                    
        PT = pt[j][i]
        title_lab = label_part[j]
        legend_lab = listSamples[i]
        weight = np.array([w[i] for _ in PT]) 
        COL = colors[i]

        ax = plt.gca()
        ax.hist(
                                    PT,
                                    bins      = pt_bins[j],
                                    histtype  = "step",
                                    range     = [0,max_ranges[j]],
                                    normed    = True,
                                    color     = COL,
                                    weights   = weight,
                                    label     = legend_lab,
                                    #linestyle = line_style[k],
                                    linewidth = 1.2
                                    )
        #ax.axvline(17,linestyle='--',color = 'r',alpha = 0.5)
        #ax.axvline(8,linestyle='--',color = 'r',alpha = 0.5)
        ax.set_title(title_lab)
        ax.set_xlabel(r'$p_t[GeV]$')
        ax.grid(linestyle='--')
        ax.legend(prop={'size':10})

plt.show()
fig.savefig(figpath+"PT.png")


# # ETA

# In[17]:




fig = plt.figure(figsize = (15, 20))
for i in range(len(data)):
    for j in range(len(eta)):
        nx,ny = 3,2
        plt.subplot(nx,ny,j+1)#j*2+1)   
        #print(k,0,j,i)                    
        ETA = eta[j][i]
        title_lab = label_part[j]
        legend_lab = listSamples[i]
        weight = np.array([w[i] for _ in ETA]) 
        COL = colors[i]

        ax = plt.gca()
        ax.hist(
                                    ETA,
                                    #bins      = eta_bins[j],
                                    histtype  = "step",
                                    #range     = [0,max_ranges[j]],
                                    normed    = False,
                                    color     = COL,
                                    weights   = weight,
                                    label     = legend_lab,
                                    #linestyle = line_style[k],
                                    linewidth = 1.2
                                    )
        #ax.axvline(17,linestyle='--',color = 'r',alpha = 0.5)
        #ax.axvline(8,linestyle='--',color = 'r',alpha = 0.5)
        ax.set_title(title_lab)
        ax.set_xlabel(r'$p_t[GeV]$')
        ax.grid(linestyle='--')
        ax.legend(prop={'size':10})

plt.show()
fig.savefig(figpath+"ETA.png")


# # Phi

# In[18]:




fig = plt.figure(figsize = (15, 20))
for i in range(len(data)):
    for j in range(len(eta)):
        nx,ny = 3,2
        plt.subplot(nx,ny,j+1)#j*2+1)   
        #print(k,0,j,i)                    
        PHI = phi[j][i]
        title_lab = label_part[j]
        legend_lab = listSamples[i]
        weight = np.array([w[i] for _ in PHI]) 
        COL = colors[i]

        ax = plt.gca()
        ax.hist(
                PHI,
                #bins      = eta_bins[j],
                histtype  = "step",
                #range     = [0,max_ranges[j]],
                normed    = False,
                color     = COL,
                weights   = weight,
                label     = legend_lab,
                #linestyle = line_style[k],
                linewidth = 1.2
                )
        #ax.axvline(17,linestyle='--',color = 'r',alpha = 0.5)
        #ax.axvline(8,linestyle='--',color = 'r',alpha = 0.5)
        ax.set_title(title_lab)
        ax.set_xlabel(r'$p_t[GeV]$')
        ax.grid(linestyle='--')
        ax.legend(prop={'size':10})

plt.show()
fig.savefig(figpath+"ETA.png")


# # Delta  ETA

# In[19]:


fig = plt.figure(figsize = (16,28))

for i in range(len(data)): 
    for j in range(len(d_eta)):
        ny,nx,n = 3,2, 1
        sizeLeg = 10
        plt.subplot(ny,nx,j+1)
        DELTA_ETA  = d_eta[j][i]
        title_lab  = title_d_eta[j]
        legend_lab = listSamples[i]
        weight     = np.array([w[i] for _ in DELTA_ETA]) 
        COL        = colors[i]

        ax = plt.gca()
        ax.hist(
                DELTA_ETA,
                bins      = 100,
                range     = [-np.pi,np.pi],
                histtype  = 'step',
                normed    = False,
                color     = COL,
                weights   = weight,
                label     = legend_lab,#label_trig[k][0][i],
                #linestyle = line_style[k],#linestyle= LIN,
                linewidth = 1.2
                )
        ax.legend(prop={'size':sizeLeg})
        #ax.set_title(label_part[j]+" eta")
        ax.set_title(title_lab)
        ax.set_xlabel(r"$\eta$")
        ax.grid(linestyle='--')
plt.show()
fig.savefig(figpath+"DeltaEta.png")


# # Delta BBBAR PHI

# In[20]:


fig = plt.figure(figsize = (16,28))

for i in range(len(data)): 
    for j in range(len(d_phi)):
        ny,nx,n = 3,2, 1
        sizeLeg = 10
        plt.subplot(ny,nx,j+1)
        DELTA_PHI  = d_phi[j][i]
        title_lab  = title_d_phi[j]
        legend_lab = listSamples[i]
        weight     = np.array([w[i] for _ in DELTA_PHI]) 
        COL        = colors[i]

        ax = plt.gca()
        ax.hist(
                DELTA_PHI,
                bins      = 100,
                range     = [-np.pi,np.pi],
                histtype  = 'step',
                normed    = False,
                color     = COL,
                weights   = weight,
                label     = legend_lab,#label_trig[k][0][i],
                #linestyle = line_style[k],#linestyle= LIN,
                linewidth = 1.2
                )
        ax.legend(prop={'size':sizeLeg})
        #ax.set_title(label_part[j]+" eta")
        ax.set_title(title_lab)
        ax.set_xlabel(r"$\phi$")
        ax.grid(linestyle='--')
plt.show()
fig.savefig(figpath+"DeltaPhi.png")


# # DELTA R

# In[21]:


fig = plt.figure(figsize = (16,28))


for i in range(len(data)): 
    for j in range(len(d_R)):
        ny,nx,n = 3,2, 1
        sizeLeg = 10
        plt.subplot(ny,nx,j+1)
        DELTA_R  = d_R[j][i]
        title_lab  = title_d_R[j]
        legend_lab = listSamples[i]
        weight     = np.array([w[i] for _ in DELTA_R]) 
        COL        = colors[i]

        ax = plt.gca()
        ax.hist(
                DELTA_R,
                bins      = 100,
                range     = [0,6],
                histtype  = 'step',
                normed    = False,
                color     = COL,
                weights   = weight,
                label     = legend_lab,#label_trig[k][0][i],
                #linestyle = line_style[k],#linestyle= LIN,
                linewidth = 1.2
                )
        ax.legend(prop={'size':sizeLeg})
        #ax.set_title(label_part[j]+" eta")
        ax.set_title(title_lab)
        ax.set_xlabel(r"$R$")
        ax.grid(linestyle='--')
plt.show()
fig.savefig(figpath+"DeltaR.png")


# In[22]:


V = [np.array(pt[1][i])/np.array(m[5][i]) for i in range(len(m[0]))]


# In[23]:


plt.figure(figsize = (10,10))
for i in range(len(V)):
    plt.hist(V[i],
            normed = True,
            range = [0,1.5],
            histtype = 'step',
             linewidth = 1.5,
             label = listSamples[i]
            )
    plt.title(r'$\frac{p_T}{m_{jj\gamma}}$')
    plt.legend()
    plt.grid(True)
plt.show()

print(15/110)

