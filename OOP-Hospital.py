# define a class for doctors
class Doctor:
    def __init__(self, name, ID, department, salary, specialization):  # constructor
        self.name = name
        self.ID = ID
        self.department = department
        self.salary = salary
        self.specialization = specialization
        self.patients = 0

    def treat_patient(self, quantity):
        # increase the number of patients treated by the doctor
        self.patients += quantity
        print(f"{self.name} treated {quantity} patients.")

    def get_salary(self):
        # calculate the salary of the doctor based on the number of patients treated and the specialization
        self.salary = self.salary + (self.patients * 10) + (self.specialization * 100)
        print(f"{self.name}'s salary is {self.salary}.")

    def change_department(self, new_department):
        # change the department of the doctor
        self.department = new_department
        print(f"{self.name} changed department to {self.department}.")


# ============= MAIN BODY =================
my_doctor = Doctor("Alice", "001", "Emergency", 1000, 1)     # object or instance with specialization 1 (cardiologist)
my_doctor1 = Doctor("Bob", "010", "Surgery", 1200, 2)        # object or instance with specialization 2 (surgeon)

my_doctor.treat_patient(20)
my_doctor.get_salary()
my_doctor.change_department("Cardiology")
