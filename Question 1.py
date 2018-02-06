
class Patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError ("This is an abstract method and needs to be implemented in derived classes")

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.cost = 1000
    def discharge(self):
        print(self.name, "Emergency Patient")

class HospitalizedPatient (Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.cost = 2000
    def discharge(self):
        print(self.name, "Hospitlized Patient")

class Hospital:
    def __init__(self):
        self.patient = []
        self.cost = 0

    def admit (self, patient):
        self.patient.append(patient)

    def discharge_all (self):
        for Patient in self.patient:
            Patient.discharge()
            self.cost += Patient.cost

    def get_total_cost (self):
        return self.cost

P1 = HospitalizedPatient ('P1')
P2 = HospitalizedPatient ('P2')
P3 = EmergencyPatient ('P3')
P4 = EmergencyPatient ('P4')
P5 = EmergencyPatient ('P4')

H = Hospital ()

H.admit(P1)
H.admit(P2)
H.admit(P3)
H.admit(P4)
H.admit(P5)
H.discharge_all()

print(H.get_total_cost())