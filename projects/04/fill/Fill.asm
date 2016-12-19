// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
    @24576
    D=M
    @SKIP
    D;JEQ
    @16384
    D=A
    @screenloc
    M=D
(SCREENON)
    @screenloc
    D=M
    A=M
    M=-1
    @screenloc
    M=M+1
    @24575
    D=D-A
    @END
    D;JEQ
    @SCREENON
    0;JMP
(END)
    @LOOP
    0;JMP
(SKIP)
    @16384
    D=A
    @screenloc
    M=D
(SCREENOFF)
    @screenloc
    D=M
    A=M
    M=0
    @screenloc
    M=M+1
    @24575
    D=D-A
    @VEND
    D;JEQ
    @SCREENOFF
    0;JMP
(VEND)
    @16384
    D=A
    @screenloc
    M=D
    @LOOP
    0;JMP