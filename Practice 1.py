def convert_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()
cho = "HeLLo World"
result = convert_case(cho)
print(result)





def searchSubstr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"

subst = "chief"
st = "chiefkeef"
result = searchSubstr(subst, st)
print(result)




def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("введи нормально")

if __name__ == "__main__":
    number1 = get_valid_input("введи первое число")
    number2 = get_valid_input("введи второе число")
    sum_result = number1 + number2
    print(sum_result)








