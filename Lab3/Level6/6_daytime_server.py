# Daytime Server (RFC 867)
# 🎯 ASSIGNMENT: This is the simplest server!
# Server sends current date/time and immediately closes connection

from datetime import datetime
import socket

def start_daytime_server():
    # Create TCP server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9013))  # Using 9013 instead of 13 (needs root)
    server_socket.listen(1)

    print("⏰ Daytime Server Started!")
    print("📍 Listening on port 9013...")
    print("💡 RFC 867 Protocol: Send time and close\n")

    try:
        while True:
            # Accept client connection
            client_socket, address = server_socket.accept()
            print(f"🎉 Client connected: {address}")

            # Get current date and time
            current_time = datetime.now().strftime("%A, %d-%b-%Y %H:%M:%S")

            # Send time to client
            client_socket.send(current_time.encode())
            print(f"📤 Sent: {current_time}")

            # Close connection immediately (RFC 867 requirement)
            client_socket.close()
            print(f"👋 Connection closed\n")

    except KeyboardInterrupt:
        print("\n🛑 Server shutting down...")
        server_socket.close()

if __name__ == "__main__":
    start_daytime_server()
