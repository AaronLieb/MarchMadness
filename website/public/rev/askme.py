def dec(x):
	return x - 1


def check(password):
	if dec(ord(password[0])) != ord('e'):
		return False
	if dec(ord(password[1])) != 107:
		return False
	if dec(ord(password[2])) != ord('`'):
		return False
	if dec(ord(password[3])) != 102:
		return False
	if dec(ord(password[4])) != ord('z'):
		return False
	if dec(ord(password[5])) != 51:
		return False
	if dec(ord(password[6])) != ord('r'):
		return False
	if dec(ord(password[7])) != 98:
		return False
	if dec(ord(password[8])) != ord('0'):
		return False
	if dec(ord(password[9])) != 48:
		return False
	if dec(ord(password[10])) != ord('|'):
		return False
	return True

password = input()
if check(password):
	print("Correct! Submit your input as the flag")
else:
	print("Try again")
