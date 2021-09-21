# find the seed of a number
# e.g. 1716 = 143*1*4*3, so 143 is the seed

def product_of_num(num: int) -> int:
    # if num is single digit, return the num
    if num < 10:
        return num
    product: int = 1
    while num != 0:
        # to get the last digit of the num, we need to % 10
        remainder: int = num % 10
        product *= remainder
        # take put the last digit
        num = num // 10
    return product


# ---------- main ----------
user_num: int = int(input("Enter number: "))

# for loop to loop thru all the numbers from 1 - user_num +1
# only test the num that has no remainder
for possible_num in range(1, user_num+1):
    if user_num % possible_num == 0:
        if product_of_num(possible_num)*possible_num == user_num:
            print(possible_num)
