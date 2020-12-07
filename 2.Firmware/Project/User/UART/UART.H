#ifndef _UART_H_
#define _UART_H_

#include <CH552.H>

#define UART0_INTERRUPT   0          //定义是否使用接收中断接收数据
#define UART0_PINMAP      0          //定义串口0是否开启引脚映射。不开启选择P16(R)、P17(T)。开启选择P34(R)、P32(T)

#ifndef  DE_PRINTF                      //程序Pirntf输出开启
#define  DE_PRINTF     1
#endif

#ifndef  UART0_BUAD
#define  UART0_BUAD    9600
#endif

void   UART0_Init( );
UINT8  CH552UART0_RcvByte( );
void   CH552UART0_SendByte(UINT8 SendDat);

#endif