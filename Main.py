import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from Schedule import *
from Move import *
from Detect_colissions import *
from Create_Population import *
from matplotlib.animation import FuncAnimation

def Animation(frame, archives, dict_places):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    for place in dict_places:
        ax.scatter(places_dict[place].Coordinate[0], places_dict[place].Coordinate[1], c = 'gray', s = 25)

    file = open(archives[frame][0], 'r')
    person = file.readline()
    person = str(file.readline())
    
    while person != '':
        parameter = ['','','']
        aux = 0
        for c in person:
            if c == ';':
                parameter[aux] = float(parameter[aux])
                aux += 1
            else:
                if c != '\n':
                    parameter[aux] += c
        #print(parameter)
        ax.scatter(parameter[0], parameter[1], c = str(parameter[2]), s = 10)
        person = file.readline()
    ax.set_title(archives[frame][1] + ' - '  + archives[frame][2] + 'h')
       
    file.close()

'''
Creating necessary classes
'''
class University():
    def __init__(self, Coordinate):
        self.Coordinate = Coordinate
class Institute(University):
    def __init__(self, Coordinate):
        super().__init__(Coordinate)
        self.Area = 0
class Classroom(University):
    def __init__(self, Coordinate):
        super().__init__(Coordinate)
        self.Area = 0
class Restaurant(University):
    def __init__(self, Coordinate):
        super().__init__(Coordinate)
        self.Area = 0
R = 10     # Raio máximo para considerar o contágio
places_dict = {'Bandeco': Restaurant(np.array([0,0])),'IMECC': Institute(np.array([-2,-2])), 'IFGW': Institute(np.array([2,2])), 'CB01': Classroom(np.array([-5,5])), 'CB02': Classroom(np.array([5,5])), 'CB03': Classroom(np.array([5, -5]))}       
'''
Colocar as estruturas no places_dict
'''
num_students = 20      #Número de estudantes
num_professors = 2    #Número de alunos
num_frames = 4*5*17*5     #Número de frames (Precisa ser múltiplo de 5, de 4 e de 17)
num_weeks = 2
num_frames_for_week = int(num_frames/num_weeks)
num_frames_for_day = int(num_frames_for_week/5)
num_frames_for_hour = int(num_frames_for_day/17)     # 17 é o número de horas presentes na simulação
time_to_run = int(num_frames_for_hour/4)
hours = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
days = ['Mon', 'Tue', 'Wed', 'Thu','Fri']
People = create_population(num_students, num_professors, num_frames_for_day)
classroom = ['CB01', 'CB02', 'CB03']    #Substitutir pelas salas de aula disponíveis
Generate_Schedule(People, classroom)
#print(People['Professors'][-1].Schedule)
Population = {'S':[], 'E': [], 'I': [], 'R': []}
time_step = 0
#listao = {}
t = num_frames
archives = []
for frame in range(t):
    day_index = int(frame/num_frames_for_day)
    day_name = days[day_index % 5]
    hour = hours[int((frame - day_index * num_frames_for_day)/num_frames_for_hour)]
    #time_step = frame - num_frames_for_day * day_index - num_frames_for_hour * (hour - 7)
    listao = {'x':[], 'y':[], 'color':[]}
    for person_class in list(People.keys()):
        for person in People[person_class]:
            movement(person, places_dict, time_step, time_to_run, num_frames_for_hour, day_name, hour, num_frames_for_day, frame)
            listao['x'].append(person.Position[0])
            listao['y'].append(person.Position[1])
            listao['color'].append(person.color)
    name = str(frame) + '.csv'
    pd.DataFrame(listao).to_csv(os.getcwd()[:47] + name, index = False, sep = ';')
    archives.append([os.getcwd()[:47] + name, day_name, str(hour)])

    #print(People['Students'][0].Position)


    Sweep_n_prune(People, 10, num_frames_for_hour, time_step, num_frames_for_day, frame)    # Definir o raio mínimo de colisão
    time_step += 1
    time_step = time_step % num_frames_for_hour
    S = 0
    E = 0
    I = 0
    R = 0
    for classe in People:
        for person in People[classe]:
            if person.Infect == 0:
                S += 1
            if person.Infect == 1:
                E += 1
            if person.Infect > 1:
                I += 1
            if person.Infect < 0:
                R += 1
    Population['S'].append(S)
    Population['E'].append(E)
    Population['I'].append(I)
    Population['R'].append(R)
time = np.arange(0, num_frames)
plt.plot(time, Population['S'], label = 'Susceptibles')
plt.plot(time, Population['E'], label = 'Exposed')
plt.plot(time, Population['I'], label = 'Infectious')
plt.plot(time, Population['R'], label = 'Recovered')
plt.legend()
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('Number of People')
plt.title('Infection Evolution')
l = int(len(time)/4)
days = np.array([time[l], time[2*l], time[3*l], time[4*l-1]])
day_label = np.array([int(time[l]/num_frames_for_day), int(time[2*l]/num_frames_for_day), int(time[3*l]/num_frames_for_day), int(time[4*l-1]/num_frames_for_day)])
plt.xticks(ticks = days, labels = day_label)#, labels = np.arange(1, len(days)))
plt.show()
print(Population['R'][-1])
fig, ax = plt.subplots()

anim = FuncAnimation(fig, func = Animation, frames = t, fargs = [archives, places_dict], interval = 0.1)
plt.show()
plt.close()