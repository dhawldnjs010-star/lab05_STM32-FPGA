# FPGA 개별 실습 (STM32_1 주차, 10/19)

조교 매뉴얼 `Glaysia/ece2_474` v1.1.0 `docs/FPGA_additional.md` 3·4·7장의 설계 모듈과 테스트벤치를
fpga-lab-template(Glaysia/fpga-lab-template, 커밋 0b3318e466e9d77f7d3880df09c827788f361913) 구조로 옮겼다.

| 폴더 | 설계 최상위 | 시뮬레이션 top | 확인할 내용 |
|---|---|---|---|
| piano | `piano` | `tb` | 버튼에 따라 다른 음계 (8음, 무입력·여러 키 무음, 리셋) |
| traffic | `traffic` | `tb` | 4방향 13단계, 보행자 점멸, 점멸 모드, 리셋 |
| adc | `adc` (보드 구현은 `adc_board`) | `tb` | 16비트 직렬 프레임, 명령 비트·채널, 12비트 값, LED 표시 |

각 폴더: `src/` 설계(수업 제공 그대로, adc_board.v만 추가), `sim/` 수업 제공 TB(파형 저장 한 줄 추가),
`constraints/pins.xdc` 핀 제약, `simulation.json`, `tools/fpga_lab.py`, `evidence/pre/` 사전 검증 기록.

실행: 각 폴더에서 `python tools/fpga_lab.py simulate` 또는 VS Code에서 `FPGA.code-workspace` → Run Task.

핀 출처: 예전교안모음의 `Xilinx S7 Pin Map.pdf`, `HBE Combo II-DLD.pdf`, 조교 저장소 `lab3_piezo.xdc`.
보드에서 확인할 가정: 신호등 비트 순서([3]=북, [2]=동, [1]=남, [0]=서)와 LED 극성, ADC의 `SPI_AD`가 칩 선택인지.
