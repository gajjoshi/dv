modern_family =['lEwiS_HaMiLton', 'MaX_vERsTapPen', 'SebASTIaN_vEtTeL','ChaRLeS_lEcLeRc']
indices=list()
drivers=list()
for i, name in enumerate(modern_family):
    indices.append(i)
    drivers.append(name.lower().replace('_', '-'))

print(indices)
print(drivers)
n=lambda a:len(a)
temp=list(map(n,drivers))
print(temp)
indices=list(map(sum,(zip(indices,temp))))
indices.sort(reverse=True)
F1_drivers=dict(zip(indices,drivers))
print(F1_drivers)