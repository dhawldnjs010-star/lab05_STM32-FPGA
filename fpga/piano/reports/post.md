# 실험 후 레포트: STM32_1 FPGA 실습 1 · 피아노

작성자 상혁(2025440084) / 실험일 2026-10-19 / Vivado 2026.1 / part xc7s75fgga484-1 / top `piano`(구현), `tb`(시뮬레이션) / XDC `constraints/pins.xdc` / 보드 클록 50 MHz

## Vivado 시뮬레이션
실습 당일 첫 XSim은 기본 실행 시간 1000 ns에서 멈춰 PASS 문구가 나오지 않았다(TB는 4,796 ns에 끝남). 이후 끝까지 실행한 파형(`evidence/post/xsim_wave.png`)에서 8음(key 80→01)의 반주기 19, 17, 15, 14, 12, 11, 10, 9클록과 무음 구간까지 진행된 것을 확인했다. Icarus 사전 검증은 `PASS piano: all 8 tones, silence, multiple keys, reset`.

## 합성·구현·비트스트림
`synth_design Complete!`, `write_bitstream Complete!`, WNS 14.776 ns, Failed Routes 0 (`evidence/post/vivado_runs.png`).

## 실제 보드 기록·실측
버튼 SW_1~SW_8을 차례로 눌렀다(`evidence/post/board_demo.mp4`, 소리 포함). 휴대폰 녹음에서 사각파의 3배 고조파를 찾아 3으로 나눴다(`piano_audio.py`).

| 음 | 설계 (Hz) | 영상 시각 (s) | 측정 (Hz) |
|---|---|---|---|
| 도 | 262 | 0.35 | 261.8 |
| 레 | 294 | 0.70 | 293.8 |
| 미 | 330 | 1.20 | 329.6 |
| 파 | 349 | 1.60 | 349.0 |
| 솔 | 392 | 2.00 | 392.0 |
| 라 | 440 | 2.45 | 439.9 |
| 시 | 494 | 2.85 | 494.0 |
| 높은 도 | 523 | 3.30 | 523.0 |

## 비교·결론
여덟 음 모두 설계 주파수와 0.4 Hz 안에서 같다.
