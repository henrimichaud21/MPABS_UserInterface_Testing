/**
  Generated Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This is the main file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  Description:
    This header file provides implementations for driver APIs for all modules selected in the GUI.
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.81.8
        Device            :  PIC18F16Q40
        Driver Version    :  2.00
*/

/*
    (c) 2018 Microchip Technology Inc. and its subsidiaries. 
    
    Subject to your compliance with these terms, you may use Microchip software and any 
    derivatives exclusively with Microchip products. It is your responsibility to comply with third party 
    license terms applicable to your use of third party software (including open source software) that 
    may accompany Microchip software.
    
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY 
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS 
    FOR A PARTICULAR PURPOSE.
    
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP 
    HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO 
    THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL 
    CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT 
    OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS 
    SOFTWARE.
*/

#include "mcc_generated_files/mcc.h"
#include <stdint.h>
#include <string.h>

/*
                         Main application
 * 
 */
uint8_t receiveData;

void sendBits(uint24_t sendData)
{
        SPI1_Open(SPI1_DEFAULT);
        Slave1_SetLow();
        
        uint8_t MSB = (sendData >> 16) & 0xFF;
        uint8_t MB = (sendData >> 8) & 0xFF;
        uint8_t LSB = sendData & 0xFF;
        
        receiveData = SPI1_ExchangeByte(MSB);
        receiveData = SPI1_ExchangeByte(MB);
        receiveData = SPI1_ExchangeByte(LSB);

        Slave1_SetHigh();
        SPI1_Close();
}

void setLMXSynthesizer(void)
{
    TRISCbits.TRISC4 = 0; // Set RC4 = CE to an output
    LATCbits.LATC4 = 1; // Set CE to 1 = HIGH to turn on LMX2571
    
    sendBits(0x002000);
    
    sendBits(0x290508);
    
    sendBits(0x28081C);
    
    sendBits(0x2711FB);
    
    sendBits(0x231043);
    
    sendBits(0x221040);
    
    sendBits(0x170684);
    
    sendBits(0x1681A4);
    
    sendBits(0x143015);
    
    sendBits(0x12C4EC);
    
    sendBits(0x1100FE);
    
    sendBits(0x070684);
    
    sendBits(0x0681A4);
    
    sendBits(0x043016);
    
    sendBits(0x0289D9);
    
    sendBits(0x01001D);
    
    sendBits(0x000983);
}


void UART2_sendString(const char *str)
{
    while(*str){
        while(!(UART2_is_tx_ready()));
        UART2_Write(*str++);
    }
}

void UART2_sendByte(uint8_t data) {
    while (!UART2_is_tx_ready());
    UART2_Write(data);
}
void main(void)
{
    // Initialize the device
    SYSTEM_Initialize();

    setLMXSynthesizer();
    
    uint8_t data = 0b00000000;
    
    while(1){
        UART2_sendByte(data); // Send current data
        data++;               // Increment data
        __delay_ms(1000);     // Wait for 1 second
        
        if(data == 0b00001111){
            data = 0b00000000;
        }
    }
}
/**
 End of File
*/