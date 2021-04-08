universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(list_of_universities):
    students = [university[1] for university in list_of_universities]
    tuition_fees = [university[2] for university in list_of_universities]

    return [students, tuition_fees]


def mean(elements):
    return sum(elements) / len(elements)


def median(elements):
    elements.sort()

    if len(elements) % 2 == 0:
        median_index = round(len(elements) / 2)
        first_half, second_half = elements[:median_index], elements[median_index:]
        result = first_half[-1] + second_half[0]
        return result
    else:
        median_index = round(len(elements) / 2)
        first_half, second_half = elements[:median_index], elements[median_index:]
        if len(first_half) > len(second_half):
            return first_half[-1]
        else:
            return second_half[0]


students_list, tuition_fees_list = enrollment_stats(universities)

msg = f"Total students: {sum(students_list)} \n" \
      f"Total tuition fees: {sum(tuition_fees_list)} \n" \
      f"\n" \
      f"Student mean: {mean(students_list):.2f} \n" \
      f"Student median: {median(students_list)} \n" \
      f"\n" \
      f"Tuition mean: {mean(tuition_fees_list):.2f} \n" \
      f"Tuition median: {median(tuition_fees_list)}"

print(msg)
