tuple4 = (('a', 23),('b', 37),('c', 11),
('d',29))
tuple4= list(tuple4)
tuple4.sort(key=lambda x:x[1])
tuple4=tuple(tuple4)
print(tuple4)


