# lab05 FPGA 1 - 피아노 (piano)

`piano(clk_50mhz, rst_p, key[7:0], piezo)`: 버튼 하나를 누르는 동안 해당 음의 사각파를 피에조로 낸다.
key[7]=도 262 Hz … key[0]=높은 도 523 Hz, 무입력·여러 키는 무음. 반주기 = 50 MHz / (2 × 주파수) 클록.

| 경로 | 내용 |
|---|---|
| src/piano.v, note_select.v, square_tone.v | 수업 제공 설계 |
| sim/piano_tb.sv | 수업 제공 TB (CLK_HZ=10000으로 축소), 파형 저장 한 줄 추가 |
| constraints/pins.xdc | clk B6, rst SW_# K6, key SW_1~SW_8, piezo Y21 |
| evidence/pre/ | Icarus PASS 로그, 파형(wave.vcd, piano_wave.png), 오류 주입 |

보드: KEYPADS SEL 스위치를 내려 버튼 모드, PIEZO ENABLE 스위치 켜기.
사전 검증: `PASS piano: all 8 tones, silence, multiple keys, reset`. 미(330 Hz)를 329로 바꾸면 `FATAL ... note lookup`.
