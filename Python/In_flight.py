# Inflight entertainment
# Auhtor: Pavan Kumar Paluri

def in_flight(movies:list, flight_duration:int):
  output=[]
  watch_set =set()
  level = 0
  for movie in movies:
    # output.append([])
    if flight_duration - movie not in watch_set:
      watch_set.add(movie)
    else:
      output.append((movie, flight_duration-movie))
      # now remove it from the set - To avoid adding duplicates.
      watch_set.remove(flight_duration-movie)
    level+=1
  return output

if __name__=="__main__":
  print(in_flight([60,30,120,60,90,70, 50], 120))
