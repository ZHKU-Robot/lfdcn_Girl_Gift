
/********************************** (C) COPYRIGHT *******************************
* File Name          : UART1.C
* Author             : lfdcn
* Version            : V1.0
* Date               : 2020/12/03
* Description        : CH552 串口1收发  
*******************************************************************************/

#include "UART.H"
#include <CH552.H>
#include "Debug.H"

#pragma  NOAREGS

/*******************************************************************************
* Function Name  : UART0_Init()
* Description    : CH552串口0初始化
* Input          : None
* Output         : None
* Return         : None
*******************************************************************************/
void UART0_Init( )
{
    UINT32 x;
    UINT8 x2; 

    SM0 = 0;
    SM1 = 1;
    SM2 = 0;                                                                   //串口0使用模式1
                                                                               //使用Timer1作为波特率发生器
    RCLK = 0;                                                                  //UART0接收时钟
    TCLK = 0;                                                                  //UART0发送时钟
    PCON |= SMOD;
    x = 10 * FREQ_SYS / UART0_BUAD / 16;                                       //如果更改主频，注意x的值不要溢出                            
    x2 = x % 10;
    x /= 10;
    if ( x2 >= 5 ) x ++;                                                       //四舍五入

    TMOD = TMOD & ~ bT1_GATE & ~ bT1_CT & ~ MASK_T1_MOD | bT1_M1;              //0X20，Timer1作为8位自动重载定时器
    T2MOD = T2MOD | bTMR_CLK | bT1_CLK;                                        //Timer1时钟选择
    TH1 = 0-x;                                                                 //12MHz晶振,buad/12为实际需设置波特率
    TR1 = 1;                                                                   //启动定时器1
    TI = 1;
    REN = 1;                                                                   //串口0接收使能
	
#if UART0_PINMAP	
    PIN_FUNC |= bUART0_PIN_X;                                                   //映射到P34(R)、P32(T)
#endif

#if UART0_INTERRUPT                                                            //开启中断使能
	ES = 1;	
	EA = 1;
#endif	
}
/*******************************************************************************
* Function Name  : CH552UART0_RcvByte()
* Description    : CH552UART0接收一个字节
* Input          : None
* Output         : None
* Return         : SBUF
*******************************************************************************/
UINT8  CH552UART0_RcvByte( )
{
    while(RI == 0);                                                           //查询接收，中断方式可不用
    RI = 0;
    return SBUF;
}

/*******************************************************************************
* Function Name  : CH552UART0_SendByte(UINT8 SendDat)
* Description    : CH552UART0发送一个字节
* Input          : UINT8 SendDat；要发送的数据
* Output         : None
* Return         : None
*******************************************************************************/
void CH552UART0_SendByte(UINT8 SendDat)
{
	SBUF = SendDat;                                                             //查询发送，中断方式可不用下面2条语句,但发送前需TI=0
	while(TI ==0);
	TI = 0;
}


#if UART0_INTERRUPT
/*******************************************************************************
* Function Name  : UART0Interrupt(void)
* Description    : UART0 中断服务程序
*******************************************************************************/
void UART0Interrupt( void ) interrupt INT_NO_UART0 using 1                       //串口1中断服务程序,使用寄存器组1
{
	UINT8 dat;
	if(RI)
	{
		dat = SBUF1;
		RI = 0;
		
//		CH554UART1SendByte(dat);
	}
}
#endif
