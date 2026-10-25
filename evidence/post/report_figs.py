import csv, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image, ImageDraw, ImageFont
fp='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; fb='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
fm.fontManager.addfont(fp); plt.rcParams.update({'font.family':fm.FontProperties(fname=fp).get_name(),'font.size':7})
BLUE='#1F5F99'; GREY='#5F6B7A'
# 1) task3 timeline
t=[];o=[]
for r in csv.DictReader(open('t3_trace.csv')):
    t.append(float(r['t_s'])); o.append(int(r['ld2_on']) if r['ld2_on']!='' else 0)
# 0.3 s 미만의 판독 끊김(손가락·각도로 LED가 잠깐 안 보인 프레임)은 앞 상태로 메운다
import itertools
runs=[(k,len(list(g))) for k,g in itertools.groupby(o)]; o2=[]
for idx,(k,n) in enumerate(runs):
    if n<3 and 0<idx<len(runs)-1: k=runs[idx-1][0]
    o2+= [k]*n
o=o2
fig,ax=plt.subplots(figsize=(3.6,1.45),dpi=300)
ax.step(t,o,where='post',color=BLUE,lw=1.0)
labels=[(0.3,3.3,'1 s'),(3.3,7.3,'2 s'),(7.3,15.3,'4 s'),(15.3,31.3,'8 s'),(31.3,34.4,'1 s')]
for a,b,l in labels:
    ax.annotate('',xy=(a,1.22),xytext=(b,1.22),arrowprops=dict(arrowstyle='<->',lw=0.5,color=GREY))
    ax.text((a+b)/2,1.3,l,ha='center',fontsize=6.3,color='#1F2933')
ax.set_ylim(-0.15,1.55); ax.set_yticks([0,1]); ax.set_yticklabels(['꺼짐','켜짐']); ax.set_xlim(0,34.5)
ax.set_xlabel('영상 시각 (s)',color=GREY)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.tick_params(length=2,width=0.5,colors=GREY)
fig.tight_layout(pad=0.3); fig.savefig('fig/task3_timeline.png'); plt.close(fig)

def lab(im,txt,sz=22):
    d=ImageDraw.Draw(im); f=ImageFont.truetype(fb,sz); w=d.textlength(txt,font=f)
    d.rectangle((0,0,w+14,sz+12),fill=(31,95,153)); d.text((7,3),txt,font=f,fill='white'); return im
def grid(items,cols,out,cw,ch):
    rows=(len(items)+cols-1)//cols; c=Image.new('RGB',(cols*cw+(cols-1)*8,rows*ch+(rows-1)*8),'white')
    for k,(im,txt) in enumerate(items):
        im=im.resize((cw,ch)); lab(im,txt); c.paste(im,((k%cols)*(cw+8),(k//cols)*(ch+8)))
    c.save(out,quality=85)
# 2) task4 scope
items=[(Image.open(f't4f/{i:03d}.png').crop((480,250,960,560)),txt) for i,txt in ((2,'0.1 s · 25%'),(14,'1.3 s · 50%'),(22,'2.1 s · 75%'),(30,'2.9 s · 25%'))]
grid(items,2,'fig/task4_scope.jpg',480,310)
# 3) traffic
tr=lambda i: Image.open(f'trf/{i:03d}.png').crop((600,60,1350,700))
items=[(tr(1),'0.0 s 점멸 켜짐'),(tr(2),'0.5 s 점멸 꺼짐'),(tr(13),'6 s 방향 0 초록'),(tr(30),'14.5 s 노랑'),(tr(37),'18 s 방향 1'),(tr(65),'32 s 방향 2')]
grid(items,3,'fig/traffic_frames.jpg',375,320)
# 4) ADC
ad=lambda t: Image.open(f'adcf/a_{t}.png').crop((330,650,700,1300))
items=[(ad(t),f'{t} s') for t in (1,4,10,16,19)]
grid(items,5,'fig/adc_frames.jpg',185,325)
