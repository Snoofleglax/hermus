import numpy as np
import scipy as sp
import os
import files as fi

def get_devs(b,v,r):
  N = len(b)
  bmean = np.mean(b)
  print bmean
  barg = np.subtract(b,bmean)
  bsq = np.power(barg,2)
  bquot = np.divide(bsq,N-1)
  bsum = np.sum(bquot)
  bd = np.sqrt(bsum)
  print str("b error = " + str(bd))
  vsq = np.power(v,2)
  vquot = np.divide(vsq,N-1)
  vsum = np.sum(vquot)
  vd = np.sqrt(vsum)
  print str("v error = " + str(vd))
  rsq = np.power(r,2)
  rquot = np.divide(rsq,N-1)
  rsum = np.sum(rquot)
  rd = np.sqrt(rsum)
  print str("r error = " + str(rd))
  

if __name__ == "__main__": 	
	data1 = fi.read_file("bdev")
	data2 = fi.read_file("vdev")
	data3 = fi.read_file("rdev")
	b = data1[:]
	v = data2[:]
	r = data3[:]
	get_devs(b,v,r)