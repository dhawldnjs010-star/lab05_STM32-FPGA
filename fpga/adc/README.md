# lab05 FPGA 3 - ADC (adc)

`adc(clk_50mhz, rst_p, add_sel[2:0], adc_sclk, adc_ncs, adc_din, adc_dout, sample[11:0], data_valid, led_out[7:0])`.
16비트 명령 {101, 채널, 11, 0, 111, 0000}을 보내며 같은 프레임에서 16비트를 받아 하위 12비트를 sample에, 상위 8비트(sample[11:4])를 LED에 낸다.
SCLK = 50 MHz / (2 × HALF_CYCLES) = 1 MHz (HALF_CYCLES=25).

| 경로 | 내용 |
|---|---|
| src/adc.v, adc_command.v, serial_frame16.v | 수업 제공 설계 |
| src/adc_board.v | 보드 구현용 최상위(추가). 핀이 없는 sample·data_valid를 내부에 둔다 |
| sim/adc_tb.sv | 수업 제공 TB (HALF_CYCLES=2), 파형 저장 한 줄 추가 |
| constraints/pins.xdc | SPI_AD H3(CS), SPI_DIN H5, SPI_DOUT J6, SPI_SCK H7, add_sel DIP_SW6~8, LED 8개 |
| evidence/pre/ | PASS 로그, 파형, 오류 주입 |

보드: 채널 0 = 가변저항(VR), 1 = 조도센서(CdS). DIP_SW6~8을 000/001로 두고 손잡이·빛을 바꿔 LED 값 변화를 본다.
채널을 바꾼 직후 첫 결과는 이전 채널 값일 수 있다(장치 설명서 확인).
사전 검증: `PASS ADC: 3 serial frames, command bits, sample, reset`. 명령 상위 3비트를 100으로 바꾸면 `FATAL ... ADC command`.

## 실험 후 (2026-10-19)

시연 영상과 실측은 `evidence/post/`, `reports/post.md`.
