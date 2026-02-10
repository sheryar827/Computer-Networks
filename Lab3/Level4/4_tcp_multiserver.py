# TCP Multi-Client Server with Threading
# This server can handle MULTIPLE clients at the same time using threads

import socket
import threading

def handle_client(client_socket, address):
    """
    This function handles ONE client
    Each client gets their own thread running this function
    """
    print(f"\n🎉 New client connected: {address}")

    # Send welcome message
    welcome = f"Welcome client {address}! Type 'bye' to disconnect."
    client_socket.send(welcome.encode())

    # Keep talking to this client
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024).decode().strip()

            if not data or data.lower() == 'bye':
                print(f"👋 Client {address} disconnected")
                break

            print(f"📥 {address}: {data}")

            # Send echo response
            response = f"Echo: {data}"
            client_socket.send(response.encode())

        except:
            print(f"❌ Error with client {address}")
            break

    # Close this client's connection
    client_socket.close()

# Main server code
def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 7000))
    server_socket.listen(5)  # Can queue up to 5 clients

    print("🚀 Multi-Client TCP Server Started!")
    print("📍 Listening on port 7000...")
    print("✨ Can handle multiple clients simultaneously!\n")

    try:
        while True:
            # Wait for new client (this line blocks)
            client_socket, address = server_socket.accept()

            # Create a new thread for this client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()

            # Show how many clients are active
            active_clients = threading.active_count() - 1  # -1 for main thread
            print(f"📊 Active clients: {active_clients}")

    except KeyboardInterrupt:
        print("\n🛑 Server shutting down...")
        server_socket.close()

# Run the server
if __name__ == "__main__":
    start_server()
