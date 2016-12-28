fout = open("150_orbits.csv","a+")
for line in open("hermus_mpn_error.0.params"):
  fout.write(line)
for num in range(1,149):
  f = open("hermus_mpn_error." + str(num) + ".params")
  f.next()
  for line in f:
    fout.write(line)
  f.close()
fout.close()