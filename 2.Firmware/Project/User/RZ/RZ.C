#include "RZ.H"
#include <CH552.H>
#include <stdio.h>
#include "Debug.H"
#include <intrins.h>

#pragma  NOAREGS

sbit DIN2_RGB = P1^5;

/*
子程序名称:RZ_SendByte(UINT8 *ptr)
功能：发送一个像素点的24bit数据
参数：接收的参数是一个指针，此函数会将此指针指向的地址的连续的三个Byte的数据发送
说明：在主函数中直接调用此函数时，在整个帧发送开始前需要先执行 ResetDataFlow()
数据是按归零码的方式发送，速率为800KBPS
*/
void RZ_SendByte(UINT8 *ptr)
{
	UINT8 i,j;
	UINT8 temp;
	
	for(j=0;j<3;j++)
	{
		temp=ptr[j];
		for(i=0;i<8;i++)
		{
			if(temp&0x80)		 //从高位开始发送
			{
				DIN2_RGB = 1;
//				delay_H();
				DIN2_RGB = 0;
//				delay_L();
			}
			else				//发送“0”码
			{
				DIN2_RGB = 1;
//				delay_H();
				DIN2_RGB = 0;
//				delay_L();
			}
			temp=(temp<<1);		 //左移位
		}
	}
}

void ResetDataFlow(void)
{
	DIN2_RGB = 0;
	mDelayuS(200);
}

void delay_L(void)
{
	_nop_();
}

void delay_H(void)
{
    _nop_();
}

/*发送24位字符（包含RGB信息各8位）*/
void Send_24bits(struct My_24bits RGB_VAL)
{
    UINT8 i;
    for(i=0; i<8; i++)
    {
        Send_A_bit(RGB_VAL.G_VAL>>(7-i)&0x01);//注意是从高位先发
    }
    for(i=8; i<16; i++)
    {
        Send_A_bit(RGB_VAL.R_VAL>>(15-i)&0x01);
    }
    for(i=16; i<24; i++)
    {
        Send_A_bit(RGB_VAL.B_VAL>>(23-i)&0x01);
    }
}

void Send_A_bit(UINT8 VAL)
{
    if (VAL==1)
    {
        DIN2_RGB=1;
        _nop_();//两个nop，大概是0.5us,经测试，发送完1后的延时最重要
        _nop_();
		_nop_();
        DIN2_RGB=0;
    }
    else
    {
        DIN2_RGB=1;
        _nop_(); //一个nop,大概是0.25us
        DIN2_RGB=0;
    }
}