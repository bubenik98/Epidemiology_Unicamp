import numpy as np
import random
from Schedule import *

def random_velocity(average_velocity):
    velocity = random.normalvariate(average_velocity, 0.5)
    angle = random.uniform(0, 360)
    angle_rad = (angle/360)*2*np.pi
    velocity_vector = np.array([velocity * np.cos(angle_rad), velocity * np.sin(angle_rad)])
    return velocity_vector


def movement(person, places_dict, time_step_between_hours, time_to_run, unity_time_per_hour, day, hour, num_frames_for_day):    # time_step corresponde ao frame em questão sendo analisado. Total_frames é o número total de frames empregado na simulação de uma semana
    '''
    ---------------- Colocar na Main
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    hours = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    
    unity_time_per_day = int(total_unity_time/5)                     # Frames totais contidos em um dia
    unity_time_per_hour = int(unity_time_per_day/len(hours))            # Frames totais em uma hora
    day = person.Time['day_of_the_week']
    hour = person.Time['hour']
    
    for i in range(len(days)):
        if days[i] == day:
            day_index = i
    time_step_between_hours = time_step - unity_time_per_day * day_index - unity_time_per_hour * (hour - 7)   # time_step_between_hour é a quantidade de unidades de tempo entre horas, como se fossem os minutos. Está é nossa menor unidade de tempo na simulação 
    time_to_run = int(unity_time_per_hour/4)       #Momento em que o aluno ve que tem uma aula e começa a ir em direção a ela
    '''
    
    hours = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    standart_velocity = 1
    #day = person.Time['day_of_the_week']
    #hour = person.Time['hour']
    if isinstance(person, Student) :
        if person.Schedule[day][hour] == '':
            velocity = random_velocity(standart_velocity)
            for place in places_dict:                         # Talvez vamos tirar
                if places_dict[place].Area > 0:
                    norm_squared = (places_dict[place].Coordinate[0] - person.Position[0])**2 + (places_dict[place].Coordinate[0] - person.Position[0])**2
                    if norm_squared <= places_dict[place].Area/(2*np.pi):
                        velocity = (-1) * (places_dict[place].Coordinate - person.Position)     # A pessoa não entra nos institutos por engano
            if hour != hours[-1]:
                if person.Schedule[day][hour + 1] != '':
                    if time_step_between_hours + time_to_run >= unity_time_per_hour:
                        future_goal = places_dict[person.Schedule[day][hour + 1]]
                        velocity = (future_goal.Coordinate - person.Position)/time_to_run
        else:
            goal = places_dict[person.Schedule[day][hour]]
            norm_squared = (goal.Coordinate[0] - person.Position[0])**2 + (goal.Coordinate[1] - person.Position[1])**2
            if norm_squared >= goal.Area/(2*np.pi):
                velocity = goal.Coordinate - person.Position
            else:
                velocity = random_velocity(max(np.sqrt(goal.Area/(8*np.pi)), standart_velocity)) #+ (standart_velocity/10)*(goal.Coordinate - person.Position)/np.sqrt(norm_squared)

            if hour != hours[-1]:
                if person.Schedule[day][hour + 1] != '':
                    if time_step_between_hours + time_to_run >= unity_time_per_hour:
                        future_goal = places_dict[person.Schedule[day][hour + 1]]
                        velocity = (future_goal.Coordinate - person.Position)/time_to_run
                else:
                    velocity = (-1)*(goal.Coordinate - person.Position)

    if isinstance(person, Professor) :
        
        if person.Schedule[day][hour] == '':
            goal = places_dict[person.Institute]

        else:
            goal = places_dict[person.Schedule[day][hour]]

        
        norm_squared = (goal.Coordinate[0] - person.Position[0])**2 + (goal.Coordinate[1] - person.Position[1])**2
        if norm_squared >= goal.Area/(2*np.pi):
            velocity = (goal.Coordinate - person.Position)
        else:
            velocity = random_velocity(standart_velocity) #+  (standart_velocity/10)*(goal.Coordinate - person.Position)/np.sqrt(norm_squared)

        if person.Time['hour'] == 13:
            velocity = random_velocity(standart_velocity)

        if hour != hours[-1]:
            if person.Schedule[day][hour + 1] != '':
                if time_step_between_hours + time_to_run >= unity_time_per_hour:
                    future_goal = places_dict[person.Schedule[day][hour + 1]]
                    velocity = (future_goal.Coordinate - person.Position)/time_to_run

    person.Att_Position(velocity, day, hour, num_frames_for_day)


    return None


