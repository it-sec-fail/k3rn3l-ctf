Basic reverse engineering of an assembler file.

The important part lies in label5.

Each number from the Pin needed to complete the flag from the section .data is is compared a few times.
validPinMessage db "Great, your flag flag{K3RN3L_DR0ID_%s}", 0

The numbers are represented by their ASCII-Code -> 0x30 is 0
Each number from the pin has different jump-conditions. 
Read about assebler jump conditions here:
https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm

Example number 1 from the pin:
mov r9b, [pinCode + 0x0]
    cmp r9b, 0x30
    jne invalid_pin
    cmp r9b, 0x31
    je invalid_pin
    cmp r9b, 0x32
    je invalid_pin
    cmp r9b, 0x35
    je invalid_pin
    push 0xFFFFFFF

Important part: jne r9b, 0x30 -> Jump if not equal to "invalid_pin" -> so the number has to be 0.

Flag: flag{K3RN3L_DR0ID_04001196}