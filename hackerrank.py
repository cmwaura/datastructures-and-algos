def main():
	a0,a1,a2 = raw_input().strip().split(' ')
	l=a0,a1,a2 = [int(a0),int(a1),int(a2)]
	b0,b1,b2 = raw_input().strip().split(' ')
	m =b0,b1,b2 = [int(b0),int(b1),int(b2)]
	n = 0
	a,b = 0, 0
	while n<len(m):
		if m[n]> l[n]:
			b += 1
			
		elif l[n]>m[n]:
			a += 1
		else:
			pass
		n += 1
	print a, b

main()