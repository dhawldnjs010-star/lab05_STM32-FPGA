# lab05 FPGA 실습용 Vivado 프로젝트 생성 스크립트
# 사용 (Vivado Tcl Console):
#   set ex piano        ;# piano | traffic | adc
#   source C:/Users/djawl/lab05_STM32-FPGA/fpga/vivado_setup.tcl
# 하는 일: 프로젝트 생성 -> RTL·XDC·TB 등록 -> top 지정 -> XSim 실행(PASS 확인)
# 비트스트림까지 만들려면 이어서:  make_bit
set root C:/Users/djawl/lab05_STM32-FPGA/fpga
if {![info exists ex] || [lsearch {piano traffic adc} $ex] < 0} { error "먼저 set ex piano|traffic|adc" }
array set impl_top {piano piano traffic traffic adc adc_board}
array set sim_top {piano tb traffic tb adc tb}
set dir $root/$ex
create_project $ex $dir/vivado -part xc7s75fgga484-1 -force
add_files -norecurse [glob $dir/src/*.v]
add_files -fileset constrs_1 -norecurse $dir/constraints/pins.xdc
set_property SOURCE_SET sources_1 [get_filesets sim_1]
add_files -fileset sim_1 -norecurse [glob $dir/sim/*.sv]
set_property top $impl_top($ex) [get_filesets sources_1]
set_property top $sim_top($ex) [get_filesets sim_1]
set_property top_lib xil_defaultlib [get_filesets sim_1]
set_property -name {xsim.simulate.runtime} -value {10us} -objects [get_filesets sim_1]
update_compile_order -fileset sources_1
update_compile_order -fileset sim_1
launch_simulation
puts "== $ex: Tcl Console에서 PASS 문장을 확인하세요. 구현 top = $impl_top($ex), 시뮬레이션 top = $sim_top($ex)"

proc make_bit {} {
    reset_run synth_1
    launch_runs impl_1 -to_step write_bitstream -jobs 4
    wait_on_run impl_1
    puts "== impl_1: [get_property STATUS [get_runs impl_1]]"
}
