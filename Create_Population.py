import random
import numpy as np

'''
-> Parâmetros people.infect
    -> 0 = Suscetível
    -> 1 = Exposto
    -> 2 = Sintomático
    -> 3 = Assintomático
    -> -1 = Recuperado
    -> -2 = Morto
'''


class people():
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Death_Period, Position, Imune, Institute, identity):
        self.Infect = Infect
        self.Vaccinated = Vaccinated
        self.Quarantined  = Quarantined
        self.Time = Time
        self.Age  =Age
        self.Collision_time = {}
        self.Incubation_Period = None
        self.Death_Period = Death_Period
        self.Recover_Period = None
        self.Infectivity_epsilon = None
        self.Position = Position
        self.Imune = Imune
        self.Institute = Institute
        self.Schedule = None
        self.identity = identity
        self.dilution_r = None
        self.range_d = None

    def def_schedule(self, schedule):
        self.Schedule = schedule

    def Att_Position(self, velocity, day, hour, num_frames_for_day):
        self.Position = self.Position + velocity
        self.Time['day_of_week'] = day
        self.Time['hour'] = hour
        if self.Infect > 1:
            self.Recover_Period -= 1
            if self.Recover_Period <= 0:
                self.Infect = -1
        if self.Infect == 1:
            self.Incubation_Period -= 1
            if self.Incubation_Period <= 0:
                time = np.random.lognormal(1.5 , 0.1)
                self.Recover_Period = time * num_frames_for_day
                self.Infect = 2  #????????????????
        

    def Begin_Infection(self, num_frames_for_day):
        self.Infect = 1
        self.Infectivity_epsilon = np.log(1-np.random.gamma(1.88, 0.008))/np.log(0.999306)  #Função gamma - Parâmetros definidos pelo Pedro
        self.dilution_r = abs(np.random.normal(5, 2))      ### Tirar o abs
        self.range_d = abs(np.random.normal(1, 0.3))
        time = np.random.lognormal(1.5, 0.6)
        self.Incubation_Period = time * num_frames_for_day

class Student(people):
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Death_Period, Position, Imune, Institute, identity):
        super().__init__(Infect, Vaccinated, Quarantined, Time, Age, Death_Period, Position, Imune, Institute, identity)
class Professor(people):
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Death_Period, Position, Imune, Institute, identity):
        super().__init__(Infect, Vaccinated, Quarantined, Time, Age, Death_Period, Position, Imune, Institute, identity)

def create_population(n_students, n_professor, num_frames_for_day):

    People = {'Students':[], 'Professors': []}

    for i in range(n_students - 1):
        People['Students'].append(Student(0, False, False, {'day_of_week': 'Mon', 'hour': 7}, 20, 5, np.array([random.random(), random.random()]), False, np.random.choice(['IFGW', 'IMECC']), str(i)))
    People['Students'][0].Begin_Infection(num_frames_for_day)
    #print(num_frames_for_day)
    #print(People['Students'][0].Incubation_Period)
    for i in range(n_professor):
        People['Professors'].append(Professor(0, False, False, {'day_of_week': 'Mon', 'hour': 7}, 40, 5, np.array([random.random(), random.random()]), False, np.random.choice(['IFGW', 'IMECC']), str(n_students*i)))
    return People
