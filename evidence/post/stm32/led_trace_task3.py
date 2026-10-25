"""과제3 영상(손에 든 보드)에서 LD2(PA5) 켜짐을 판독: 항상 켜진 상단 초록 LED(기준점)에 대한
프레임 추출: ffmpeg -i <영상> -vf fps=10,scale=540:-2 frames/%04d.png (세로 영상 기준)
상대 위치(왼쪽 아래 약 (-95~-140, +60~+130) px, 540 px 폭 기준)에 초록 점이 있으면 켜짐."""
import sys, glob, numpy as np
from PIL import Image
from scipy import ndimage
fs=sorted(glob.glob(sys.argv[1]+'/*.png'))
st=[]
for i,f in enumerate(fs):
    a=np.asarray(Image.open(f)).astype(int); r,g,b=a[...,0],a[...,1],a[...,2]
    m=(g>160)&(g-r>20)&(g-b>30); lab,n=ndimage.label(m)
    bl=[]
    for k in range(1,n+1):
        ys,xs=np.nonzero(lab==k)
        if len(xs)>=4: bl.append((xs.mean(),ys.mean(),len(xs)))
    on=None
    if bl:
        ref=max(bl,key=lambda q:(q[2] if q[1]<350 else 0))   # 위쪽의 가장 큰 초록 점
        on=any(-150<=x-ref[0]<=-75 and 55<=y-ref[1]<=135 and s>=10 for x,y,s in bl)
    st.append(on)
print('t_s,ld2_on')
for i,o in enumerate(st): print(f'{i/10:.1f},{"" if o is None else int(o)}')
seg=[];cur=None;a=0
for i,o in enumerate(st+[None]):
    if o!=cur:
        if cur is not None: seg.append((a/10,i/10,cur))
        cur=o;a=i
print('# segments', file=sys.stderr)
for s,e,o in seg: print(f'# {s:.1f}-{e:.1f} {e-s:.1f}s {"ON" if o else "off"}', file=sys.stderr)
