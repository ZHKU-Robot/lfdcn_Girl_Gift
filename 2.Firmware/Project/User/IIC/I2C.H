#ifndef _I2C_H_
#define _I2C_H_

#include <CH552.H>
#include <intrins.h>

#define _Nop() _nop_() /*定义空指令*/

//“程序开发调试设置项”
#define LM75A_ADD 		0x9E  // LM75A的I2C地址（1001 A2 A1 A0 W/R）（模块专用地址，禁止修改）

extern bit LM75_N;//温度值的符号（0正1负）
extern UINT8 LM75_T,LM75_P;//温度值的整数,小数值（十进制，小数值2位，精度0.125中的前两位）

void Start_I2c();
void Stop_I2c();
void SendByte(UINT8 c);
UINT8 RcvByte();
void Ack_I2c(bit a);
bit ISendByte(UINT8 sla,UINT8 c);
bit ISendStr(UINT8 sla,UINT8 suba,UINT8 *s,UINT8 no);
bit IRcvByte(UINT8 sla,UINT8 *c);
void LM75A_GetTemp( );
UINT8 IRcvStr(UINT8 sla,UINT8 suba,UINT8 *s,UINT8 no);
extern void LM75A_GetTemp( );

#endif