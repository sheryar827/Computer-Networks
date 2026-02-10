# TCP File Client
# Downloads files from the file server

import socket

def download_file(filename):
    # Connect to file server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('127.0.0.1', 8000))
        print(f"✅ Connected to file server")

        # Send filename request
        client_socket.send(filename.encode())
        print(f"📤 Requesting: {filename}")

        # Receive response
        response = client_socket.recv(2).decode()

        if response == "OK":
            print("✅ Server has the file! Downloading...")

            # Receive file data
            downloaded_filename = "downloaded_" + filename
            with open(downloaded_filename, 'wb') as file:
                bytes_received = 0
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)
                    bytes_received += len(chunk)

            print(f"✅ Download complete! ({bytes_received} bytes)")
            print(f"💾 Saved as: {downloaded_filename}")
        else:
            # Receive error message
            error = client_socket.recv(1024).decode()
            print(f"❌ {error}")

    except ConnectionRefusedError:
        print("❌ Error: File server is not running!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    print("📁 File Download Client\n")
    filename = input("Enter filename to download: ")
    download_file(filename)
