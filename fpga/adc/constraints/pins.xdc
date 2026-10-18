# STM32_1 FPGA 실습 3 - ADC (구현 최상위: adc_board, 내부에 수업 제공 adc 사용)
# 핀 출처: Xilinx S7 Pin Map의 AD Convertor 표 (SPI_AD, SPI_DIN, SPI_DOUT, SPI_SCK), DIP·LED는 lab4와 같음
# 8채널 SPI ADC: CH0 = 가변저항(VR), CH1 = 조도센서(CdS) (HBE Combo II-DLD 설명서)
# SPI_DIN은 ADC로 들어가는 명령(FPGA 출력), SPI_DOUT은 ADC가 내보내는 변환값(FPGA 입력)으로 본다.
# SPI_AD는 ADC 칩 선택(CS)으로 보고 adc_ncs에 연결했다. 보드 설명서로 확인한다.
set_property PACKAGE_PIN B6  [get_ports clk_50mhz]
set_property PACKAGE_PIN K4  [get_ports rst_p]       ;# SW_1
set_property PACKAGE_PIN W1  [get_ports {add_sel[2]}] ;# DIP_SW6
set_property PACKAGE_PIN V4  [get_ports {add_sel[1]}] ;# DIP_SW7
set_property PACKAGE_PIN U4  [get_ports {add_sel[0]}] ;# DIP_SW8
set_property PACKAGE_PIN H3  [get_ports adc_ncs]     ;# SPI_AD
set_property PACKAGE_PIN H5  [get_ports adc_din]     ;# SPI_DIN
set_property PACKAGE_PIN J6  [get_ports adc_dout]    ;# SPI_DOUT
set_property PACKAGE_PIN H7  [get_ports adc_sclk]    ;# SPI_SCK
set_property PACKAGE_PIN L4  [get_ports {led_out[7]}]
set_property PACKAGE_PIN M4  [get_ports {led_out[6]}]
set_property PACKAGE_PIN M2  [get_ports {led_out[5]}]
set_property PACKAGE_PIN N7  [get_ports {led_out[4]}]
set_property PACKAGE_PIN M7  [get_ports {led_out[3]}]
set_property PACKAGE_PIN M3  [get_ports {led_out[2]}]
set_property PACKAGE_PIN M1  [get_ports {led_out[1]}]
set_property PACKAGE_PIN N5  [get_ports {led_out[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports *]
create_clock -name clk_50mhz -period 20.000 [get_ports clk_50mhz]
set_false_path -from [get_ports {rst_p add_sel[*]}]
