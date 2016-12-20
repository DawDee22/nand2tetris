// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
	@i 		//i is some memory location
	M=1 	//i = 1
	@R2 	//total is some mem. location
	M=0		//total = 0

(LOOP)
	@i
	D=M 	//D = i
	@R0
	D=D-M	//D = i - R0
	@END
	D;JGT	//go to end if (i-R0)>0
	@R1
	D=M
	@R2
	M=M+D 	//total = total + R1
	@i
	M=M+1
	@LOOP
	0;JMP	//goto LOOP

(END)
	@END
	0;JMP	//INfinite Loop