# This is the source code for the YouTube video
# "7 Simple Tricks to Write Better Python Code"
# The video can be found at: "https://youtu.be/VBokjWj_cEA"
# For complete explanations of each block, watch video
# This is simply a compilation of Sebastiaan Mathot's tips

#TRICK 1 - USING ENUMERATE FUNCTION
print('\n** TRICK 1: USING ENUMERATE FUNCTION **')

cities = ['Marseille', 'Amsterdam', 'New York', 'London']

# the bad way
# i = 0
# for city in cities:
#     print(i, city)
#     i += 1


# the good way
for i, city in enumerate(cities):
    print(i, city)

#TRICK 2 - USING ZIP FUNCTION
print('\n** TRICK 2: USING ZIP FUNCTION **')

x_list = [1,2,3]
y_list = [2,4,6]

# the bad way
# for i in range(len(x_list)):
#     x = x_list[i]
#     y = y_list[i]
#     print(x,y)

# the good way
for x, y in zip(x_list, y_list):
    print(x,y)

#TRICK 3 - USING TUPLE SUBSTITUTION
print('\n** TRICK 3: USING TUPLE SUBSTITUTION **')

x = 10
y = -10
print('Before: x = %d, y = %d' % (x, y))

# the bad way
# tmp = y
# y = x
# x = tmp
# print('After: x = %d, y = %d' % (x, y))

# the good way
x,y = y, x
print('After: x = %d, y = %d' % (x, y))

#TRICK 4 - IMPROVED DICTIONARY SEARCH
print('\n** TRICK 4: IMPROVED DICTIONARY SEARCH')

ages = {
    'Mary'      : 31,
    'Jonathan'  : 28,
    #'Dick'      : 51
    }

# the bad way
# if 'Dick' in ages:
#     age = ages['Dick']
# else:
#     age = 'Unknown'
# print('Dick is %s years old' % age)

# the good way
age = ages.get('Dick', 'Unknown')
print('Dick is %s years old' % age)

#TRICK 5 - FOR / ELSE SEARCH
print('\n** TRICK 5: FOR / ELSE SEARCH **')

needle = 'd'
haystack = ['a',
            'b',
            'c',
            #'d'  #Comment or uncomment to toggle found or not found
            ]

# the bad way
# found = False
# for letter in haystack:
#     if needle == letter:
#         print('Found!')
#         found = True
#         break
# if not found:
#     print('Not found!')

# the good way
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else: #if no break occurred
    print('Not found!')

#TRICK 6 - IMPROVED FILE READING
print('\n** TRICK 6: IMPROVED FILE READING **')

# PLACE 'pimpin_aint_easy.txt' in same directory as 7SimpleTricks.py

# the bad way
# f = open('pimpin_aint_easy.txt')
# text = f.read()
# for line in text.split('\n'):
#     print(line)
# f.close()

# the better way
# f = open('pimpin_aint_easy.txt')
# for line in f:
#     print(line)
# f.close()

# the better way
with open('pimpin_aint_easy.txt') as f:
    for line in f:
        print(line)

#TRICK 7 - TRY-EXCEPT-ELSE
print('\n** TRICK 7: TRY-EXCEPT-ELSE **')

# the bad way
# print('Converting!')
# try:
#     print(int('x'))
# except:
#     print('Conversion failed!')
# print('Done')

#the good way
print('Converting!')
try:
    print(int('x'))
    # print(int('1')) # Comment / Uncomment these two lines to toggle success/failure
except:
    print('Conversion failed!')
else: #if no except runs
    print('Conversion succeeded!')
finally: # Always runs
    print('Done')