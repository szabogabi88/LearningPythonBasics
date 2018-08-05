
# Default arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok=input(prompt)
		if ok in ( 'y', 'yes', 'YES', 'Yes' ):
			return True
		if ok in ( 'n', 'no', 'NO', 'No' ):
			return False
		retries=retries-1
		if retries<0:
			raise ValueError('invalid user response')
		print(reminder)
