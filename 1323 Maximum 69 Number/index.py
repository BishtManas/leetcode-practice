def maximum69Number(num):
  
    num_list = list(str(num))
    
  
    for i in range(len(num_list)):
        if num_list[i] == '6':
            num_list[i] = '9'
            break
    

    return int(''.join(num_list))


if __name__ == "__main__":
    num = int(input("Enter a number (only 6s and 9s): "))
    result = maximum69Number(num)
    print(f"Maximum number after at most one change: {result}")
