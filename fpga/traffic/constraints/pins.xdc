# STM32_1 FPGA 실습 2 - 신호등 제어 (최상위: traffic)
# 핀 출처: Xilinx S7 Pin Map의 신호등 모듈(확장 커넥터) 표, 클록 B6, 버튼 K4, DIP Y1
# 비트 순서 가정: [3]=북(N), [2]=동(E), [1]=남(S), [0]=서(W). direction 0→1→2→3이 북→동→남→서 순서가 된다.
# 교재의 원본 예제와 방향 순서가 다르면 이 표만 바꾼다. LED 극성(1=켜짐)도 보드에서 확인한다.
set_property PACKAGE_PIN B6  [get_ports clk_50mhz]
set_property PACKAGE_PIN K4  [get_ports rst_p]       ;# SW_1
set_property PACKAGE_PIN Y1  [get_ports flicker]     ;# DIP_SW1, 올리면 점멸 모드
set_property PACKAGE_PIN C12 [get_ports {led_red[3]}]
set_property PACKAGE_PIN C17 [get_ports {led_red[2]}]
set_property PACKAGE_PIN B13 [get_ports {led_red[1]}]
set_property PACKAGE_PIN G14 [get_ports {led_red[0]}]
set_property PACKAGE_PIN D13 [get_ports {led_yellow[3]}]
set_property PACKAGE_PIN C18 [get_ports {led_yellow[2]}]
set_property PACKAGE_PIN L18 [get_ports {led_yellow[1]}]
set_property PACKAGE_PIN A14 [get_ports {led_yellow[0]}]
set_property PACKAGE_PIN E11 [get_ports {led_green[3]}]
set_property PACKAGE_PIN A20 [get_ports {led_green[2]}]
set_property PACKAGE_PIN E16 [get_ports {led_green[1]}]
set_property PACKAGE_PIN C16 [get_ports {led_green[0]}]
set_property PACKAGE_PIN F10 [get_ports {led_left[3]}]
set_property PACKAGE_PIN C19 [get_ports {led_left[2]}]
set_property PACKAGE_PIN F15 [get_ports {led_left[1]}]
set_property PACKAGE_PIN D15 [get_ports {led_left[0]}]
set_property PACKAGE_PIN C11 [get_ports {led_walk_red[3]}]
set_property PACKAGE_PIN E18 [get_ports {led_walk_red[2]}]
set_property PACKAGE_PIN A19 [get_ports {led_walk_red[1]}]
set_property PACKAGE_PIN G13 [get_ports {led_walk_red[0]}]
set_property PACKAGE_PIN G11 [get_ports {led_walk_green[3]}]
set_property PACKAGE_PIN A16 [get_ports {led_walk_green[2]}]
set_property PACKAGE_PIN E19 [get_ports {led_walk_green[1]}]
set_property PACKAGE_PIN F12 [get_ports {led_walk_green[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports *]
create_clock -name clk_50mhz -period 20.000 [get_ports clk_50mhz]
set_false_path -from [get_ports {rst_p flicker}]
