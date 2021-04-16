

def get(first_number, last_number, properties):
    numbers = []
    for i in range(first_number, last_number + 1):
        numbers.append(i)

    n = 2
    response_index = len(numbers) // n
    if numbers[response_index] == property:
        return response_index
    elif numbers[response_index] < properties:
        first_number = numbers[response_index]
        get(first_number, last_number, properties)
        # response = (first_number + last_number) // n
    elif numbers[response_index] > properties:
        last_number = numbers[response_index]
        get(first_number, last_number, properties)
        # response = (first_number + last_number) // n


result = get(1, 100, 78)
print(result)
