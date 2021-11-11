####Importar o que precisa
import numpy as np
import random
from Create_Population import *
'''def infection_prob_equation(x):
  P = 1-np.exp()'''

collision_dict = {'Collisions':[], 'time': np.array([])}    #Conta o tempo em que uma colisão permanece acontecendo

def func(t, x):                     # Esta é a equação do Pedro
  gamma_shape = 1 #?????
  r = 0.00001     #??????
  Q = 1   #????????
  p = 1   #???????????

  q = np.random.gamma(gamma_shape)/(1+np.exp(np.random.normal(2,0.5) * (x - 2)))
  Prob = np.exp(-q*t*p/Q)
  return Prob

def Union(list1, list2):
  for i in list1:
    if not i in list2:
      list2.append(i)
  return list2

def solve_collision(collision_set):
  
  #----------------------------------------------------------------------------------------------------------
  # Será acrescentado as novas colisões ao dicionário global definido acima e será adcionado na contagem de tempo, espaços para contar os respectivos tempos das novas colisões
  # Em seguida, o tempo de cada colisão é acrescido de 1
  aux = len(collision_dict['Collisions'])
  collision_dict['Collisions'] = Union(list(collision_set), collision_dict['Collisions'])
  aux = len(collision_dict['Collisions']) - aux
  collision_dict['time'] = np.array(list(collision_dict['time']) + list(np.zeros(aux)))
  collision_dict['time'] += 1
  #----------------------------------------------------------------------------------------------------------


  #----------------------------------------------------------------------------------------------------------
  # Colisões que deixaram de existir são excluídas. Se elas voltarem a ocorrer em algum momento, os tempos são reiniciados
  i = 0
  aux = len(collision_dict['Collisions'])
  while i < aux:
    if not collision_dict['Collisions'][i] in collision_set:
      del collision_dict['Collisions'][i]
      collision_dict['time'] = np.delete(collision_dict['time'], i)
    else:
  #----------------------------------------------------------------------------------------------------------

  #----------------------------------------------------------------------------------------------------------
  # Se a colisão se mantém ativa, o indivíduo passa pelo risco de ser infectado
      Prob = func(collision_dict['Collisions'][i][2], collision_dict['time'][i] - 1) - func(collision_dict['Collisions'][i][2], collision_dict['time'][i])
      test = random.random()
      if test < Prob:
        collision_dict['Collisions'][i][1].Begin_Infection()

      if i < len(collision_dict['Collisions']) - 1:
        i += 1
      else:
        i = aux + 1  
  #----------------------------------------------------------------------------------------------------------


def detect_collision(p1, p2, R):                  
# Detect the proximity between two persons and returns the validity word and the distance
  if abs(p2.Position[0]-p1.Position[0]) > R:
    validation = 0
  if abs(p2.Position[1]-p1.Position[1]) > R:
    validation = 0
  norm_squared = (p1.Position[1] - p2.Position[1])**2 + (p1.Position[0] - p2.Position[0])**2
  if norm_squared <= R**2:
    validation  = 1
  else:
    validation = 0
  return validation, norm_squared


def Sweep_n_prune(People,R) -> None:
  """
  This function is responsible to detect all the possible "Collisions" ( pair of people that enter the maximum infectious radius of eachother) in a time complexity better than O(n^2), where n = len(People)
  """ 
  '''

  Para entender está função, favor assistir esse vídeo:
  ->  https://youtu.be/eED4bSkYCB8

  '''
  #Sort people by the x-axis
  New_People = []
  for key in People:
    New_People = New_People + People[key]
  New_People = sorted(New_People, key = lambda x : x.Position[0])
  active = []
  collision_set = set()
  for i in New_People:
    if i.Quarantined == False:
      if len(active)>1:
        
        #If there is at least one person in the active list and the interval of all the list coincides
        if abs(active[0].Position[0] - i.Position[0]) <= R:
          
          active.append(i)
        # If the new person does not bellong to the currente interval we check all the collisions in the active list
        else:
          for j in range(len(active)):
            for k in range(j):
              if (active[j].Infect >= 1 or active[k].Infect >=1) and not (active[j].Infect >= 1 and active[k].Infect >=1 ) and not(active[j].Infect <0 or active[k].Infect <0 ):
                validation, norm_squared = detect_collision(active[j], active[k], R)
                if validation == 1:
                  if active[j].Infect>=1:
                    collision_set.add((active[j],active[k], np.sqrt(norm_squared)))
                  else:
                    collision_set.add((active[k],active[j], np.sqrt(norm_squared)))

          # We then remove the first item of the active list, since all of his possible collsions have been checked
          active.remove(active[0])

          # We now start to remove all the itens of the active list, until the new item is in the interval of someone inside the active list or the active list is empty
          for j in active:
            if np.abs(j.Position[0] - i.Position[0]) <= R or len(active) == 0:
              active.append(i)
              break

            else:
              active.remove(j)
      else:
        active.append(i)

  # We can now solve all the collisions
 # for i in collision_set:
  solve_collision(collision_set)

'''People = {'Students':[], 'Professor': []}
for i in range(100):
  People['Students'].append(Student(0, False, False, {'day_of_week': 'Mon', 'hour': 7}, 20, 5, 15, 9, 0, 10*np.array([random.random(), random.random()]), False, 'IFGW'))

for i in range(100):
  People['Professor'].append(Professor(2, False, False, {'day_of_week': 'Mon', 'hour': 7}, 40, 5, 15, 9, 0, 10*np.array([random.random(), random.random()]), False, 'IFGW'))
for i in range(50):
  Sweep_n_prune(People, 1)

for i in People:
  for j in People[i]:
    print(j.Infect)'''