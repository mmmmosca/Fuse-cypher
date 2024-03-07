import string
alphabet = list(string.ascii_uppercase)
word = list(str(input().upper()))
word_num = []

for letter in word:
	word_num.append(ord(letter))

for n in word_num:
	n = str(n)
	sn = int(len(n)/2)
	res = int(n[:sn])+int(n[sn:])
	print(alphabet[res],end='')
		
#It is an cyphering system that assigns each letter of the given word its corresponding ASCII value, divides this value in half, and then combines the results to obtain a new value, which is then converted back into a letter of the alphabet.