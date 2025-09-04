
while (1):
    unit_input= input("\nPlease enter the unit: ")
    unit = unit_input.capitalize()
    if unit in ('C', 'F', 'K'):
        input_temp = input("Please enter the temperature in that unit: ")
        if unit == 'C':
            temp_C = float(input_temp)
            temp_F = temp_C * 9/5 + 32
            temp_K = temp_C + 273.15

        elif unit == 'F':
            temp_F = float(input_temp)
            temp_C = (temp_F - 32) * 5/9
            temp_K = temp_C + 273.15
        else:
            temp_K = float(input_temp)
            temp_C = temp_K - 273.15
            temp_F = temp_C * 9 / 5 + 32
        print(f"Temperature = {temp_C:.1f}C = {temp_F:.1f}F = {temp_K:.1f}K")
    else:
        print("\nError: Invalid unit detected (ONLY 'C', 'F', 'K')\n")



