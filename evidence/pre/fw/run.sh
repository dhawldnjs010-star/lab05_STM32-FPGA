#!/bin/sh
# 모의 실행 재현: STM32_1_TASK를 3, 4로 바꿔 PC용 gcc로 컴파일하고 실행한다.
set -e
cd "$(dirname "$0")"
for t in 3 4; do
  sed "s/^#define STM32_1_TASK      3/#define STM32_1_TASK      $t/" ../../../Core/Src/ece2_474_routine.c > routine_t$t.c
  gcc -std=c11 -Wall -Wextra -Imock -o harness_t$t harness.c routine_t$t.c
  ./harness_t$t > fw_log_task$t.txt
  rm -f routine_t$t.c harness_t$t
done
