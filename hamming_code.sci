clc;
clear;
close;
i1 = input("Enter information bit-1: ");
i2 = input("Enter information bit-2: ");
i3 = input("Enter information bit-3: ");
i4 = input("Enter information bit-4: ");

dataword = [i1,i2,i3,i4];
disp("the entercodeword is : ");

disp(dataword);
p1 = modulo(i1+i2+i3,2);
p2 = modulo(i2+i3+i4,2);
p3 = modulo(i2+i1+i4,2);

codeword = [i1,i2,i3,i4,p1,p2,p3];

disp("thye generated (7,4) hamming code is :");
disp(codeword);
error_pattern = [0,0,0,0,1,0,0];
codeword(5)=bitxor(error_pattern(5),codeword(5) )
disp("the recieved codeword through channel is: ");
disp(codeword);

n1=modulo(codeword(1)+ codeword(2)+ codeword(3)+ codeword(5) ,2);
n2=modulo(codeword(2)+ codeword(3)+ codeword(4)+ codeword(6) ,2);
n3=modulo(codeword(1)+ codeword(2)+ codeword(3)+ codeword(7) ,2);

syndrome = [n1,n2,n3];

disp("the recieved syndrome through channel  is :");
disp(syndrome);

correctedCodeword = modulo(codeword + error_pattern,2);
disp("the corrected code is :");
disp(correctedCodeword);
