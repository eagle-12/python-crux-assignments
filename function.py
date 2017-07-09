def is_divisible(m,n):
	if(m%n==0):
		return 1
	else:
		return 0
import math
def yikes(x):
	ans = x*math.exp(-x)+math.sqrt(1-math.exp(-x))
	return ans

def roots(a,b,c):
	if(b*b<4*a*c):
		print "error"
	else:
		ele = (b*b)-(4*a*c)
		ele = math.sqrt(ele)
		ans = ((-b)+(ele))/(2*a)
		ans2 = 	((-b)-(ele))/(2*a)
		print ans
		print ans2				
