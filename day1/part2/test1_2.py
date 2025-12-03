def read_all_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            input_data = file.readlines()
            #print(lines)
            for i in range(len(input_data)):
                input_data[i] = input_data[i].replace('\n','')
           # print(lines)
       
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    return input_data


file_path = './input.txt' 
input_data = read_all_lines(file_path)
print(input_data)
read_all_lines(file_path)