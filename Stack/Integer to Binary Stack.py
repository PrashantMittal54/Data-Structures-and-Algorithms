def convert_int_to_bin(dec_num):
    binary_list = []
    while dec_num:
        # temp = dec_num%2
        if dec_num % 2 == 0:
            binary_list.append('0')
        else:
            binary_list.append('1')
        dec_num = dec_num//2
    binary_list = binary_list[::-1]
    number = int(''.join(binary_list))
    return number


print(convert_int_to_bin(2))
