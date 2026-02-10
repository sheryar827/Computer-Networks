# Daytime Client
# Connects to daytime server and receives current time

import socket

def get_daytime():
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to daytime server
        client_socket.connect(('127.0.0.1', 9013))
        print("✅ Connected to Daytime Server\n")

        # Receive time from server
        time_data = client_socket.recv(1024).decode()
        print(f"⏰ Server Time: {time_data}")

    except ConnectionRefusedError:
        print("❌ Error: Daytime server is not running!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client_socket.close()
        print("\n👋 Disconnected")

if __name__ == "__main__":
    print("⏰ Daytime Client\n")
    get_daytime()
