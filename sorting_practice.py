def bubble_sort(alist):
	sbool = True
	end = 1
	while sbool == True: 
		sbool = False
		for i in range(len(alist)-end):
			if alist[i+1] < alist[i]:
				alist[i+1], alist[i] = alist[i], alist[i+1]
				sbool = True
		end = end + 1

	return alist

print bubble_sort([3,6,1,0,7,5,9])





def bubble_rec(alist, sbool=True, end=1):	
	if sbool == False:
		return alist

	sbool = False
	for i in range(len(alist)-end):
		if alist[i+1] < alist[i]:
			alist[i+1], alist[i] = alist[i], alist[i+1]
			sbool = True
	

	return bubble_rec(alist, sbool,(end+1))

print bubble_rec([3,6,1,0,7,5,9])