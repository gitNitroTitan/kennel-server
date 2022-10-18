EMPLOYEES = [
        {
            "id": 1,
            "name": "Ryan McHenchman"
        },
        {
            "id": 2,
            "name": "Squirrel Girl"        }
    ]
def get_all_employees():
    """Function getting all employees."""
    return EMPLOYEES

def get_single_employee(id):
    """gets the individual employee by id"""
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
