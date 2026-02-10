# TCP Multi-Client (works with threaded server)
# You can run multiple copies of this client at the same time!

import socket

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('127.0.0.1', 7000))
    print("✅ Connected to multi-client server!\n")

    # Receive welcome message
    welcome = client_socket.recv(1024).decode()
    print(f"Server: {welcome}\n")

    # Chat loop
    while True:
        # Get message from user
        message = input("You: ")

        # Send to server
        client_socket.send(message.encode())

        # Check if user wants to exit
        if message.lower() == 'bye':
            print("👋 Goodbye!")
            break

        # Receive echo response
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}\n")

except ConnectionRefusedError:
    print("❌ Error: Server is not running!")
    print("💡 Start the server first, then run this client.")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    client_socket.close()
