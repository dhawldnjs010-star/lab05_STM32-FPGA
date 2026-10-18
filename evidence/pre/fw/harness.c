/* STM32_1 과제3·4 모의 실행: 실제 ece2_474_routine.c를 그대로 컴파일하고
 * 1 ms 가상 시간에서 TIM6 인터럽트(100 ms)와 버튼 EXTI 호출을 흉내 낸다. */
#include <stdio.h>
#include "main.h"
#include "ece2_474.h"
GPIO_TypeDef GPIOA_obj, GPIOC_obj; TIM_TypeDef TIM6_obj, TIM3_obj;
USART_TypeDef USART2_obj, USART3_obj;
TIM_HandleTypeDef htim6 = {&TIM6_obj, 0}, htim3 = {&TIM3_obj, 500};
UART_HandleTypeDef huart2 = {&USART2_obj}, huart3 = {&USART3_obj};
static uint32_t now_ms; static int led; static int tim6_on, pwm_on;
uint32_t HAL_GetTick(void) { return now_ms; }
void HAL_GPIO_TogglePin(GPIO_TypeDef *p, uint16_t pin) {
    if (p == GPIOA && pin == LED_ece2_Pin) { led = !led; printf("TOGGLE t=%u led=%d\n", now_ms, led); } }
int HAL_TIM_Base_Start_IT(TIM_HandleTypeDef *h) { if (h == &htim6) tim6_on = 1; return 0; }
int HAL_TIM_PWM_Start(TIM_HandleTypeDef *h, uint32_t ch) { (void)ch; if (h == &htim3) pwm_on = 1; return 0; }
int HAL_UART_Receive_IT(UART_HandleTypeDef *h, uint8_t *b, uint16_t n) { (void)h; (void)b; (void)n; return 0; }

/* 버튼 EXTI 호출 시각(ms): 3000/3030/3060은 한 번 누를 때 접점 떨림 세 번 */
static const uint32_t press[] = {3000, 3030, 3060, 10000, 22000, 30000, 50000};
int main(void) {
    unsigned k = 0, last_ccr = 0xFFFF;
    ece2_474_init();
    printf("INIT tim6=%d pwm=%d ccr=%u\n", tim6_on, pwm_on, htim3.ccr1);
    for (now_ms = 1; now_ms <= 60000; now_ms++) {
        while (k < sizeof press / sizeof press[0] && press[k] == now_ms) {
            HAL_GPIO_EXTI_Callback(BUTTON_ece2_Pin);
            printf("PRESS t=%u\n", now_ms); k++; }
        if (tim6_on && now_ms % 100 == 0) HAL_TIM_PeriodElapsedCallback(&htim6);
        polling_routine();
        if (pwm_on && htim3.ccr1 != last_ccr) { last_ccr = htim3.ccr1; printf("CCR t=%u ccr=%u duty=%u%%\n", now_ms, last_ccr, last_ccr / 10); }
    }
    return 0;
}
