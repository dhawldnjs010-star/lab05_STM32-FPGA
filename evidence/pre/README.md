# lab05 실험 전 검증 자료 (STM32_1 · 인터럽트와 PWM, FPGA 피아노·신호등·ADC)

## STM32 (NUCLEO-G474RE)
- 소스: `Core/Src/ece2_474_routine.c` (`STM32_1_TASK` 3 또는 4로 과제 선택)
- `logs/build_debug_task3.txt`, `build_debug_task4.txt`: CMake Debug 빌드 출력, 오류·경고 0 (클라우드 작업 환경의 GNU Arm 13.2.1)
- `fw/`: HAL 함수만 흉내 낸 PC 모의 실행. `sh fw/run.sh`로 재현. 결과 `fw_log_task3.txt`, `fw_log_task4.txt`
- `fig/fw_timeline.png`: 모의 실행 결과 그림 (가상 시간, 보드 실측 아님)

## FPGA (Combo II-DLD, xc7s75fgga484-1)
- `../../fpga/<실습>/evidence/pre/`: Icarus Verilog 12.0 PASS 로그, VCD, 파형 그림, 오류 주입 로그
- 그림 스크립트: `fig/fpga_wave_figs.py`, `fig/fw_timeline_fig.py`
