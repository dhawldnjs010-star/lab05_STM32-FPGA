"""피아노 시연 영상의 녹음에서 음별 주파수를 읽는다. 휴대폰 마이크는 저음 응답과 잡음(약 220 Hz)이
커서 사각파의 3배 고조파(3f)를 찾아 3으로 나눴다. 0.35 s 창, 0.05 s 간격, 16배 영채움 FFT. 음은 도→높은도 순서로 눌렀으므로 앞 음보다 뒤에서 찾는다."""
import sys, wave, numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
w=wave.open(sys.argv[1]); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float)
names='도 레 미 파 솔 라 시 높은도'.split(); notes=[262,294,330,349,392,440,494,523]
win=int(0.35*sr); N=16*win; hop=int(0.05*sr)
ts=np.arange(0,len(x)-win,hop)/sr
f=np.fft.rfftfreq(N,1/sr); S=[]
for t in ts:
    i=int(t*sr); S.append(np.abs(np.fft.rfft(x[i:i+win]*np.hanning(win),N))**2)
S=np.array(S)
print('note,expected_Hz,time_s,measured_Hz(3f/3),peak_ratio')
rows=[]; prev=0.0
for n,fn in zip(names,notes):
    m=abs(f-3*fn)<=4; nb=(abs(f-3*fn)>10)&(abs(f-3*fn)<60)
    r=S[:,m].max(1)/S[:,nb].mean(1); r[(ts>3.8)|(ts<=prev)]=0  # 음계를 차례로 누른 0~3.8 s 구간에서, 앞 음 뒤로 찾는다
    j=int(np.argmax(r)); k=np.argmax(np.where(m,S[j],0))
    prev=ts[j]; rows.append((n,fn,ts[j],f[k]/3,r[j])); print(f'{n},{fn},{ts[j]:.2f},{f[k]/3:.1f},{r[j]:.1f}')
if len(sys.argv)>2:
    fp='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; fm.fontManager.addfont(fp)
    plt.rcParams.update({'font.family':fm.FontProperties(fname=fp).get_name(),'font.size':6.5})
    band=(f>700)&(f<1650)
    fig,ax=plt.subplots(figsize=(8.4/2.54,2.3),dpi=300)
    Z=10*np.log10(S[:,band].T+1); Z=Z-np.percentile(Z,50)
    ax.imshow(np.clip(Z,0,None),aspect='auto',origin='lower',extent=[ts[0],ts[-1]+0.05,f[band][0],f[band][-1]],cmap='Blues')
    for n,fn,t,fm_,r in rows:
        ax.plot([t],[3*fm_],marker='o',ms=3,mfc='none',mec='#c2410c',mew=0.8)
        ax.text(t+0.05,3*fm_+15,n,fontsize=5.8,color='#1f2933')
    ax.set_xlim(0,4); ax.set_xlabel('영상 시각 (s)',color='#5f6b7a'); ax.set_ylabel('주파수 (Hz, 3배 고조파)',color='#5f6b7a')
    for s in ('top','right'): ax.spines[s].set_visible(False)
    ax.tick_params(length=2,colors='#5f6b7a')
    fig.tight_layout(pad=0.3); fig.savefig(sys.argv[2])
