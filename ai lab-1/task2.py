def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# Example usage:
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]
even_sum, odd_sum = sum_even_odd(num_list)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")