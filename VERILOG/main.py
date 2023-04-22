import os
count = 0
while count<256:

    file_ptr = open("multiplier_tb.v" , "r")
    file_ptr_write = open("ass_python.v" , "w")

    for line in file_ptr:
        #read replace the string and write to output file
        temp1 = 1

        if line == "module multiplier_tb;\n":
            str = f"module ass_python;\n"
            file_ptr_write.write(str)

        elif line == "        assign a0 = 1'd0;\n":
            temp = count>>0 & temp1
            str = f"        assign a0 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign a1 = 1'd0;\n":
            temp = count>>1 & temp1
            str = f"        assign a1 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign a2 = 1'd0;\n":
            temp = count>>2 & temp1
            str = f"        assign a2 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign a3 = 1'd0;\n":
            temp = count>>3 & temp1
            str = f"        assign a3 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign b0 = 1'd0;\n":
            temp = count>>4 & temp1
            str = f"        assign b0 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign b1 = 1'd0;\n":
            temp = count>>5 & temp1
            str = f"        assign b1 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign b2 = 1'd0;\n":
            temp = count>>6 & temp1
            str = f"        assign b2 = 1'd{temp};\n"
            file_ptr_write.write(str)

        elif line == "        assign b3 = 1'd0;\n":
            temp = count>>7 & temp1
            str = f"        assign b3 = 1'd{temp};\n"
            file_ptr_write.write(str)   
        
        else:
            file_ptr_write.write(line)

      
    file_ptr_write.close()
    file_ptr.close()

    
    cmd = f"iverilog -o multiplier_tb  ass_python.v multiplier.v full_adder.v half_adder.v"
    os.system(cmd)
    cmd = f"vvp multiplier_tb"
    os.system(cmd)
    #os.ngspice.system("quit") 
    count = count+1