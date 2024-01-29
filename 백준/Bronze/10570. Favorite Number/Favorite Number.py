def count_number(number_list):
    count_dict = {}
    
    for number in number_list:
        if number not in count_dict:
            count_dict[number] = 0
            
        count_dict[number] += 1
        
    return count_dict

def favorite_number(number_list):
    count_dict = count_number(
        number_list=number_list
    )
    
    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_count[0][0]


if __name__ == "__main__":
    for _ in range(int(input())):
        number_list = []
        for _ in range(int(input())):
            number = int(input())
            number_list.append(number)
            
        print(favorite_number(number_list=number_list))