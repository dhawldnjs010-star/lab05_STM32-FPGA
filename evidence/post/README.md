# lab05 실험 후 자료 (2026-10-19 실습)

영상은 원본(1080p HEVC)을 720p H.264로 줄인 사본이다. 피아노 영상만 소리를 남겼다.

## STM32 (NUCLEO-G474RE) · `stm32/`
MCU 시연은 조원 PC에서 조원이 작성한 과제별 파일 `stm32_1_tasks/task3_ece2_474_routine.c`, `task4_ece2_474_routine.c`로 했다(파일을 `ece2_474_routine.c`에 통째로 붙여넣어 사용). `Core/Src/ece2_474_routine.c`는 실험 전 보고서 때 작성한 같은 동작의 코드(`STM32_1_TASK` 3·4)다.

| 파일 | 내용 |
|---|---|
| `task3_isr_PA5_demo.mp4` | 과제3: 버튼·TIM6 인터럽트로 LD2(PA5) 간격 1→2→4→8→1 s |
| `led_trace_task3.py`, `led_trace_task3.csv`, `led_segments_task3.txt` | 영상에서 LD2 켜짐/꺼짐 판독 (10 fps) |
| `task3_timeline.png` | 판독 결과 그림 (0.3 s 미만 판독 끊김은 메움) |
| `task4_pwm_PB4_scope.mp4`, `task4_scope.jpg` | 과제4: PB4 PWM 25→50→75→25% 오실로스코프 화면 |
| `debugger/01~04_*.png` | 과제4 C 디버거: 74번 줄 중단점, 조사식 `pwm_compare` 500 → 750 → 250 |
| `build_debug_demo_task3.txt`, `build_debug_demo_task4.txt` | 시연 코드(stm32_1_tasks)의 CMake Debug 빌드, 오류·경고 0 (클라우드 GNU Arm 13.2.1) |

## FPGA (Combo II-DLD, Vivado 2026.1) · `fpga/`
- `fpga/vivado_tcl_console.txt`: 세 프로젝트의 Vivado Tcl 콘솔 전체
- `../../fpga/<실습>/evidence/post/`: XSim 파형, 실행 상태, 시연 영상·프레임, 분석 스크립트
