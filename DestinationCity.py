Paths=[["B","C"],["D","B"],["C","A"]]
#OUTPUT=A
#give value 1 to city having route to other city and value 0 for city having no link

def destinationcity(paths):
  """
  FInd the destination city that has no furthur path to other city
  """
  outgoing_city={}
  for path in paths:
    citya,cityb=path
    outgoing_city[citya]=1
    outgoing_city[cityb]=outgoing_city.get(cityb,0)
  for city in outgoing_city:
    if outgoing_city[city]==0:
      return city

res=destinationcity(Paths)
print("Destination City:", res)
