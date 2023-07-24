import json

from employee import details, employee_name, age, title

#Creates a dictionary from three arguments and returns it.
def create_dict(name, age, title):

    employee_dict = {
      'first_name': str(name),
      'age': int(age),
      'title': str(title)
    }
    return employee_dict

    raise NotImplementedError()

#Wrties json to another files.
def write_json_to_file(json_obj, output_file):

    newfile = open(output_file, "w")
    newfile.write(json_obj)
    newfile.close()
    return

    raise NotImplementedError()


def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    #Converts a dictionary to a json format.
    json_object = json.dumps(create_dict(employee_name, age, title))
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")


if __name__ == "__main__":
    main()
