# STM32_1 과제 코드 보관본

`stm32_lab\Core\Src\ece2_474_routine.c`에 통째로 붙여넣어 쓴다. 붙여넣은 뒤에는 디버깅을 끝내고(Shift+F5) Build → F5로 다시 올린다.

| 파일 | 과제 | 동작 |
|---|---|---|
| `task3_ece2_474_routine.c` | STM32_1_과제3 | 버튼 ISR에서 간격 1→2→4→8→1초, TIM6 ISR(100 ms)에서 횟수를 세어 PA5 반전 |
| `task4_ece2_474_routine.c` | STM32_1_과제4 | 버튼 ISR에서 PB4 PWM 비교값 250→500→750→250 (25→50→75→25%) |

- 두 과제의 파일은 서로 다른 코드이므로 한 번에 하나만 `ece2_474_routine.c`에 둔다.
- 과제4의 디버거 중단점은 버튼 ISR 안의 `__HAL_TIM_SET_COMPARE` 줄(74번 줄)에 건다. 변수는 `pwm_compare`.
- 현재 `stm32_lab\Core\Src\ece2_474_routine.c`는 과제4 코드다.
- 출처: ece2_474 매뉴얼 v1.1.0 (https://github.com/Glaysia/ece2_474)
