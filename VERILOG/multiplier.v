module multiplier (a0,a1,a2,a3,b0,b1,b2,b3,c5, p6, p5, p4, p3, p2, p1, p0);

// INPUT
input a0,a1,a2,a3,b0,b1,b2,b3;

// OUTPUT
output c5,p6,p5,p4,p3,p2,p1,p0;

// CIRCUIT DESCRIPTION

wire o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15;
wire l1,l2,l3,l4,l5,l6,l7,p1,p0;
wire c5,p6,m1,m2,m3,m4,m5,p2;
wire m7,p5,m8,m9,m10,p4,m11,p3;

//AND GATES LEVEL
assign o1 = b3&a3;
assign o2 = b2&a3;
assign o3 = b3&a2;
assign o4 = b3&a1;
assign o5 = b1&a3;
assign o6 = a2&b2;
assign o7 = b1&a2;
assign o8 = b0&a3;
assign o9 = b3&a0;
assign o10 = b2&a1;
assign o11 = b1&a1;
assign o12 = b0&a2;
assign o13 = b2&a0;
assign o14 = b0&a1;
assign o15 = b1&a0;
assign p0 = b0&a0;

//LEVEL 1
full_adder FA1 (l2,l1,o2,o3,m1);
half_adder HA2 (l4,l3,o7,o8);
half_adder HA3(l6,l5,o11,o12);
half_adder HA4 (p1,l7,o14,o15);

//LEVEL 2
full_adder FA5 (p6,c5,o1,l1,m7);
full_adder FA6 (m2,m1,o5,o6,l3);
full_adder FA7 (m4,m3,l4,o10,l5);
full_adder FA8 (p2,m5,l6,o13,l7);

//LEVEL 3
full_adder FA9 (p5,m7,l2,m8,m10);
full_adder FA10 (m9,m8,o4,m2,m3);
half_adder HA11 (p4,m10,m9,m11);
full_adder FA12 (p3,m11,o9,m4,m5);

endmodule