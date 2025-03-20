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


adc_result_t Result1;
adc_result_t Result2;
uint8_t LSB8_G;
uint8_t MSB4_G;
uint8_t LSB8_P;
uint8_t MSB4_P;

void main(void)
{
    // Initialize the device
    SYSTEM_Initialize();

    ADCC_Initialize();
    
    LATCbits.LATC1 = 0;
    TRISCbits.TRISC1 = 1;
    ANSELCbits.ANSELC1 = 1;
    WPUC1 = 0;
    
    ADCC_StartConversion(0b010001);
    
    while(1){
        ADCC_StartConversion(0b010001);
        __delay_ms(10);
        if(ADCC_IsConversionDone()){
            Result1 = ADCC_GetConversionResult();
            LSB8_P = Result1 & 0xFF;
            MSB4_P = (Result1 >> 8) & 0x0F;
            ADCON0bits.ADGO = 1;
        }
        __delay_ms(10);
        ADCC_StartConversion(0b010010);
        __delay_ms(10);
        if(ADCC_IsConversionDone()){
            Result2 = ADCC_GetConversionResult();
            LSB8_G = Result2 & 0xFF;
            MSB4_G = (Result2 >> 8) & 0x0F;
            ADCON0bits.ADGO = 1;
        }
        UART2_Write(MSB4_P);
        UART2_Write(LSB8_P);
        UART2_Write(MSB4_G);
        UART2_Write(LSB8_G);
        __delay_ms(10);
    }
    
    
    // If using interrupts in PIC18 High/Low Priority Mode you need to enable the Global High and Low Interrupts
    // If using interrupts in PIC Mid-Range Compatibility Mode you need to enable the Global Interrupts
    // Use the following macros to:

    // Enable the Global Interrupts
    //INTERRUPT_GlobalInterruptEnable();

    // Disable the Global Interrupts
    //INTERRUPT_GlobalInterruptDisable();
//        UART2_sendString("H");

}
/**
 End of File
*/