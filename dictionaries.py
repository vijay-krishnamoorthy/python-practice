e={'Eid':100120,'name':'vijay','age':21}
e1={'Eid':100121,'name':'vijay','age':21}
e3={'Eid':100122,'name':'vijay','age':21}
print(e)
print(e.get('name'))
e['age']=22;
for i in e.keys():
    print(e[i])
for i,j in e.items():
    print(i,j)
