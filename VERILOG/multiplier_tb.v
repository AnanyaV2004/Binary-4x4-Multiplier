`timescale 1ns/10ps

module multiplier_tb;

reg a0,a1,a2,a3,b0,b1,b2,b3;
wire c5, p6, p5, p4, p3, p2, p1, p0;

multiplier TES (a0,a1,a2,a3,b0,b1,b2,b3,c5, p6, p5, p4, p3, p2, p1, p0);
initial
    begin
        
        // $dumpfile("multiplier_tb.vcd");
        // dumpvars(0,multiplier_tb);

        assign a0 = 1'd0;
        assign a1 = 1'd0;
        assign a2 = 1'd0;
        assign a3 = 1'd0;
        assign b0 = 1'd0;
        assign b1 = 1'd0;
        assign b2 = 1'd0;
        assign b3 = 1'd0;

        #20
        // $fdisplay(fd, "a0 = %b\ta1=%b\ta2 = %b\ta3 = %b",a0,a1,a2,a3);
        // $fdisplay(fd, "b0 = %b\tb1=%b\tb2 = %b\tb3 = %b",b0,b1,b2,b3);
        // $fdisplay(fd, "c5 = %b\tp6=%b\tp5 = %b\tp4 = %b\tp3=%b\tp2 = %b\tp1 = %b\tp0 = %b\n",c5,p6,p5,p4,p3,p2,p1,p0);

        $display("a0 = %d\ta1=%d\ta2 = %d\ta3 = %d",a0,a1,a2,a3);
        $display("b0 = %d\tb1=%d\tb2 = %d\tb3 = %d",b0,b1,b2,b3);
        $display("c5 = %d\tp6=%d\tp5 = %d\tp4 = %d\tp3=%d\tp2 = %d\tp1 = %d\tp0 = %d\n",c5,p6,p5,p4,p3,p2,p1,p0);

        // $fclose(fd);  
    end

endmodule


