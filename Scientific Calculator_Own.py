import math

def scientific_calculator():
    print("~~~ Scientific Calculator ~~~")
    print("Available functions: +, -, *, /, **, %(modulo)")
    print("Further available functions: sin(x), cos(x), tan(x), log(x), sqrt(x), exp(x)[e raised to the power x]")
    print("Use 'math.' prefix for functions, e.g., math.sin(x), where x is an angle in radians")
    print("Type quit to exit")

    while True:
        a=input("Enter expression")
        if a.lower()=="quit":
            print("Exiting Calculator")
            break

        try:
            result= eval(a, {"__builtins__": None}, {"math": math})
            print("Result:", result)
        except Exception as e:
             print("Error:", e)

if __name__=="__main__":
    scientific_calculator()
        
