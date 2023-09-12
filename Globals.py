def get_input(type = "string", range_input = None):
    if range_input == None:
        if type == "int":
            range_input = [-2147483648, 2147483647]
        elif type == "float":
            range_input = [-1000000.0, 1000000.0]
    while True:
        try:
            if type == "string":
                choice = str(input())
            elif type == "int":
                choice = int(input())
                if not range_input[0] <= choice <= range_input[1]:
                    raise Exception
            elif type == "float":
                choice = float(input())
                if not range_input[0] <= choice <= range_input[1]:
                    raise Exception
            return choice
        except Exception:
            if type == "string":
                print("You must enter a string.")
            elif type == "int":
                print("You must enter an int between " + str(range_input[0]) + " and " + str(range_input[1]) + ".")
            elif type == "float":
                print("You must enter a float between " + str(range_input[0]) + " and " + str(range_input[1]) + ".")
