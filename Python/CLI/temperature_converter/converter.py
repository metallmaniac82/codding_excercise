def ConvertTo(input_unit, temperature ,output_unit):
    if output_unit == "C":
        if input_unit == "C":
            temp = temperature
            print("temperature ",round(temp,2),"\xb0 C \n" )
        elif input_unit == "F":
            temp = (5/9)*(temperature-32)
            print("temperature ",round(temp,2),"\xb0 C \n" )
        elif input_unit == "K":
            temp = temperature - 273.15
            print("temperature ",round(temp,2),"\xb0 C \n" )
    elif output_unit == "K":
        if input_unit == "C":
            temp = temperature + 273.15
            print("temperature ",round(temp,2)," K \n" )
        elif input_unit == "F":
            temp = ((5/9)*(temperature - 32)) + 273.15
            print("temperature ",round(temp,2)," K \n" )
        elif input_unit == "K":
            temp = temperature
            print("temperature ",round(temp,2)," K \n" )
    elif output_unit == "F":
        if input_unit == "C":
            temp = (9/5) * temperature + 32
            print("temperature ",round(temp,2),"\xb0 F \n" )
        elif input_unit == "F":
            temp = temperature
            print("temperature ",round(temp,2),"\xb0 F \n" )
        elif input_unit == "K":
            temp = ((9/5)*(temperature - 273.15)) + 32
            print("temperature ",round(temp,2) ,"\xb0 F \n" )

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def is_temperature_unit(unit):
    if unit == "C" or unit == "F" or unit == "K":
        return True
    else:
        return False

def unit_description():
    print("Temperature units used in software \n")
    print("C-celsius \n","F-fahrenheit \n","K-kelvin \n")

def main():
    while 1:
        unit_description()
        print("please select input unit from C, K or F \n")
        input_unit = input("").upper()
        if is_temperature_unit(input_unit) == False:
            print("incorrect temperature unit, please choose from C, K or F : \n")
            unit_description()
        else: 
            print("please select output unit from C, K or F \n")
            output_unit = input("").upper()
            if is_temperature_unit(output_unit) == False:
                print("incorrect temperature unit, please choose from C, K or F : \n")
                unit_description() 
            else:
                value = input("please provide temperature value e.g. 100 or 100.0 \n")
                if(False == is_number(value)):
                    print("value is NaN, please input value as integer, float or double format \n")
                else:
                    ConvertTo(input_unit,float(value),output_unit)
        next_turn = input("for break put N \n").upper()
        if next_turn == "N":
            break

               
main()