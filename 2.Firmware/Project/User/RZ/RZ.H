#ifndef _RZ_H_
#define _RZ_H_
#include <CH552.H>
#include "Debug.H"

//extern struct My_24bits
//{
//    UINT8 G_VAL;
//    UINT8 R_VAL;
//    UINT8 B_VAL;
//};

void RZ_SendByte(UINT8 *ptr);
void delay_L(void);
void delay_H(void);
void ResetDataFlow(void);
void Send_A_bit(UINT8 VAL);
void Send_24bits(struct My_24bits RGB_VAL);

#endif