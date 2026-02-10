# TCP File Server
# This server sends files to clients who request them

import socket
import os

def start_file_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(1)

    print("📁 File Server Started!")
    print("📍 Listening on port 8000...")
    print("💡 Place files in the same folder as this script\n")

    while True:
        # Accept client
        client_socket, address = server_socket.accept()
        print(f"\n🎉 Client connected: {address}")

        # Receive filename request
        filename = client_socket.recv(1024).decode().strip()
        print(f"📥 Client requested: {filename}")

        # Check if file exists
        if os.path.exists(filename):
            # Send OK signal
            client_socket.send("OK".encode())
            print(f"✅ File found! Sending...")

            # Send file in chunks
            with open(filename, 'rb') as file:
                bytes_sent = 0
                while True:
                    chunk = file.read(1024)  # Read 1KB at a time
                    if not chunk:
                        break
                    client_socket.send(chunk)
                    bytes_sent += len(chunk)

            print(f"✅ Sent {bytes_sent} bytes")
        else:
            # Send error message
            error_msg = "ERROR: File not found on server"
            client_socket.send(error_msg.encode())
            print(f"❌ File not found: {filename}")

        client_socket.close()
        print(f"👋 Client {address} disconnected\n")
        print("⏳ Waiting for next client...")

if __name__ == "__main__":
    # Create a sample file if it doesn't exist
    if not os.path.exists("sample.txt"):
        with open("sample.txt", "w") as f:
            f.write("Hello from File Server!\nThis is a test file.\n")
        print("📝 Created sample.txt for testing\n")

    start_file_server()
