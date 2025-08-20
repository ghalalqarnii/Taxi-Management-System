import socket
import threading
import requests
import googlemaps

def send_message(client_socket, message):
    try:
        client_socket.send(message.encode('utf-8'))
    except (BrokenPipeError, ConnectionResetError):
        print("Client disconnected unexpectedly.")
        raise

def receive_message(client_socket):
    return client_socket.recv(1024).decode('utf-8')

def get_location(api_key):
    gmaps = googlemaps.Client(key=api_key)

    try:
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
        response = requests.post(url)

        if response.status_code == 200:
            location_data = response.json()
            latlng = f"{location_data['location']['lat']},{location_data['location']['lng']}"

            places_result = gmaps.places_nearby(location=latlng, radius=5000, type='point_of_interest')
            
            nearby_locations = [place['name'] for place in places_result['results']]

            return latlng, nearby_locations
        else:
            print(f"Failed to retrieve location. Status code: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"Error retrieving location: {e}")
        return None, None

def calculate_distance(start, end):

    return 10.0  




def handle_client(client_socket, api_key):
    try:
        print("Handling client...")
        if "2" in receive_message(client_socket):
            send_message(client_socket, f"Rating")
            handle_client2(client_socket, api_key)
            return
        send_message(client_socket, "Please enter your name: ")
        name = receive_message(client_socket)
        print(f"Received name: {name}")

        while True:
            location, nearby_locations = get_location(api_key)
            if location and nearby_locations:
                send_message(client_socket, f"Your current location: {location}")
                for i, line in enumerate(nearby_locations[:4]):
                    send_message(client_socket, f"Nearby locations: {i + 1} - {line.strip()}")

                while True:
                    send_message(client_socket, "Choose a destination from the nearby locations (e.g., 1, 2, 3, 4): ")
                    destination_index = int(receive_message(client_socket))

                    if 0 <= destination_index < len(nearby_locations):
                        destination = nearby_locations[destination_index - 1]
                        print(f"Received ride request from {name} to {destination}")

                        driver_info = "Your driver is John. Car: Toyota Prius, License Plate: ABC123"
                        send_message(client_socket, driver_info)

                        distance = calculate_distance(location, destination)
                        send_message(client_socket, f"Estimated distance to your destination: {distance} miles")

                        while True:
                            send_message(client_socket, "Do you accept the ride? (yes/no): ")
                            user_input = receive_message(client_socket)

                            if user_input.lower() == 'yes':

                                send_message(client_socket, "Simulating ride...")

                                send_message(client_socket, "Your ride is complete. Here is your bill: $10.00")

                                send_message(client_socket, "Do you want to request another ride? (yes/no): ")
                                user_input = receive_message(client_socket)

                                if user_input.lower() == 'yes':
                                    break  
                                elif user_input.lower() == 'no':
                                    send_message(client_socket, "Thank you. Goodbye!")
                                    return
                                else:
                                    send_message(client_socket, "Invalid response. Please enter 'yes' or 'no'.")
                            elif user_input.lower() == 'no':
                                send_message(client_socket, "Thank you. Goodbye!")
                                return
                            else:
                                send_message(client_socket, "Invalid response. Please enter 'yes' or 'no'.")

                        break
                    else:
                        send_message(client_socket, "Invalid destination index. Please choose a valid index.")
            else:
                send_message(client_socket, "Failed to retrieve location or nearby locations. Please try again.")
    except (BrokenPipeError, ConnectionResetError):
        print("Client disconnected unexpectedly.")
    finally:

        client_socket.close()
        print("Connection closed.")



def handle_client2(client_socket, port):
    try:
        if "Please rate the driver" in receive_message(client_socket):
            send_message(client_socket, "We're sorry to hear that your experience was less than satisfactory.")

            send_message(client_socket, "\nPlease share additional details about your experience and any suggestions for improvement:")
            feedback = receive_message(client_socket)
            print(f"Received feedback: {feedback}")
            send_message(client_socket, "Thank you for providing feedback. We have received your suggestions and will work on improving our service.")

    except (BrokenPipeError, ConnectionResetError):
        print("Client disconnected unexpectedly.")
    finally:

        client_socket.close()
        print("Connection closed.")


def start_server(api_key):
    host = '127.0.0.1'
    port = 5566

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Accepted connection from {client_addr}")

        try:
            client_thread = threading.Thread(target=handle_client, args=(client_socket, api_key))
            client_thread.start()
        except Exception as e:
            print(f"Error creating client thread: {e}")
            continue

def start_server_rating():
    host = '127.0.0.1'
    port = 5566 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Rating Server listening on {host}:{port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Accepted rating connection from {client_addr}")

        try:
            rating_thread = threading.Thread(target=handle_client_rating, args=(client_socket,))
            rating_thread.start()
        except Exception as e:
            print(f"Error creating rating thread: {e}")
            continue

def main():
    api_key = "AIzaSyD5AXYAJfBWC4CQLS2dN_0yyWyFjqhbfjI"
    start_server(api_key)
    start_server_rating()


if __name__ == "__main__":
    main()
