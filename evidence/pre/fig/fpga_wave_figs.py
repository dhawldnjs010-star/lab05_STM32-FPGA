import re, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Polygon
fp='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(fp); plt.rcParams['font.family']=fm.FontProperties(fname=fp).get_name()
plt.rcParams.update({'font.size':6.5,'axes.unicode_minus':False})
INK='#1f2933'; BLUE='#1f5f99'; GREY='#8b95a1'; LIGHT='#e8edf2'
W=8.4/2.54
R='repo/fpga'

def vcd(path):
    ids={}; sig={}; t=0; scope=[]
    for line in open(path):
        s=line.strip()
        if s.startswith('$scope'): scope.append(s.split()[2]); continue
        if s.startswith('$upscope'): scope.pop(); continue
        m=re.match(r'\$var \w+ (\d+) (\S+) (\S+)',s)
        if m:
            name='.'.join(scope+[m.group(3)]); ids.setdefault(m.group(2),[]).append(name); sig[name]=[]; continue
        if s.startswith('#'): t=int(s[1:])//1000; continue   # ps -> ns
        m=re.match(r'b([01xz]+) (\S+)$',s)
        if m and m.group(2) in ids:
            v=m.group(1); v=int(v,2) if set(v)<=set('01') else None
            for n in ids[m.group(2)]: sig[n].append((t,v)); continue
        m=re.match(r'([01xz])(\S+)$',s)
        if m and m.group(2) in ids:
            v=int(m.group(1)) if m.group(1) in '01' else None
            for n in ids[m.group(2)]: sig[n].append((t,v))
    return sig
def at(ev,t):
    v=None
    for tt,x in ev:
        if tt<=t: v=x
        else: break
    return v
def runs(ev,t0,t1):
    out=[]; v=at(ev,t0); a=t0
    for tt,x in ev:
        if t0<tt<t1 and x!=v: out.append((a,tt,v)); a=tt; v=x
    out.append((a,t1,v)); return out

def wave(sig,rows,t0,t1,fname,fmt=None,marks=()):
    fmt=fmt or {}
    fig,ax=plt.subplots(figsize=(W,0.36*len(rows)+0.5),dpi=300)
    n=len(rows)
    for i,(label,key,kind) in enumerate(rows):
        y=n-1-i; ev=sig[key]
        if kind=='bit':
            xs=[];ys=[]
            for a,b,v in runs(ev,t0,t1):
                v=v or 0; xs+= [a,b]; ys+=[y-0.22+0.44*v]*2
            ax.plot(xs,ys,color=BLUE,lw=0.9)
        else:
            span=t1-t0; d=span*0.006
            for a,b,v in runs(ev,t0,t1):
                h=0.26
                ax.add_patch(Polygon([(a,y),(a+d,y+h),(b-d,y+h),(b,y),(b-d,y-h),(a+d,y-h)],closed=True,fc=LIGHT,ec=BLUE,lw=0.6))
                txt='?' if v is None else (fmt.get(key,'{}').format(v))
                if (b-a)>span*0.045: ax.text((a+b)/2,y,txt,ha='center',va='center',color=INK,fontsize=5.6)
        ax.text(t0-(t1-t0)*0.015,y,label,ha='right',va='center',color=INK,fontsize=6.3)
    for x,txt in marks:
        ax.axvline(x,color=GREY,lw=0.5,ls=(0,(2,2)))
        if txt: ax.text(x,n-0.45,txt,ha='center',va='bottom',fontsize=5.6,color=GREY)
    ax.set_xlim(t0,t1); ax.set_ylim(-0.6,n-0.2+ (0.35 if marks else 0)); ax.set_yticks([])
    for s in ('top','right','left'): ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#8a96a3'); ax.tick_params(axis='x',length=2,colors='#5f6b7a',labelsize=5.8)
    ax.set_xlabel('시뮬레이션 시간 (ns)',fontsize=6,color='#5f6b7a')
    fig.tight_layout(pad=0.3); fig.savefig('fig/'+fname); plt.close(fig)

# piano: 도 시작부터 레로 바뀐 직후까지
s=vcd(f'{R}/piano/evidence/pre/wave.vcd')
ks=[(t,v) for t,v in s['tb.key'] if v in (0x80,0x40)]
t_do=ks[0][0]; t_re=[t for t,v in ks if v==0x40][0]
wave(s,[('key','tb.key','bus'),('piezo','tb.piezo','bit')],t_do-20,t_re+260,'piano_wave.png',
     fmt={'tb.key':'{:02X}','tb.dut.u_tone.count':'{}'},marks=[(t_do,'도 (19클록 반주기)'),(t_re,'레 (17)')])
print('piano', t_do, t_re)
# traffic: 방향 0의 13단계 + 방향 1 시작
s=vcd(f'{R}/traffic/evidence/pre/wave.vcd')
t0=[t for t,v in s['tb.rst'] if v==0][0]
wave(s,[('direction','tb.dut.direction','bus'),('phase','tb.dut.phase','bus'),('green','tb.green','bus'),('yellow','tb.yellow','bus'),
        ('walk_green','tb.wg','bus'),('blink','tb.dut.blink','bit')],t0,t0+13*40+60,'traffic_wave.png',
     fmt={'tb.green':'{:04b}','tb.yellow':'{:04b}','tb.wg':'{:04b}'},marks=[(t0+4*40,'보행 점멸'),(t0+11*40,'노랑'),(t0+13*40,'방향 1')])
print('traffic',t0)
# adc: 첫 프레임
s=vcd(f'{R}/adc/evidence/pre/wave.vcd')
fall=[t for t,v in s['tb.cs_n'] if v==0][0]; rise=[t for t,v in s['tb.cs_n'] if v==1 and t>fall][0]
wave(s,[('cs_n','tb.cs_n','bit'),('sclk','tb.sclk','bit'),('mosi','tb.mosi','bit'),('miso','tb.miso','bit'),('valid','tb.valid','bit'),('sample','tb.sample','bus')],
     fall-30,rise+140,'adc_wave.png',fmt={'tb.sample':'{:03X}'})
print('adc',fall,rise)
