import string
alphabet = list(string.ascii_uppercase)
word = list(str(input().upper()))
word_num = []

for letter in word:
	word_num.append(alphabet.index(letter)+1)

for n in word_num:
	try:
		n = str(n)
		sn = int(len(n)/2)
		res = int(n[:sn])+int(n[sn:])
		print(alphabet[res],end='')
	except:
		print(alphabet[int(n)],end='')
		
#It is an encryption system that assigns each letter of the given word its corresponding ASCII value, divides this value in half, and then combines the results to obtain a new value, which is then converted back into a letter of the alphabet.