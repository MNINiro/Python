def add_check_digit(upc_str):
       upc_str = str(upc_str)

       if len(upc_str) != 11:
              raise Exception("Invalid length")

       odd_sum = 0

       even_sum = 0

       for i, char in enumerate(upc_str):

              j = i+1

              if j % 2 == 0:

                   even_sum += int(char)
              else:
                   odd_sum += int(char)



       total_sum = (odd_sum * 3) + even_sum

       mod = total_sum % 10

       check_digit = 10 - mod

       if check_digit == 10:

              check_digit = 0
       return upc_str + str(check_digit)



#upc_str=[1, 7, 5, 3, 6, 8, 9, 5, 6, 5, 4, 0];

upc_str="02345600007"
print(add_check_digit(upc_str))
