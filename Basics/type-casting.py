# Implicit casting
a = 5          # integer
b = 2.0        # float
c = a + b      # a is implicitly converted to float
print(f'Implicit casting: {c} (type: {type(c)})')

# Explicit casting
x = 10         # integer
y = float(x)   # explicitly convert integer to float
print(f'Explicit casting: {y} (type: {type(y)})')

# String to int
s = "20"
n = int(s)     # explicitly convert string to integer
print(f'String to int: {n} (type: {type(n)})')  

# Float to int
f = 9.8
i = int(f)     # explicitly convert float to integer (truncates decimal)
print(f'Float to int: {i} (type: {type(i)})')

# Int to string
num = 100
str_num = str(num)  # explicitly convert integer to string
print(f'Int to string: {str_num} (type: {type(str_num)})')

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # explicitly convert list to tuple
print(f'List to tuple: {my_tuple} (type: {type(my_tuple)})')

# Tuple to list
my_new_list = list(my_tuple)  # explicitly convert tuple to list
print(f'Tuple to list: {my_new_list} (type: {type(my_new_list)})')

# String to float
str_float = "3.14"
float_num = float(str_float)  # explicitly convert string to float
print(f'String to float: {float_num} (type: {type(float_num)})')

# Bool to int
bool_val = True
int_val = int(bool_val)  # explicitly convert boolean to integer
print(f'Bool to int: {int_val} (type: {type(int_val)})')

# Int to bool
zero_int = 0
bool_from_int = bool(zero_int)  # explicitly convert integer to boolean
print(f'Int to bool: {bool_from_int} (type: {type(bool_from_int)})')

# Set to list
my_set = {1, 2, 3}
set_to_list = list(my_set)  # explicitly convert set to list
print(f'Set to list: {set_to_list} (type: {type(set_to_list)})')

# List to set
list_to_set = set(my_list)  # explicitly convert list to set
print(f'List to set: {list_to_set} (type: {type(list_to_set)})')

