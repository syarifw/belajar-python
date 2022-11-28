a = ["AA","BB","C"]
b = ["CC","AA"]
c = []
d = []

for aa in a:
    if aa not in b:
        c.append(aa)
        continue
for aa in a:
    if aa in b:
        d.append(aa)
        continue

print('Belum sukses',c)
# print('Sukses',d)

# for aa in a:
#     if aa.startswith("PRAPR"):
#         pint.append(aa)
#     elif aa.startswith("PRABL"):
#         bl.append(aa)
#     elif aa.startswith("PRASM"):
#         sek.append(aa)
#     elif aa.startswith("PRATP"):
#         tp.append(aa)
#     elif aa.startswith("PRAPM"):
#         pij.append(aa)