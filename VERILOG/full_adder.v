module full_adder(sum, carry, a,b,c);

input a,b,c;
output sum,carry;
wire s0,c0;
half_adder HA1 (s0,c0,a,b);
assign sum = s0^c;
assign carry = (c&s0) | c0;

endmodule