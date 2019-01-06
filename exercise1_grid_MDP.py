#coding=utf-8
import os, sys, traceback, random

'''
S状态空间：0-15
A动作：四个方向
P状态概率转移：均匀概率
π策略：随机策略
R即时奖励：R(0)=R(15)=1,R(x)=0(1-14)
价值函数：V(s)
'''

s_t=[i for i in range(16)]
a_t={'s':4,'n':-4,'e':-1,'w':1}
v_t=[0 for i in range(16)]
lam=1.0
def NextState(s, a):
    global s_t, a_t, v_t, lam
    if (s / 4 == 0 and a == 'n') or (s % 4 == 0 and a == 'e') or (s % 4 == 3 and a == 'w') or (s >= 12 and a == 's'):
        return s
    return s + a_t[a]

def Reward(s):
    if s == 0 or s == 15: return 0
    return -1

def ValueIteration(s):
    global s_t, a_t, v_t, lam
    #terminators return
    if s == 0 or s == 15: return 0.0
    new_v_t = 0
    for a in a_t:
        next_state = NextState(s,a)
        try:
            new_v_t +=  1/4.0 * (Reward(next_state) + lam*v_t[next_state])
            #print s, next_state, new_v_t
        except:
            print traceback.format_exc()
            raise()
    return new_v_t

def Print(v):
    outs = ''
    for i in range(16):
        if i % 4 == 0:
            outs += '\n' + str(v[i])
        else:
            outs += ' '+ str(v[i])
    #outs += '\n'
    print outs
if __name__ == '__main__':
    #global s_t, a_t, v_t, lam

    max_epoch = 160  #about 150
    for i in range(0, max_epoch):
        new_v_t = [0 for x in range(16)]
        for j in range(0,16):
            new_v_t[j] = ValueIteration(j)
        v_t = new_v_t
        Print(v_t)


