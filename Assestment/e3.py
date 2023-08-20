def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees



employees = [["jonh", 33, 65000], ["Sarah", 24, 75000], ["Josie", 29, 100000], ["Jason", 26, 55000], ["Connor", 25, 110000]]

sortby = "name"

print(sort_employees(employees, sortby))