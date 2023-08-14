def formatname(sname):
    fname = sname[0:1].upper() + sname[1:].lower()
    return fname


f_map = map(formatname, ["yifeng", "CHUANKUAN", "niHAO"])
print(list(f_map))
