from rich import print 
from enum import Enum
import json

cars=list()

class Operations(Enum):
    PRINT = 1
    ADD = 2
    DELETE = 3
    UPDATE = 4
    EXIT = 5
    INFO = 6
    CLEAR = 7
    
def menu():
    for oper in Operations: print(f'{oper.value} - {oper.name}')   
    return Operations(int(input("Choose your action:")))

def print_cars():
    for index, car in enumerate(cars):
        print(f'[bold magenta]({index}) Type: {car['type']}, Model: {car['model']}, Color:{car['color']}, Cast.Name: {car['castName']}[/]')

def add_car():
    cars.append({"type":input("Car Type?  "), "model":input("Car Model?  "), "color":input(" Color?  "), "castName": input("Client name?  ")})
    
def get_index():
    print_cars()
    choice=int(input("Choose car's number: "))
    return choice
    

def delete_car():
    choice= get_index()
    print(f'The car: {cars[choice]} is deleted')
    cars.pop(choice)

def update_car():
    choice= get_index()
    cars[choice]={"type":input("Car Type?  "), "model":input("Car Model?  "), "color":input(" Color?  "), "castName": input("Client name?  ")}
    print(f'The car: {cars[choice]} is updated successfully')

def info():
    print(f'[red]Total cars in the garage: {len(cars)}[/] ')
    types = set(car['type'] for car in cars)
    print('Car types:')
    for car_type in types:
        count = sum(1 for car in cars if car['type'] == car_type)
        print(f'  {car_type}: {count} units')
        
def clear_data():
    global cars
    cars = [] 
    print("[red]All car data has been successfully cleared.[/]")        
        
        
def save_cars_to_file():
    with open('cars.json', 'w', encoding='utf-8') as file:
        json.dump(cars, file, ensure_ascii=False, indent=4)
        

def load_cars_from_file():
    try:
        with open('cars.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

cars = load_cars_from_file()      
    

if __name__ == "__main__":  
    while True:
        user_selection = menu()
        if user_selection== Operations.EXIT: exit()    
        if user_selection== Operations.ADD:
            add_car()
            save_cars_to_file()
        if user_selection== Operations.PRINT: print_cars()
        if user_selection== Operations.DELETE:
            delete_car()
            save_cars_to_file()
        if user_selection== Operations.UPDATE:
            update_car()
            save_cars_to_file()
        if user_selection== Operations.INFO: info()
        if user_selection == Operations.CLEAR: 
            clear_data()
            save_cars_to_file()