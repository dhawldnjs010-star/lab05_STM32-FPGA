# STM32_1 FPGA 실습 1 - 피아노 (최상위: piano)
# 핀 출처: HBE Combo II-DLD 설명서·Xilinx S7 Pin Map(예전교안모음), 조교 저장소 lab3_piezo.xdc (B6, Y21)
# 버튼은 누르면 HIGH(보드에 채터링 방지 회로 내장). KEYPADS SEL 스위치를 아래로 내려 버튼 모드로 쓴다.
# 보드의 PIEZO ENABLE 스위치를 켜야 소리가 난다.
set_property PACKAGE_PIN B6  [get_ports clk_50mhz]
set_property PACKAGE_PIN K6  [get_ports rst_p]       ;# SW_#
# key[7] = 도(262 Hz) ... key[0] = 높은 도(523 Hz)
set_property PACKAGE_PIN K4  [get_ports {key[7]}]    ;# SW_1 도
set_property PACKAGE_PIN N8  [get_ports {key[6]}]    ;# SW_2 레
set_property PACKAGE_PIN N4  [get_ports {key[5]}]    ;# SW_3 미
set_property PACKAGE_PIN N1  [get_ports {key[4]}]    ;# SW_4 파
set_property PACKAGE_PIN P6  [get_ports {key[3]}]    ;# SW_5 솔
set_property PACKAGE_PIN N6  [get_ports {key[2]}]    ;# SW_6 라
set_property PACKAGE_PIN L5  [get_ports {key[1]}]    ;# SW_7 시
set_property PACKAGE_PIN J2  [get_ports {key[0]}]    ;# SW_8 높은 도
set_property PACKAGE_PIN Y21 [get_ports piezo]
set_property IOSTANDARD LVCMOS33 [get_ports {clk_50mhz rst_p key[*] piezo}]
create_clock -name clk_50mhz -period 20.000 [get_ports clk_50mhz]
set_false_path -from [get_ports rst_p]
