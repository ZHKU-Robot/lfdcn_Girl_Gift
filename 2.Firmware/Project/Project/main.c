
/********************************** (C) COPYRIGHT *******************************
* File Name          : main.C
* Author             : lfdcn
* Version            : V1.0
* Date               : 2020.11.27
* Description        : 主程序
*******************************************************************************/
#include "Debug.H"
#include <CH552.H>
#include "UART.H"
#include "I2C.H"
#include "GPIO.H"
#include <stdio.h>
#include <string.h>
#include "RZ.H"

#pragma  NOAREGS

void LM75A_GetTemp( );

bit LM75_N;//温度值的符号（0正1负）
UINT8 LM75_T,LM75_P;//温度值的整数,小数值（十进制，小数值2位，精度0.125中的前两位）
UINT8 rz[24];
UINT8 RGB[3]={0xFF,0xFF,0xFF};

sbit LM75_ADDR = P1^1;

struct My_24bits RGB_VAL;

void main( )
{
	CfgFsys( );                                                                //CH552时钟选择配置
	mDelaymS(20);
	UART0_Init( );                                                             //串口0初始化
	printf("start\n");

	Port1Cfg(1,1);
	Port1Cfg(1,4);
	Port1Cfg(1,7);
	Port1Cfg(1,5);
	Port1Cfg(1,6);
	Port3Cfg(1,3);
	Port3Cfg(1,4);
	
	LM75_ADDR = 1;
	printf("%d %d %d\n",RGB[0],RGB[1],RGB[2]);
	
	RGB_VAL.G_VAL = 0x00;
	RGB_VAL.B_VAL = 0XFF;
	RGB_VAL.R_VAL = 0x00;
	
	Send_24bits(RGB_VAL);
	ResetDataFlow( );
	
	while(1) {
//		LM75A_GetTemp( );
//		mDelaymS(1000);
		Send_24bits(RGB_VAL);
//		RZ_SendByte(RGB);
//		printf("%d %d %d\n",RGB[0],RGB[1],RGB[2]);
//		printf("%d %d %d\n",RGB_VAL.G_VAL,RGB_VAL.B_VAL,RGB_VAL.R_VAL);
	}
}
