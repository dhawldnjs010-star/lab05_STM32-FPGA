import re, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fp='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(fp); plt.rcParams['font.family']=fm.FontProperties(fname=fp).get_name()
plt.rcParams.update({'font.size':6.5})
BLUE='#1f5f99'; GREY='#8b95a1'; INK='#1f2933'
L='repo/evidence/pre/fw/'
t3=open(L+'fw_log_task3.txt').read(); t4=open(L+'fw_log_task4.txt').read()
tog=[int(x)/1000 for x in re.findall(r'TOGGLE t=(\d+)',t3)]
press=[3,10,22,30,50]
fig,axs=plt.subplots(2,1,figsize=(8.4/2.54,2.6),dpi=300,gridspec_kw={'height_ratios':[1,1]})
ax=axs[0]; xs=[0]; ys=[0]; v=0
for t in tog: xs+=[t,t]; ys+=[v,1-v]; v=1-v
xs.append(60); ys.append(v)
ax.plot(xs,ys,color=BLUE,lw=0.9)
labels={3:'2 s',10:'4 s',22:'8 s',30:'1 s',50:'2 s'}
for p in press:
    ax.axvline(p,color=GREY,lw=0.5,ls=(0,(2,2))); ax.text(p+0.4,1.12,labels[p],fontsize=5.8,color=INK)
ax.text(0.4,1.12,'1 s',fontsize=5.8,color=INK)
ax.set_ylim(-0.2,1.35); ax.set_yticks([0,1]); ax.set_yticklabels(['꺼짐','켜짐']); ax.set_title('과제3 · PA5 (TIM6 100 ms 계수)',loc='left',fontsize=7,pad=2)
cc=[(int(t)/1000,int(c)) for t,c in re.findall(r'CCR t=(\d+) ccr=(\d+)',t4)]
ax=axs[1]; xs=[];ys=[]
for i,(t,c) in enumerate(cc):
    t2=cc[i+1][0] if i+1<len(cc) else 60
    xs+=[t,t2]; ys+=[c/10,c/10]
ax.plot(xs,ys,color=BLUE,lw=0.9)
for p in press: ax.axvline(p,color=GREY,lw=0.5,ls=(0,(2,2)))
ax.set_ylim(0,90); ax.set_yticks([25,50,75]); ax.set_yticklabels(['25%','50%','75%']); ax.set_title('과제4 · PB4 PWM 비율 (비교값/1000)',loc='left',fontsize=7,pad=2)
ax.set_xlabel('가상 시간 (s) · 점선: 버튼 호출 (3 s는 30 ms 간격 3회)',color='#5f6b7a',fontsize=6)
for a in axs:
    a.set_xlim(0,60)
    for s in ('top','right'): a.spines[s].set_visible(False)
    a.tick_params(length=2,width=0.5,colors='#5f6b7a')
fig.tight_layout(h_pad=0.5); fig.savefig('fig/fw_timeline.png')
