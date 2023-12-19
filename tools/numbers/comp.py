def sumOfDigits(number):

        num_str = str(number)
        digit_sum = 0    
        for digit in num_str:  
            digit_sum += int(digit)
        return digit_sum

def isPal(number):
        original_number = number
        reversed_number = 0
        while number > 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number = number // 10
        return original_number == reversed_number