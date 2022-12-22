import networkx as nx
import matplotlib.pyplot as plp
import math
import operator
import pylab
import random
import datetime

starttime = datetime.datetime.now()#开始计时
G = nx.Graph()
allpath="./datasets/filelist_dataset.txt"
allpathlist=''
#nodenumber表示节点数，ordervalue,是算法的排序的结果值，列表形式
def dm_metric(nodenumber,ordervalue):
    result_dm=len(set(ordervalue))*1.0/nodenumber
    return result_dm
def M_metric(nodenumber,ordervalue):
    dist_r=set(ordervalue)

    nr=0
    all_nr=0
    for item in dist_r:
        nr=list(ordervalue).count(item)
        all_nr=all_nr+nr*(nr-1)

    res=(1-(all_nr/(nodenumber*(nodenumber-1))))**2
    return res

def simjkd(u, v):        
    set_v = set( G.neighbors(v))
    set_v.add(v)
    set_u = set( G.neighbors(u))
    set_u.add(u)
    jac = len(set_v & set_u) * 1.0 / len(set_v | set_u)    
    return jac

def convert_shell(shelldict):
    resdict={}
    for key,valuelist in shelldict.items():
        for vlist in valuelist:
            resdict.setdefault(vlist,key)
    return resdict
with open(allpath,'r') as f:
    allpathlist=f.readlines()
    f.close()
pathfile=''
for pt in allpathlist:
    pt=pt.strip('\n')
    pathfile="./datasets/"+pt+'/data/'+pt+'.txt'
    G.clear()
    
    with open(pathfile) as file:
        for line in file:
            head, tail = [int(x) for x in line.split()]
            G.add_edge(head, tail)
    file.close()
    G=G.to_undirected()
    G.remove_edges_from(nx.selfloop_edges(G))
    #The degree of nodes
    deg = G.degree()

    N = G.number_of_nodes()   
    max_deg = max(dict(deg).values())

      
    CC=nx.clustering(G)
    k_shell=nx.core_number(G)
    maxk_shell=max(k_shell.values())
    mink_shell=min(k_shell.values())
    #Initial  Information of Nodes，type，dict，node：value
    IIv={}
    I1v={} #一阶信息量
    I2v={}#二阶信息量
    allinfo={}#节点的最终信息

    for node in G.nodes():

        value=1.0*deg[node]/max_deg+1.0*k_shell[node]/maxk_shell

        IIv.setdefault(node,value)
     
    print('IIv down')
    for v in G.nodes():  
        value1=IIv[v]
       
        for u in G.neighbors(v):       

            Juv=simjkd(v,u)            

            ccuv=(1-CC[u])

            if k_shell[u]>k_shell[v]:
                info_t=IIv[u]*ccuv*Juv*(k_shell[u]/(maxk_shell-mink_shell))
            if k_shell[u]<k_shell[v]:
                info_t=IIv[u]*ccuv*Juv*(k_shell[u]/(maxk_shell+mink_shell))
            if k_shell[u]==k_shell[v]:
                info_t=IIv[u]*ccuv*Juv*(k_shell[u]/maxk_shell)     

            value1+=info_t
        I1v.setdefault(v,value1)
    print('I1v down')
    for v in G.nodes():  
        value2=0
        for u in G.neighbors(v):           
            value2+=I1v[u]

        I2v.setdefault(v,value2)
    print('I2v down')
    for v in G.nodes(): 
        allinfo.setdefault(v,I2v[v]+IIv[v])

    sort_val_vniid = sorted(allinfo.items(), key=lambda x: x[1], reverse=True) 

    nodes,val=map(list,zip(*sort_val_vniid))

    endtime = datetime.datetime.now()#结束时间
    time_cost = (endtime - starttime).seconds #初始迭代时间
    print('time',time_cost)
    #dm指标结果
    files="./datasets/"+pt+'/sir_alg/IDME_'+pt+'.txt'
    f1 =open(files , "w+")
    for key,val in sort_val_vniid:
       f1.write(str(key)+'\t'+str(val)+"\n")   
    
    f1.close()
    res_dm=dm_metric(G.number_of_nodes(),allinfo.values())
    res_m=M_metric(G.number_of_nodes(),allinfo.values())
    print(pt.strip('\n')+'DM Metric value:',res_dm)
    #m指标结果
    print(pt.strip('\n')+'M Metric value:',res_m)    
