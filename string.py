my_template_str = 'foo {0} bar {1} baz {2}'

print(my_template_str.format('ba', 'te', 'il'))
print(len(my_template_str.format('ba', 'te', 'il')))
print(my_template_str.format('ba', 'te', 'il').count('a'))
print(my_template_str.format('ba', 'te', 'il')[::-1])
list = my_template_str.format('ba', 'te', 'il').split(' ')
print(list)
print(list[::-1])
print(' '.join(list[::-1]))
