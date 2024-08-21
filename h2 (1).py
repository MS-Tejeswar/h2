#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

class Child:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.vaccination_schedule = []

    def add_vaccination(self, vaccine_name, due_date):
        self.vaccination_schedule.append({'vaccine': vaccine_name, 'due_date': due_date})

    def get_vaccination_info(self):
        return self.vaccination_schedule

class VaccinationSystem:
    def __init__(self):
        self.children = {}

    def add_child(self, name, birth_date):
        child = Child(name, birth_date)
        self.children[name] = child
        print(f"Added child: {name}")

    def add_vaccination(self, child_name, vaccine_name, due_date):
        if child_name in self.children:
            self.children[child_name].add_vaccination(vaccine_name, due_date)
            print(f"Added vaccination for {child_name}: {vaccine_name} due on {due_date}")
        else:
            print("Child not found!")

    def view_vaccination_schedule(self, child_name):
        if child_name in self.children:
            schedule = self.children[child_name].get_vaccination_info()
            if schedule:
                print(f"Vaccination schedule for {child_name}:")
                for record in schedule:
                    print(f"{record['vaccine']} - Due on: {record['due_date']}")
            else:
                print(f"No vaccinations scheduled for {child_name}.")
        else:
            print("Child not found!")

    def check_reminders(self):
        today = datetime.date.today()
        for child in self.children.values():
            for record in child.get_vaccination_info():
                if record['due_date'] == today:
                    print(f"Reminder: {child.name} has a vaccination due today: {record['vaccine']}")

def main():
    system = VaccinationSystem()

    while True:
        print("\nVaccination Management System")
        print("1. Add Child")
        print("2. Add Vaccination")
        print("3. View Vaccination Schedule")
        print("4. Check Reminders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            birth_date = input("Enter child's birth date (YYYY-MM-DD): ")
            system.add_child(name, birth_date)

        elif choice == '2':
            child_name = input("Enter child's name: ")
            vaccine_name = input("Enter vaccine name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            system.add_vaccination(child_name, vaccine_name, datetime.date.fromisoformat(due_date))

        elif choice == '3':
            child_name = input("Enter child's name: ")
            system.view_vaccination_schedule(child_name)

        elif choice == '4':
            system.check_reminders()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




