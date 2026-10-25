"""신호등 시연 영상(2 fps 프레임)에서 초록·노랑 화소 수를 세어 단계 시간을 읽는다.
사용: ffmpeg -i board_demo.mp4 -vf fps=2 frames/%03d.png 후 python traffic_trace.py frames
(원본 1080p 기준 crop. 720p 사본에서는 좌표를 2/3로 바꾼다.)"""
import sys, glob, numpy as np
from PIL import Image
print('t_s,green_px,yellow_px')
for i,f in enumerate(sorted(glob.glob(sys.argv[1]+'/*.png'))):
    a=np.asarray(Image.open(f).crop((600,60,1350,700))).astype(int); r,g,b=a[...,0],a[...,1],a[...,2]
    gm=(g>170)&(g>r+20)&(b>120); ym=(r>200)&(g>150)&(b<120)&(g<r)
    print(f'{i/2:.1f},{gm.sum()},{ym.sum()}')
