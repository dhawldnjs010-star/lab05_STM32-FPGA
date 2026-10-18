/* PC 모의 실행용 main.h: polling 루틴이 쓰는 HAL 이름만 흉내 낸다. */
#ifndef MOCK_MAIN_H
#define MOCK_MAIN_H
#include <stdint.h>
typedef enum { GPIO_PIN_RESET = 0, GPIO_PIN_SET = 1 } GPIO_PinState;
typedef struct { int id; } GPIO_TypeDef;
typedef struct { int id; } TIM_TypeDef;
typedef struct { int id; } USART_TypeDef;
typedef struct { TIM_TypeDef *Instance; uint32_t ccr1; } TIM_HandleTypeDef;
typedef struct { USART_TypeDef *Instance; } UART_HandleTypeDef;
typedef struct { int dummy; } SPI_HandleTypeDef;
typedef struct { int dummy; } I2C_HandleTypeDef;
extern GPIO_TypeDef GPIOA_obj, GPIOC_obj;
extern TIM_TypeDef TIM6_obj, TIM3_obj;
extern USART_TypeDef USART2_obj, USART3_obj;
#define GPIOA (&GPIOA_obj)
#define GPIOC (&GPIOC_obj)
#define TIM6 (&TIM6_obj)
#define TIM3 (&TIM3_obj)
#define USART2 (&USART2_obj)
#define USART3 (&USART3_obj)
#define LED_ece2_Pin 0x0020U
#define LED_ece2_GPIO_Port GPIOA
#define BUTTON_ece2_Pin 0x2000U
#define BUTTON_ece2_GPIO_Port GPIOC
#define GPIO_IN_PULLUP_ece2_Pin 0x0001U
#define GPIO_IN_PULLDOWN_ece2_Pin 0x0002U
#define TIM_CHANNEL_1 0U
#define __HAL_TIM_SET_COMPARE(h, ch, v) ((h)->ccr1 = (v))
uint32_t HAL_GetTick(void);
void HAL_GPIO_TogglePin(GPIO_TypeDef *port, uint16_t pin);
int HAL_TIM_Base_Start_IT(TIM_HandleTypeDef *h);
int HAL_TIM_PWM_Start(TIM_HandleTypeDef *h, uint32_t ch);
int HAL_UART_Receive_IT(UART_HandleTypeDef *h, uint8_t *b, uint16_t n);
#endif
