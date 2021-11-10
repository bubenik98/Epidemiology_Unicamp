import numpy as np
import random 
import matplotlib.pyplot as plt

'''
Creating necessary classes
'''
class people():
    def __init__(self, Schedule, Infect_State, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Velocity, Imune , Current_Place, Institute):
        self.Schedule = Schedule
        self.Infect_State = Infect_State
        self.Vaccinated = Vaccinated
        self.Quarantined  =Quarantined
        self.Time = Time
        self.Age  =Age
        self.Incubation_Period = Incubation_Period
        self.Death_Period = Death_Period
        self.Recover_Period = Recover_Period
        self.Infectivity = Infectivity
        self.Position = Position
        self.Imune = Imune
        self.Velocity = Velocity
        self.Current_Place = Current_Place
        self.Institute = Institute

class Student(people):
    def __init__(self, Schedule, Infect_State, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Velocity, Imune, Current_Place, Institute):
        super().__init__(Schedule, Infect_State, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Velocity, Imune, Current_Place, Institute)
class Professor(people):
    def __init__(self, Schedule, Infect_State, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Velocity, Imune, Current_Place, Institute):
        super().__init__(Schedule, Infect_State, Vaccinated, Quarantined, Time, Age, Incubation_Period, Death_Period, Recover_Period, Infectivity, Position, Velocity, Imune, Current_Place, Institute)

num_students = 1
num_professors = 1

