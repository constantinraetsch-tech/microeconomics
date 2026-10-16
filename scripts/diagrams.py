import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT="/home/claude/out/images/"
BLUE="#2563eb"; RED="#dc2626"; GREEN="#16a34a"; GREY="#6b7280"; ORANGE="#ea580c"
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
def save(fig,name):
    fig.tight_layout(); fig.savefig(OUT+name,dpi=130,facecolor="white"); plt.close(fig)

# 1 surplus basic (Qd=120-2p, Qs=20+3p) -> p=20,Q=80 ; plot p on y
def base(ax,title):
    ax.set_xlabel("Q"); ax.set_ylabel("p"); ax.set_title(title,fontsize=12)
Q=np.linspace(0,120,200)
fig,ax=plt.subplots(figsize=(6,4.2))
pd=lambda q:(120-q)/2; ps=lambda q:(q-20)/3
ax.plot(Q,pd(Q),color=BLUE,label="Demand: Qd = 120 − 2p")
q2=np.linspace(20,120,100); ax.plot(q2,ps(q2),color=RED,label="Supply: Qs = 20 + 3p")
ax.plot([0,20],[0,0],color=RED)
qq=np.linspace(0,80,100)
ax.fill_between(qq,20,pd(qq),color=BLUE,alpha=.2,label="CS = 1,600")
ax.fill_between(qq,np.maximum(ps(qq),0),20,color=RED,alpha=.2,label="PS = 1,000 (trapezoid)")
ax.plot([80,80],[0,20],"k:",[0,80],[20,20],"k:"); ax.plot(80,20,"ko")
ax.annotate("E (80, 20)",(80,20),(88,27))
ax.set_xlim(0,125); ax.set_ylim(0,62); base(ax,"Consumer & producer surplus"); ax.legend(fontsize=9,loc="upper right")
save(fig,"surplus-basic.png")

# 2 price ceiling (Peking duck Qd=80-2p, Qs=-20+3p) p*=20 Q*=40; ceiling 12
fig,ax=plt.subplots(figsize=(6.4,4.4))
Q=np.linspace(0,80,200); pd=lambda q:(80-q)/2; ps=lambda q:(q+20)/3
ax.plot(Q,pd(Q),color=BLUE,label="D: Qd = 80 − 2p"); ax.plot(Q,ps(Q),color=RED,label="S: Qs = −20 + 3p")
ax.axhline(12,color="k",lw=1.4); ax.text(66,12.6,"p max = 12")
q1=np.linspace(0,16,50)
ax.fill_between(q1,12,pd(q1),color=BLUE,alpha=.22,label="CS = 384")
ax.fill_between(q1,ps(q1),12,color=RED,alpha=.22,label="PS = 42.7")
q3=np.linspace(16,40,50); ax.fill_between(q3,ps(q3),pd(q3),color=GREY,alpha=.35,label="DWL = 240")
for x in (16,40,56): ax.plot([x,x],[0,pd(x) if x!=56 else 12],"k:")
ax.annotate("",(56,5),(16,5),arrowprops=dict(arrowstyle="<->",color=ORANGE)); ax.text(28,2.5,"shortage = 40",color=ORANGE)
ax.plot(16,32,"o",color=BLUE); ax.text(17,32.5,"WTP = 32")
ax.set_xlim(0,82); ax.set_ylim(0,42); ax.set_xticks([0,16,40,56,80]); base(ax,"Binding price ceiling (Seminar 2, Q4)"); ax.legend(fontsize=8.5)
save(fig,"price-ceiling.png")

# 3 price floor generic
fig,ax=plt.subplots(figsize=(6.2,4.2))
Q=np.linspace(0,100,200); pd=lambda q:100-q; ps=lambda q:q
ax.plot(Q,pd(Q),color=BLUE,label="D"); ax.plot(Q,ps(Q),color=RED,label="S")
pm=65; qd=35; qs=65
ax.axhline(pm,color="k",lw=1.4); ax.text(2,pm+1.5,"p min")
q1=np.linspace(0,qd,50)
ax.fill_between(q1,pm,pd(q1),color=BLUE,alpha=.22,label="CS (smaller)")
ax.fill_between(q1,ps(q1),pm,color=RED,alpha=.22,label="PS (bigger or smaller?)")
q3=np.linspace(qd,50,50); ax.fill_between(q3,ps(q3),pd(q3),color=GREY,alpha=.35,label="DWL")
ax.annotate("",(qs,8),(qd,8),arrowprops=dict(arrowstyle="<->",color=ORANGE)); ax.text(40,3,"excess supply (surplus)",color=ORANGE)
for x in (qd,50,qs): ax.plot([x,x],[0,max(pd(x),ps(x)) if x!=qs else pm],"k:")
ax.set_xticks([qd,50,qs]); ax.set_xticklabels(["Qd","Q*","Qs"]); ax.set_yticks([50,pm]); ax.set_yticklabels(["p*","p min"])
ax.set_xlim(0,100); ax.set_ylim(0,100); base(ax,"Binding price floor: Q traded = Qd"); ax.legend(fontsize=8.5,loc="upper right",bbox_to_anchor=(1,0.6))
save(fig,"price-floor.png")

# 4 quota apples Qd=200-2p, Qs=3p, quota 80
fig,ax=plt.subplots(figsize=(6.2,4.3))
Q=np.linspace(0,200,200); pd=lambda q:(200-q)/2; ps=lambda q:q/3
ax.plot(Q,pd(Q),color=BLUE,label="D: Qd = 200 − 2p"); ax.plot(Q[:150],ps(Q[:150]),color=RED,label="S: Qs = 3p")
ax.plot([80,80],[0,70],color="k",lw=1.4); ax.text(81,66,"quota = 80")
q1=np.linspace(0,80,50)
ax.fill_between(q1,60,pd(q1),color=BLUE,alpha=.22,label="CS = 1,600")
ax.fill_between(q1,ps(q1),60,color=RED,alpha=.22,label="PS = 3,733")
q3=np.linspace(80,120,50); ax.fill_between(q3,ps(q3),pd(q3),color=GREY,alpha=.35,label="DWL = 667")
ax.plot([0,80],[60,60],"k:",[0,120],[40,40],"k:",[120,120],[0,40],"k:")
ax.set_yticks([26.67,40,60,100]); ax.set_xticks([0,80,120,200])
ax.set_xlim(0,202); ax.set_ylim(0,102); base(ax,"Production quota (Seminar 3, Q3)"); ax.legend(fontsize=8.5)
save(fig,"production-quota.png")

# 5 minimum wage Ld=6000-4w, Ls=2000+w, wmin=1000
fig,ax=plt.subplots(figsize=(6.4,4.3))
L=np.linspace(0,6000,200); wd=lambda l:(6000-l)/4
ax.plot(L,wd(L),color=BLUE,label="Labour demand (firms)")
l2=np.linspace(2000,6000,100); ax.plot(l2,l2-2000,color=RED,label="Labour supply (workers)")
ax.axhline(1000,color="k",lw=1.4); ax.text(4700,1030,"w min = 1,000")
ax.plot([5200,5200],[0,800],"k:",[0,5200],[800,800],"k:")
for x in (2000,3000): ax.plot([x,x],[0,1000],"k:")
ax.annotate("",(3000,150),(2000,150),arrowprops=dict(arrowstyle="<->",color=ORANGE)); ax.text(2050,40,"unemployment 1,000",color=ORANGE,fontsize=9)
ax.annotate("",(5200,300),(2000,300),arrowprops=dict(arrowstyle="<->",color=GREEN)); ax.text(3300,330,"job destruction 3,200",color=GREEN,fontsize=9)
ax.set_xticks([2000,3000,5200]); ax.set_yticks([800,1000,1500])
ax.set_xlim(0,6200); ax.set_ylim(0,1600); ax.set_xlabel("L (workers)"); ax.set_ylabel("w (€/month)"); ax.set_title("Minimum wage (Seminar 3, Q2)",fontsize=12); ax.legend(fontsize=8.5,loc="upper right")
save(fig,"minimum-wage.png")

# 6 linear demand elasticity regions Q=200-4p
fig,(ax,ax2)=plt.subplots(1,2,figsize=(9,3.8))
p=np.linspace(0,50,200); q=200-4*p
ax.plot(q,p,color=BLUE); ax.plot(100,25,"ko"); ax.text(103,26,"|ε| = 1  (p = a/2b = 25)")
ax.text(25,42,"elastic |ε| > 1",color=RED); ax.text(130,8,"inelastic |ε| < 1",color=GREEN)
ax.set_xlabel("Q"); ax.set_ylabel("p"); ax.set_title("Q = 200 − 4p: same slope, changing ε",fontsize=11)
ax2.plot(p,p*q,color=ORANGE); ax2.axvline(25,color="k",ls=":"); ax2.text(26,1000,"max revenue\nat ε = −1")
ax2.set_xlabel("p"); ax2.set_ylabel("Revenue = p·Q"); ax2.set_title("Revenue peaks at the midpoint",fontsize=11)
save(fig,"linear-demand-elasticity.png")

# 7 revenue rectangles elastic vs inelastic
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
for ax,(title,slope) in zip(axs,[("Elastic: price ↓ → revenue ↑",0.15),("Inelastic: price ↑ → revenue ↑",1.6)]):
    q=np.linspace(0,10,100)
    if slope<1:
        p1,p2=8,6.5; f=lambda p:(10-p)/slope*0.1; q1,q2=3,9
        d=lambda x: 8.45-0.15*x
        ax.plot(q,d(q),color=BLUE); p1,p2=d(3),d(9)
        ax.add_patch(plt.Rectangle((0,p2),3,p1-p2,color=RED,alpha=.3)); ax.text(0.5,(p1+p2)/2-.1,"−",fontsize=16)
        ax.add_patch(plt.Rectangle((3,0),6,p2,color=GREEN,alpha=.3)); ax.text(5.5,p2/2,"+",fontsize=16)
        ax.set_ylim(0,10)
    else:
        d=lambda x: 10-1.6*x
        ax.plot(q[:63],d(q[:63]),color=BLUE); qa,qb=4,3.4; pa,pb=d(qa),d(qb)
        ax.add_patch(plt.Rectangle((0,pa),qb,pb-pa,color=GREEN,alpha=.3)); ax.text(1.4,(pa+pb)/2-.2,"+",fontsize=16)
        ax.add_patch(plt.Rectangle((qb,0),qa-qb,pa,color=RED,alpha=.3)); ax.text(qb+.1,pa/2,"−",fontsize=14)
        ax.set_ylim(0,10); ax.set_xlim(0,7)
    ax.set_title(title,fontsize=11); ax.set_xlabel("Q"); ax.set_ylabel("p")
save(fig,"revenue-rectangles.png")

# 8 joint PPF company Seminar1 Q2  (B horizontal, I vertical)
fig,ax=plt.subplots(figsize=(5.8,4))
ax.plot([0,400,1000],[300,200,0],color=BLUE,lw=2)
ax.plot(400,200,"ko"); ax.annotate("kink (400, 200)\nEldorado makes only bars",(400,200),(430,230),fontsize=9)
ax.text(120,262,"slope −1/4 (Eldorado)",fontsize=9); ax.text(650,120,"slope −1/3 (Navojoa)",fontsize=9)
ax.set_xlabel("Chocolate bars (B)"); ax.set_ylabel("Ice cream cups (I)"); ax.set_xlim(0,1050); ax.set_ylim(0,330)
ax.set_title("Joint PPF: lowest OC producer first",fontsize=12)
save(fig,"joint-ppf.png")

# 9 four cases of double shifts (table-like)
fig,axs=plt.subplots(2,2,figsize=(8.4,6.4))
cases=[("D ↑ and S ↑","Q ↑, P ?",1,1),("D ↑ and S ↓","P ↑, Q ?",1,-1),("D ↓ and S ↑","P ↓, Q ?",-1,1),("D ↓ and S ↓","Q ↓, P ?",-1,-1)]
x=np.linspace(0,10,50)
for ax,(t,r,dd,ss) in zip(axs.flat,cases):
    ax.plot(x,10-x,color=BLUE); ax.plot(x,x,color=RED)
    ax.plot(x,10-x+1.8*dd,color=BLUE,ls="--"); ax.plot(x,x-1.8*ss,color=RED,ls="--")
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
    ax.set_title(f"{t}  →  {r}",fontsize=11); ax.set_xlabel("Q"); ax.set_ylabel("P")
fig.suptitle("Both curves shift: one variable is certain, the other is '?'",fontsize=12)
save(fig,"double-shifts.png")
print("ok")
