import re

for test_string in ['555-1212', 'a12-1243']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
	print test_string, 'is a valid US local phone number'
    else:
	print test_string, 'rejected'
