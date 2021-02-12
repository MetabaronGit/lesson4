seq = "asidfgsajdnvirnhbvjasndvkjsnavdn"
resume = dict()

for obj in seq:
    if resume.get(obj) == None:
        resume[obj] = 1
    else:
        resume[obj] += +1
# místo if bloku by stačilo: resume[obj] = resume.setdefault(obj,0) + 1
print(resume)


# vzorové řešení
# -----------------------------------
seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
counts = {}
for num in seq:
    counts[str(num)] = counts.setdefault(str(num),0) + 1
print(counts)