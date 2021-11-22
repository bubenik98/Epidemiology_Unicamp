import numpy as np
import random 
import matplotlib.pyplot as plt
from Schedule import *
from Move import *
from Detect_colissions import *
from Create_Population import *

'''
Creating necessary classes
'''
class University():
    def __init__(self, Coordinate):
        self.Coordinate = Coordinate
class Institute(University):
    def __init__(self, Coordinate, Area):
        super().__init__(Coordinate)
        self.Area = Area
class Classroom(University):
    def __init__(self, Coordinate, Area):
        super().__init__(Coordinate)
        self.Area = Area
R = 1     # Raio máximo para considerar o contágio
places_dict = []       
'''
Colocar as estruturas no places_dict
'''
num_students = 1      #Número de estudantes
num_professors = 1    #Número de alunos
num_frames = 1000     #Número de frames (Precisa ser múltiplo de 5, de 4 e de 17)
num_weeks = 1
num_frames_for_week = int(num_frames/num_weeks)
num_frames_for_day = int(num_frames_for_week/5)
num_frames_for_hour = int(num_frames_for_day/17)     # 17 é o número de horas presentes na simulação
time_to_run = int(num_frames_for_hour/4)
hours = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
days = ['Mon', 'Thu', 'Wed', 'Tue','Fri']
People = create_population(num_students, num_professors)
classroom = ['CB01', 'CB02', 'CB03']    #Substitutir pelas salas de aula disponíveis
Generate_Schedule(People, classroom)

for frame in range(num_frames):
    day_index = int(frame/num_frames_for_day)
    day_name = days[day_index % 5]
    hour = hours[int((frame - day_index * num_frames_for_day)/num_frames_for_hour)]
    time_step = frame - num_frames_for_day * day_index - num_frames_for_hour * (hour - 7)
    for person_class in range(len(list(People.keys()))):
        for person in People[person_class]:
            movement(person, places_dict, time_step, time_to_run, num_frames_for_hour, day_name, hour)

        restart_time = 0
    if frame % num_frames_for_day == 0:      # Critério para reiniciar a contagem do tempo de exposição
        restart_time = 1

    Sweep_n_prune(People, R, num_frames_for_hour, time_step, restart_time)    # Definir o raio mínimo de colisão
