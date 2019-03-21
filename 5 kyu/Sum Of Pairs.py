def sum_pairs(ints, s):
    seenarr = []
    # efficiency gain: use a hashing structure instead
    # of a list for O(1) lookup.
    index = 0
    rtnarr = []
    for int in ints:
        if int not in seenarr :
            if s - int in seenarr and not s - int == int:
                rtnarr.append(s - int);
                rtnarr.append(int)
                return rtnarr
				#you can return anonymous objects in python! [,] :O 
            seenarr.append(int)
        elif int + int == s and int in seenarr:
            rtnarr.append(int);
            rtnarr.append(int)
            return rtnarr
        index += 1
    return None
	
	#------
	#best practices
	def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)