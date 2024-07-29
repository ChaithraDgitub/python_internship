class Train:
    def _init_(self):
        self.database = {
            'MXP': [4, 5, 8, 10, 6, 4, 1],
            'HXP': [2, 3, 7, 9, 9, 6, 3],
            'CXP': [7, 9, 12, 21, 5, 7, 13]
        }

    def create_train(self):
        Train_Number = input("Enter the train Name that you want to create: ")
        No_of_seats = input("Enter seats for each day: ")
        seats_list = list(map(int, No_of_seats.split()))
        self.database[Train_Number] = seats_list
        print(self.database)

    def update_seats(self):
        train_number = input("Enter the train name you should change: ")
        if train_number in self.database:
            print('0-->monday,1-->tuesday,2-->wednesday,3-->thursday,\
                  4-->friday,5-->saturday,6-->sunday')
            index = int(input("Enter the day to change: "))
            new_value = int(input("Enter the updated seat count: "))
            if 0 <= index <= 6:
                self.database[train_number][index] = new_value
                print(f"Updated seats for Train {train_number} on day {index}:
                       {self.database[train_number]}")
            else:
                print(f"Invalid day code {index}")
        else:
            print(f"Train {train_number} not found in the database")

    def delete_train(self):
        Train_Name = input("Enter the train name that you want to delete: ")
        if Train_Name in self.database:
            del self.database[Train_Name]
        else:
            print("The invalid Train Name")
        print(self.database)

    def predict_ticket_volume(self):
        T_N = input("Enter the Train name to predict: ")
        print('0-->monday,1-->tuesday,2-->wednesday,3-->thursday,4-->friday,\
              5-->saturday,6-->sunday')
        day_input = int(input("Enter the day: "))
        days_of_week = ['Monday', 'Tuseday', 'Wednesday', 'Thursday', 
                        'Friday', 'Saturday', 'Sunday']
        if T_N in self.database and 0 <= day_input <= 6:
            day = days_of_week[day_input]
            seats = self.database[T_N][day_input]
            print(f"Number of seats in {T_N} on {day} is {seats}")
        else:
            print("Invalid train name")

    def count_trains(self):
        num_trains=len(self.database)
        print(f"Number of trains:{num_trains}") 

    def Suggest_Staff_allocation(database):
        Train_name=input("Enter the train name:")
        print( '0-->monday,1-->tuesday,2-->wednesday,3-->thursday,4-->friday,\
              5-->saturday,6-->sunday')
        Day_input=int(input("Enter the day :"))
        days_of_week=['Monday','Tuseday','Wednesday','Thursday','Friday',
                      'Saturday','Sunday']
        if Train_name in database and 0<=Day_input<=6:
           Day=days_of_week[Day_input]
           seats=database[Train_name][Day_input]
           staff=int(seats/2)
           print(f"IN Train {Train_name} on {Day} {staff}  of staffs are allocated")
        else:
           print("Invalid input day")              


train_function = Train()

while True:

    print("1.Create the train")
    print("2.update the train") 
    print("3.Delete the train")
    print("4.Predict the train")
    print("5.Count the number of trains")
    print("6.Staff allocation in trains")
    print("Enter -1 to exit")

    choice = int(input("Enter your choice: "))
    if choice == -1:
        break
    match choice:
        case 1:
            train_function.create_train()
        case 2:
            train_function.update_seats()
        case 3:
            train_function.delete_train()
        case 4:
            train_function.predict_ticket_volume()
        case 5:
            train_function.count_trains()
        case 6 :
            train_function.Suggest_Staff_allocation()        
        case _:
            print("Invalid choice")
