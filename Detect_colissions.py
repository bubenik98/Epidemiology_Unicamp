####Importar o que precisa


def detect_collision (p1, p2,R) -> bool:
  if abs(p2.Position[0]-p1.Position[0]) > R:
    return False
  if abs(p2.Position[1]-p1.Position[1]) > R:
    return False

  if (p1.Position[1] - p2.Position[1])**2 + (p1.Position[0] - p2.Position[0])**2 <= R**2:
    return True


def Sweep_n_prune(People,R) -> None:
  """
  This function is responsible to detect all the possible "Collisions" ( pair of people that enter the maximum infectious radius of eachother) in a time complexity better than O(n^2), where n = len(People)
  """
  #Sort people by the x-axis
  People = sorted(People, key=lambda People: People.Position[0])
  active = []
  collision_set = set()
  for i in People:
    if i.Quaren == False:
        if len(active)>1:
          #If there is at least one person in the active list and the interval of all the list coincides
          if abs(active[0].Position[0] - i.Position[0]) <= R:
            active.append(i)
          # If the new person does not bellong to the currente interval we check all the collisions in the active list
          else:
            for j in range(len(active)):
              for k in range(j):
                if (active[j].Infect >= 1 or active[k].Infect >=1) and not (active[j].Infect >= 1 and active[k].Infect >=1 ) and not(active[j].Infect <0 or active[k].Infect <0 ) and detect_collision(active[j], active[k], R):
                    if active[j].Infect>=1:
                        collision_set.add((active[j],active[k]))
                    else:
                        collision_set.add((active[k],active[j]))

            # We then remove the first item of the active list, since all of his possible collsions have been checked
            active.remove(active[0])

            # We now start to remove all the itens of the active list, until the new item is in the interval of someone inside the active list or the active list is empty
            for j in active:
              if abs(j.Position[0] - i.Position[0]) <= R or len(active) == 0:
                active.append(i)
                break

              else:
                active.remove(j)
        else:
            active.append(i)

  # We can now solve all the collisions
  for i in collision_set:
    solve_collision(i[0],i[1])
