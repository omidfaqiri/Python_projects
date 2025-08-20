bin_num = str(input("What is the binary_number ?"))
start_point = len(bin_num) -1
power_counter = 0
base_10_total = 0

while (start_point >= 0):
    base_10_total = base_10_total + int(bin_num(start_point)) * (2 **power_counter)
    start_point -= 1
    power_counter += 1
    print(base_10_total)    
