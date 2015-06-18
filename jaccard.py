def jaccard(a,b):
	a=a.split()
	b=a.split()
	union = list(set(a+b))
	intersection = list(set(a) - (set(a)-set(b)))
	print "Union - %s" % union
	print "Intersection - %s" % intersection
	jaccard_coeff = float(len(intersection))/len(union)
	print "Jaccard Coefficient is = %f " % jaccard_coeff