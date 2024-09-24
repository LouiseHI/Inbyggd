def input_list():
    input_list = []
    input_str = input("Enter numbers: ").split()
    for num in input_str:
        input_list.append(int(num))
    return input_list

def add_list(input_list):
    return sum(input_list)

print(add_list(input_list()))