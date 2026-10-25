# 실험 후 레포트: STM32_1 FPGA 실습 2 · 신호등 제어

작성자 상혁(2025440084) / 실험일 2026-10-19 / Vivado 2026.1 / top `traffic`(구현), `tb`(시뮬레이션) / 보드 클록 50 MHz

## Vivado 시뮬레이션
`PASS traffic: full cycle, pedestrian blink, flicker, reset`, `$finish` 2,186 ns (콘솔 로그). 파형 `evidence/post/xsim_wave.png`.

## 합성·구현·비트스트림
`write_bitstream Complete!`, WNS 15.109 ns, LUT 32, FF 32 (`evidence/post/vivado_runs.png`).

## 실제 보드 기록·실측
영상(`evidence/post/board_demo.mp4`)을 2 fps로 나눠 초록·노랑 화소를 셌다(`traffic_trace.py`, `traffic_trace.csv`, 분해능 0.5 s).

| 구간 | 관측 | 설계 |
|---|---|---|
| 0~3 s | 노랑(차량)·빨강(보행)이 0.5 s마다 함께 켜졌다 꺼짐 | flicker 모드 |
| 3.5 s~ | 한 방향 초록 시작 | flicker 해제 후 방향 0, 단계 0 |
| 초록 시작 간격 | 3.5 → 16.0 → 29.0 → 42.0 s (13 s) | 한 방향 13 s |
| 초록 지속 | 약 10.5~11 s, 이어서 노랑 2 s | 0~10 s 초록, 11~12 s 노랑 |
| 보행 초록 점멸 시작 | 각 방향 초록 시작 약 4 s 뒤 | 4 s부터 점멸 |

## 비교·결론
flicker, 단계 시간, 보행 점멸, 네 방향 순환이 설계대로 동작했다. 네 방향은 모듈에서 차례로 이웃한 방향으로 넘어갔다.
