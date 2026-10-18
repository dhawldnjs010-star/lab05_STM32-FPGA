# lab05 FPGA 2 - 신호등 제어 (traffic)

`traffic(clk_50mhz, rst_p, flicker, led_red/yellow/green/left[3:0], led_walk_red/green[3:0])`.
1초 tick마다 phase 0~12, 한 방향 13초(0~10 초록, 11~12 노랑), 4방향 순환. 보행 신호는 0~3초 초록, 4~10초 점멸.
flicker=1이면 차량 노랑·보행 빨강이 함께 점멸하는 점멸 모드.

| 경로 | 내용 |
|---|---|
| src/traffic.v, second_tick.v, traffic_sequence.v, traffic_lights.v | 수업 제공 설계 |
| sim/traffic_tb.sv | 수업 제공 TB (CLK_HZ=4로 축소: 1초 = 4클록), 파형 저장 한 줄 추가 |
| constraints/pins.xdc | 신호등 모듈(확장 커넥터) 24핀, rst SW_1 K4, flicker DIP_SW1 Y1 |
| evidence/pre/ | PASS 로그, 파형, 오류 주입 |

가정: 비트 [3]=북, [2]=동, [1]=남, [0]=서. LED 극성은 1=켜짐. 보드에서 확인하고 다르면 XDC만 바꾼다.
사전 검증: `PASS traffic: full cycle, pedestrian blink, flicker, reset`. 초록 구간을 0~9로 줄이면 `FATAL ... dir=0 phase=10`.
