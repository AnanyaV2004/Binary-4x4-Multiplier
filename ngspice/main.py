import os
count = 0
while count<256:

    file_ptr = open("circuit.cir" , "r")
    file_ptr_write = open("ass_python.cir" , "w")

    for line in file_ptr:
        #read replace the string and write to output file
        temp1 = 1
        if line == "VinA0 A0 GND dc 0\n":
            temp = count & temp1
            str = f"VinA0 A0 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinA1 A1 GND dc 0\n':
            temp = count>>1 & temp1
            str = f"VinA1 A1 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinA2 A2 GND dc 0\n':
            temp = count>>2 & temp1
            str = f"VinA2 A2 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinA3 A3 GND dc 0\n':
            temp = count>>3 & temp1
            str = f"VinA3 A3 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinB0 B0 GND dc 0\n':
            temp = count>>4 & temp1
            str = f"VinB0 B0 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinB1 B1 GND dc 0\n':
            temp = count>>5 & temp1
            str = f"VinB1 B1 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinB2 B2 GND dc 0\n':
            temp = count>>6 & temp1
            str = f"VinB2 B2 GND dc {temp}\n"
            file_ptr_write.write(str)

        elif line == 'VinB3 B3 GND dc 0\n':
            temp = count>>7 & temp1
            str = f"VinB3 B3 GND dc {temp}\n"
            file_ptr_write.write(str)   
        
        else:
            file_ptr_write.write(line)

      
    file_ptr_write.close()
    file_ptr.close()

    
    cmd = f"ngspice ass_python.cir"
    os.system(cmd)
    #os.ngspice.system("quit") 
    count = count+1