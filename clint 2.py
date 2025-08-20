# code غلا 
import socket
import time
import multiprocessing as mp

def send_message(server_socket, message):
    server_socket.send(message.encode('utf-8'))

def receive_message(server_socket):
    return server_socket.recv(1024).decode('utf-8')

def main0():
    host = '127.0.0.1'
    port = 5566

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    send_message(client_socket,"1")
    try:
        while True:
            response = receive_message(client_socket)
            print(response)

            if "Please enter your name" in response:
                name = input("Your name: ")
                send_message(client_socket, name)
            elif "Choose a destination" in response:
                destination = input("Choose a destination (e.g., 1, 2, 3, 4): ")
                send_message(client_socket, destination)
            elif "Do you accept the ride?" in response:
                user_input = input("Do you accept the ride? (yes/no): ")
                send_message(client_socket, user_input)
                if user_input.lower() == 'no':
                    print("Thank you. Goodbye!")
                    break  
            elif "Continue the ride?" in response:
                user_input = input("Continue the ride? (yes/no): ")
                send_message(client_socket, user_input)
            elif "Do you want to request another ride?" in response:
                user_input = input("Do you want to request another ride? (yes/no): ")
                send_message(client_socket, user_input)
                if user_input.lower() == 'no':
                    print("Goodbye!")
                    break
            else:
                print("Invalid response from the server.")

    except Exception as e:
        print(f"An error occurred: {e}")


#///////////////////////////////////////
        
def start_client2(host, port):
    host = '127.0.0.1'
    port = 5566

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
 
    try:
        send_message(client_socket,"2")
        response = receive_message(client_socket)
        user_input = "Please rate the driver"
        send_message(client_socket,user_input)
        response = receive_message(client_socket)
        print(response)
        user_input =input("Enter feed back ")
        send_message(client_socket,user_input)
        response = receive_message(client_socket)
        user_input =input(response)
        send_message(client_socket,user_input)
        done = True
    except Exception as e:
            print(f"An error occurred: {e}")
            done = True

    client_socket.close()

def main3(host, port):
    start_client2(host, port)

#////////////////////////////////////////////////
#///////////////////////////////////////////////
    # كود ليان ١
def cal_boss(ridesNum):
    total = ridesNum * 10
    bossShare = total * (100 - 30) / 100  # 30%
    eachBoss = int(bossShare / 4)
    return eachBoss

def cal_manger(ridesNum):
    total = ridesNum * 10
    MangersShare = total * (100 - 20) / 100  # 20%
    mangersIn = total - MangersShare
    eachManger = int(mangersIn / 180)
    return eachManger

def cal_driver(ridesNum):
    total = ridesNum * 10
    driversShare = total * (100 - 30) / 100  # 30%
    driversIn = total - driversShare
    eachDriver = int(driversIn / 2600)
    return eachDriver

def cal_car(ridesNum):
    total = ridesNum * 10
    CarsShare = total * (100 - 20) / 100  # 20%
    carsIn = total - CarsShare
    eachCar = int(carsIn / 1177)
    return eachCar

def cal_com(ridesNum):
    total = ridesNum * 10
    CarsShare = total * (100 - 20) / 100
    carsIn = total - CarsShare
    eachCar = int(carsIn / 1177)
    return eachCar

def main1():
    print("Enter the number of rides this year")
    rides = int(input())

    start = time.time()
    resultBoss = cal_boss(rides)
    resultManger = cal_manger(rides)
    resultDriver = cal_driver(rides)
    resultCar = cal_car(rides)
    resultCom = cal_com(rides)
    end = time.time()

    print(f"Each boss's profit: {resultBoss}$\n"
          f"Each Manger's profit: {resultManger}$\n"
          f"Each driver's profit:{resultDriver}$\n"
          f"Each car's maintance profit: {resultCar}$")

    print("\nNormal time:", end - start)

    start = time.time()
    p1 = mp.Process(target=cal_boss, args=(rides,))
    p2 = mp.Process(target=cal_manger, args=(rides,))
    p3 = mp.Process(target=cal_driver, args=(rides,))
    p4 = mp.Process(target=cal_car, args=(rides,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end = time.time()
    print("Multiprocessing time", end - start)

#/////////////////////////////////////////////////////
    

if __name__ == "__main__":
    print("~~ Welcome to Taxi Management System ~~")

    while True:
        print("Select 1 if you want to request a ride\n"
              "Select 2 if you want to rate a driver\n"
              "Select 3 if you're a Manager")

        choose = int(input("Enter your choice: "))

        if choose == 1:
            print("Requesting a ride...")
            main0()

        elif choose == 2:
            while True:
                try:
                    rating = int(input("Please rate the driver on a scale from 1 to 5 (1 = Poor, 5 = Excellent): "))
                    
                    if 1 <= rating <= 3:
                        print("We're sorry for your bad experience.\n"
                              "Please wait a moment until a manager gets connected with you.")
                        
                        main3('127.0.0.1', 5567)  
                    
                    elif 4 <= rating <= 5:
                        print(f"Thank you for rating the driver {rating} out of 5!")
                    
                    else:
                        print("Invalid rating. Please enter a number between 1 and 5.")
                    
                    break  
                except ValueError:
                    print("Invalid input. Please enter a valid number.")


        elif choose == 3:
            password = input("Enter the admin's password: ")

            if password == "taxsm":
                while True:
                    print("Choose the operation you would like to perform"
                          "\n1 - Profit Management"
                          "\n2 - Exit")

                    operation = input("Enter your choice: ")

                    if operation == '1':
                        print("Profit Management operation selected.")
                        main1()
                        break

                    elif operation == '2':
                        print("Exiting the program. Goodbye!")
                        break

                    else:
                        print("Invalid input. Please enter 1, 2, or 3.")

            else:
                print("Incorrect password. Access denied.")

        else:
            print("Invalid input. Please enter 1, 2, or 3.")

        continue_program = input("Do you want to continue? (yes/no): ").lower()
        if continue_program != 'yes':
            print("Exiting the program. Goodbye!")
            break