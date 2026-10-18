`timescale 1ns/1ps
// 보드 구현용 최상위(학생 추가). 수업 제공 adc 모듈을 수정 없이 쓰고,
// 보드에 연결할 장치가 없는 sample[11:0]·data_valid는 내부 신호로 둔다.
// 연결되지 않은 최상위 포트가 있으면 Vivado 비트스트림 단계에서 핀 미지정 오류가 나기 때문이다.
module adc_board(
    input wire clk_50mhz, rst_p,
    input wire [2:0] add_sel,
    output wire adc_sclk, adc_ncs, adc_din,
    input wire adc_dout,
    output wire [7:0] led_out
);
    wire [11:0] sample;
    wire data_valid;
    adc u_adc(clk_50mhz, rst_p, add_sel, adc_sclk, adc_ncs, adc_din, adc_dout,
              sample, data_valid, led_out);
endmodule
