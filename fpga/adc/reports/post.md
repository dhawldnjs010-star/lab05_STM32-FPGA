# 실험 후 레포트: STM32_1 FPGA 실습 3 · ADC

작성자 상혁(2025440084) / 실험일 2026-10-19 / Vivado 2026.1 / top `adc_board`(구현), `tb`(시뮬레이션) / 보드 클록 50 MHz

## 시뮬레이션
- XSim: `PASS ADC: 3 serial frames, command bits, sample, reset` (2,016 ns, `xsim_wave.png`)

## 합성·구현·비트스트림
`write_bitstream Complete!`, WNS 15.290 ns, Failed Routes 0 (`vivado_runs.png`).

## 실제 보드 기록
`board_demo.mp4`: DIP_SW6~8 = 000(CH0 가변저항)에서 손잡이를 돌리자 LED1~8이 모두 꺼짐(0)부터 모두 켜짐(255)까지 바뀌었다(`adc_frames.jpg`, 1·10 s 0, 4 s 255).
