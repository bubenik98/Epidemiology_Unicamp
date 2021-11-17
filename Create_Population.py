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
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Imune, Institute):
        self.Infect = Infect
        self.Vaccinated = Vaccinated
        self.Quarantined  = Quarantined
        self.Time = Time
        self.Age  =Age
        self.Incubation_Period = Incubation_Period
        self.Death_Period = Death_Period
        self.Recover_Period = Recover_Period
        self.Infectivity = Infectivity
        self.Position = Position
        self.Imune = Imune
        self.Institute = Institute
        self.Schedule = None

    def def_schedule(self, schedule):
        self.Schedule = schedule

    def Att_Position(self, velocity):
        self.Position = self.Position + velocity
        if self.Infect == 1:
            self.Incubation_Period -= 1
            if self.Incubation_Period <= 0:
                #self.Recover_Period = np.random.lognormal(9 * , '''Standart desviation''')
                self.Infect = 2  #????????????????
        if self.Infected == 2 or self.Infected == 3:
            self.Recover_Period -= 1
            if self.Recover_Period <= 0:
                self.Infect = -1

    def Begin_Infection(self):
        self.Infect = 1
        #self.Incubation_Period = np.random.lognormal('''mean''', '''std''')

class Student(people):
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Imune, Institute):
        super().__init__(Infect, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Imune, Institute)
class Professor(people):
    def __init__(self, Infect, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Imune, Institute):
        super().__init__(Infect, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Imune, Institute)

def create_population(n_students, n_professor):

    People = {'Students':[], 'Professor': []}

    for i in range(n_students):
        People['Students'].append(Student(0, False, False, {'day_of_week': 'Mon', 'hour': 7}, 20, 5, 15, 9, 0, np.array([random.random(), random.random()]), False, 'IFGW'))

    for i in range(n_professor):
        People['Professor'].append(Professor(0, False, False, {'day_of_week': 'Mon', 'hour': 7}, 40, 5, 15, 9, 0, np.array([random.random(), random.random()]), False, 'IFGW'))
    return People
