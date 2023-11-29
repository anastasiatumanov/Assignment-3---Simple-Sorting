people = [
    {
        "firstName": "Joe", 
        "lastName": "Wu",
        "age": 28, 
        "idNumber": 734928238
    },
    {
        "firstName": "Amira",
        "lastName": "Abadi", 
        "age": 32, 
        "idNumber": 567856856
    },
    {
        "firstName": "Emily", 
        "lastName": "Jones", 
        "age": 24, 
        "idNumber": 456754675
    },
    {
        "firstName": "James", 
        "lastName": "Bond", 
        "age": 43, 
        "idNumber": 253794370
    },
    {
        "firstName": "Ariel", 
        "lastName": "Zara", 
        "age": 19, 
        "idNumber": 356554665
    },
    {
        "firstName": "Emilio", 
        "lastName": "Palma", 
        "age": 13, 
        "idNumber": 996758677
    },
    {
        "firstName": "Max", 
        "lastName": "Jonathan", 
        "age": 17, 
        "idNumber": 250700675
    },
    {
        "firstName": "Hampton", 
        "lastName": "Brooks", 
        "age": 45, 
        "idNumber": 196784635
    },
    {
        "firstName": "Eric", 
        "lastName": "Mendington", 
        "age": 38, 
        "idNumber": 226354777
    },
    {
        "firstName": "Monny", 
        "lastName": "Wasowski", 
        "age": 92, 
        "idNumber": 236711676
    }
   ]

def compare_people_by_name(person_1, person_2):
    """Return -1 if person_1's name comes before person_2's name
    (alphabetically), 0 if person_1 and person_2 have the same name,
    and 1 if person_1's name comes after person_2's name.
    """
    name_1 = (person_1["lastName"] + "," + person_1["firstName"]).lower()
    name_2 = (person_2["lastName"] + "," + person_2["firstName"]).lower()
    if name_1 < name_2:
        return -1
    if name_1 == name_2:
        return 0
    return 1

def compare(thing_1, thing_2, comparator):
    """Return a negative int if thing_1 is less than thing_2,
    0 if thing_1 is equal to thing_2, and a positive int if
    thing_1 is greater than thing_2.
    """
    return comparator(thing_1, thing_2)

def compare_ages(age_1, age_2):
    """Return a negative int if age_1 is less than age_2,
    0 if age_1 is equal to age_2, and a positive int if
    age_1 is greater than age_2.
    """
    if age_1.get("age") < age_2.get("age"):
        return -1
    if age_1.get("age") == age_2.get("age"):
        return 0
    return 1

def compare_idNumbers(num_1, num_2):
    """Return a negative int if num_1 is less than num_2,
    0 if num_1 is equal to num_2, and a positive int if
    num_1 is greater than num_2.
    """
    if num_1.get("idNumber") < num_2.get("idNumber"):
        return -1
    if num_1.get("idNumber") == num_2.get("idNumber"):
        return 0
    return 1


def bubble_sort(a, compare_function):
    """Sorts list a in ascending order by value using function
    compare_function() for value comparisons.
    """
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if compare(a[i - 1], a[i], compare_function) > 0:
                a[i - 1], a[i] = a[i], a[i - 1]  # swap
                swapped = True
        n -= 1


def selection_sort(a, compare_function):
    n = len(a)
    for i in range(n-1):
        m=i
        for j in range(i+1, n):
            if compare(a[j], a[m], compare_function) < 0:
                m=j
        if m!= i:
            a[i], a[m] = a[m], a[i]

def search(a, person, comparator):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left+right) // 2
        comparison = compare(a[mid], person, comparator)
        if comparison == 0:
            return mid
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    print("Sorting people by name.")
    selection_sort(people, compare_people_by_name)
    selection_sort(people, compare_ages)
    selection_sort(people, compare_idNumbers)
    search(people, {"firstName": "Francis", "lastName": "Wu"}, compare_people_by_name)
    for d in people:
        print(d)

if __name__ == "__main__":
    main()