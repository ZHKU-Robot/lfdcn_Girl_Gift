
/********************************** (C) COPYRIGHT *******************************
* File Name          : Main.C
* Author             : WCH
* Version            : V1.1
* Date               : 2017/11/18
* Description        : GPIO 设置与使用和GPIO中断使用示例   
*******************************************************************************/
#include "CH552.H"                                                   
#include "Debug.H"
#include "GPIO.H"
#include "stdio.h"
#include <string.h>

#pragma  NOAREGS

sbit LED0 = P1^6;
sbit LED1 = P1^7;

void main( ) 
{
    UINT16 j = 0;
    CfgFsys( );                                                                //CH554时钟选择配置   
    mDelaymS(20);
    mInitSTDIO( );                                                             //串口0初始化
    printf("start ...\n"); 
    Port1Cfg(1,6);                                                             //P16设置推挽模式
    Port1Cfg(1,7);                                                             //P17设置推挽模式
    LED0 = 0;
    LED1 = 0;	

    while(1){
      printf(".");
      LED0 = ~LED0;
      LED1 = ~LED1;			
      mDelaymS(100);			
    }
}