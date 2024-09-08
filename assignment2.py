# q1
int_var = int(input("Question 1, Enter Integer: "))
float_var = float(input("Question 1, Enter Float: "))
string_var = input("Question 1, Enter String: ")
print(type(int_var))
print(type(float_var))
print(type(string_var))

# q2
none_var = None
complex_var = complex(input("Question 2, Enter Complex Number (e.g., 1+2j): "))
byte_var = bytes(int(input("Question 2, Enter Integer for Byte Conversion: ")))
print(type(none_var))
print(type(complex_var))
print(type(byte_var))

# q3
name = input("Question 3, Enter Name: ")
age = int(input("Question 3, Enter Age: "))
enrollmentNo = input("Question 3, Enter Enrollment Number: ")
formatted_string = f"Welcome {name},\nStudent Age: {age},\nStudent id: {enrollmentNo}."
print(formatted_string)

# q4
name = input("Question 4, Enter Name: ")
height = float(input("Question 4, Enter Height: "))
blood_group = input("Question 4, Enter Blood Group: ")
formatted_message = f"Hello {name}\nHeight: {height}\nBlood Group: {blood_group}"
print(formatted_message)

# q5
distance = float(input("Question 5, Enter Distance in meters: "))
time = float(input("Question 5, Enter Time in seconds: "))
speed_kmph = (distance / 1000) / (time / 3600)
print(f"Speed: {speed_kmph:.2f} km/h")

# q6
speed = float(input("Question 6, Enter Speed in meters per second: "))
time = float(input("Question 6, Enter Time in seconds: "))
acceleration = speed / time
print(f"Acceleration: {acceleration:.2f} m/s²")

# q7
city_name = input("Question 7, Enter City Name: ")
population = int(input("Question 7, Enter Population: "))
area = float(input("Question 7, Enter Area in km²: "))
population_density = population / area
print(f"City: {city_name}\nPopulation: {population}\nArea: {area} km²\nPopulation Density: {population_density:.2f} people per km²")

# q8
total_population = int(input("Question 8, Enter Total Population: "))
urban_population = int(input("Question 8, Enter Urban Population: "))
percentage = (urban_population / total_population) * 100
print(f"Urban Population Percentage: {percentage:.2f}%")

# q9
integer_var = int(input("Question 9, Enter an Integer: "))
float_var = float(input("Question 9, Enter a Floating-point Number: "))
string_var = input("Question 9, Enter a String: ")
print(f"Value: {integer_var}, Type: {type(integer_var)}")
print(f"Value: {float_var}, Type: {type(float_var)}")
print(f"Value: {string_var}, Type: {type(string_var)}")

# q10
weight = float(input("Question 10, Enter Weight in kilograms: "))
height = float(input("Question 10, Enter Height in meters: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

# q11
name = input("Question 11, Enter Name: ")
marks_sem1 = float(input("Question 11, Enter Marks for Semester 1: "))
marks_sem2 = float(input("Question 11, Enter Marks for Semester 2: "))
marks_sem3 = float(input("Question 11, Enter Marks for Semester 3: "))
marks_sem4 = float(input("Question 11, Enter Marks for Semester 4: "))
average_marks = (marks_sem1 + marks_sem2 + marks_sem3 + marks_sem4) / 4
formatted_message = f"Hello {name}\nAverage Marks: {average_marks:.2f}"
print(formatted_message)

# q12
year = int(input("Question 12, Enter Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# q13
int_var = int(input("Question 13, Enter Integer: "))
float_var = float(input("Question 13, Enter Float: "))
string_var = input("Question 13, Enter String: ")
print(f"The value of var is {int_var} and its type is {type(int_var)}.")
print(f"The value of var is {float_var} and its type is {type(float_var)}.")
print(f"The value of var is {string_var} and its type is {type(string_var)}.")

# q14
city = input("Question 14, Enter City Name: ")
population = int(input("Question 14, Enter Population: "))
area = float(input("Question 14, Enter Area in sq km: "))
print(f"City: {city}\nPopulation: {population}\nArea: {area} sq km")

# q15
distance1, time1, distance2, time2 = map(float, input("Question 15, Enter Distance1, Time1, Distance2, Time2 (space-separated): ").split())
speed1 = distance1 / time1
speed2 = distance2 / time2
overall_average_speed = (speed1 + speed2) / 2
print(f"Car 1: Distance: {distance1} km\nTime: {time1} hours\nAverage Speed: {speed1:.2f} km/h")
print(f"Car 2: Distance: {distance2} km\nTime: {time2} hours\nAverage Speed: {speed2:.2f} km/h")
print(f"Overall Average Speed: {overall_average_speed:.2f} km/h")

# q16
radius = float(input("Question 16, Enter Radius of the base: "))
height = float(input("Question 16, Enter Height of the cone: "))
volume = (1/3) * 3.1416 * (radius ** 2) * height
print(f"Volume of the Cone: {volume:.2f}")

# q17
bool_var = bool(int(input("Question 17, Enter 1 or 0 for Boolean value: ")))
tuple_var = tuple(map(int, input("Question 17, Enter Tuple values (space-separated): ").split()))
range_var = range(int(input("Question 17, Enter end value for Range: ")))
print(type(bool_var))
print(type(tuple_var))
print(type(range_var))

# q18
radius = float(input("Question 18, Enter Radius of the Hemisphere: "))
volume = (2/3) * 3.1416 * (radius ** 3)
print(f"Volume of the Hemisphere: {volume:.2f}")

# q19
student_name = input("Question 19, Enter Student Name: ")
course_name = input("Question 19, Enter Course Name: ")
grade = input("Question 19, Enter Grade: ")
formatted_info = f"Student: {student_name}\nCourse: {course_name}\nGrade: {grade}"
print(formatted_info)

# q20
principal = float(input("Question 20, Enter Principal Amount: "))
annual_rate = float(input("Question 20, Enter Annual Interest Rate (in %): "))
compounding_frequency = int(input("Question 20, Enter Compounding Frequency: "))
years = int(input("Question 20, Enter Number of Years: "))
amount = principal * (1 + annual_rate / (compounding_frequency * 100)) ** (compounding_frequency * years)
print(f"Total Amount: {amount:.2f}")

#q21
space_string_int = input("Question 21, Enter Space Seperated Integer: ").split()
final_string = ""
for x in space_string_int:
    final_string += f"'{x}'"
print(final_string)

#q22
comma_values = input("Question 22, Enter Comma Seperated Integer: ").split(",")
int_values = []
for x in comma_values:
    try:
        value = int(x)
        int_values.append(value)
    except ValueError:
        None
print(int_values)

# q23
comma_booleans = input("Question 23, Enter Comma Separated Booleans (True, False): ").split(",")
int_values = []
for value in comma_booleans:
    if value.strip() == "True":
        int_values.append(1)
    elif value.strip() == "False":
        int_values.append(0)
print(" ".join(map(str, int_values)))

# q24
integer_value = int(input("Question 24, Enter an Integer: "))
string_value = input("Question 24, Enter a String Representing an Integer: ")
sum_value = integer_value + int(string_value)
print(f"Sum: {sum_value}")

# q25
integer_value = int(input("Question 25, Enter an Integer: "))
float_value = float(input("Question 25, Enter a Float: "))
concatenated_result = str(integer_value) + str(float_value)
print(f"Concatenated Result: {concatenated_result}")

# q26
boolean_value = input("Question 26, Enter a Boolean (True, False): ")
boolean_string = str(boolean_value)
print(f"Boolean as String: {boolean_string}")

# q27
string_value = input("Question 27, Enter a String Representing a Number: ")
float_value = float(input("Question 27, Enter a Float: "))
product = float(string_value) * float_value
print(f"Product: {product}")

# q28
integer_value = int(input("Question 28, Enter an Integer: "))
binary_representation = bin(integer_value)
print(f"Binary Representation: {binary_representation}")

# q29
string_value = input("Question 29, Enter a String Representing a Number: ")
reversed_integer = int(string_value[::-1])
print(f"Reversed Integer: {reversed_integer}")

# q30
float_value = float(input("Question 30, Enter a Floating-Point Number: "))
rounded_value = round(float_value)
print(f"Rounded Value: {rounded_value}")

# q31
integer_value = int(input("Question 31, Enter an Integer: "))
hex_representation = hex(integer_value)
print(f"Hexadecimal Representation: {hex_representation}")

# q32
string_value = input("Question 32, Enter a String: ")
digit_count = sum(c.isdigit() for c in string_value)
print(f"Number of Digits: {digit_count}")

# q33
string_value = input("Question 33, Enter a String: ")
ascii_sum = sum(ord(c) for c in string_value)
print(f"Sum of ASCII Values: {ascii_sum}")

# q34
string_value = input("Question 34, Enter a String: ")
ascii_values = [str(ord(c)) for c in string_value]
print("ASCII Values: " + " ".join(ascii_values))

# q35
string_value = input("Question 35, Enter a String: ")
can_convert = string_value.isdigit()
print(f"Can Convert to Integer: {can_convert}")

# q36
string_value = input("Question 36, Enter a String: ")
all_digits = string_value.isdigit()
print(f"All Digits: {all_digits}")

# q37
integer_value = int(input("Question 37, Enter an Integer: "))
float_string = input("Question 37, Enter a String Representing a Float: ")
product = integer_value * float(float_string)
print(f"Product: {product}")

# q38
ascii_values = input("Question 38, Enter Comma Separated ASCII Values: ").split(",")
characters = [chr(int(value.strip())) for value in ascii_values]
print(f"Resulting String: {''.join(characters)}")

# q39
float_string1 = input("Question 39, Enter a String Representing a Float: ")
float_string2 = input("Question 39, Enter Another String Representing a Float: ")
product = float(float_string1) * float(float_string2)
print(f"Product: {product}")

# q40
string_value = input("Question 40, Enter a String: ")
try:
    complex(string_value)
    is_complex = True
except ValueError:
    is_complex = False
print(f"Can be Interpreted as Complex: {is_complex}")