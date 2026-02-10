# OOP Custom Servers - Examples
# Shows how to create specialized servers by inheriting from TCPServer

from oop_base_server import TCPServer
from datetime import datetime
import socket

# ==========================================
# EXAMPLE 1: Echo Server
# ==========================================
class EchoServer(TCPServer):
    """Server that echoes back whatever client sends"""

    def handle_client(self, client_socket, address):
        try:
            client_socket.send(b"Echo Server Ready! Type 'bye' to quit.\n")

            while True:
                data = client_socket.recv(1024)
                if not data or data.decode().strip().lower() == 'bye':
                    break

                # Echo back with prefix
                response = b"ECHO: " + data
                client_socket.send(response)

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            client_socket.close()
            print(f"👋 {address} left Echo Server")


# ==========================================
# EXAMPLE 2: Uppercase Server
# ==========================================
class UppercaseServer(TCPServer):
    """Server that converts messages to UPPERCASE"""

    def handle_client(self, client_socket, address):
        try:
            client_socket.send(b"Uppercase Server! Send text, get UPPERCASE back!\n")

            while True:
                data = client_socket.recv(1024).decode().strip()
                if not data or data.lower() == 'bye':
                    break

                # Convert to uppercase
                uppercase = data.upper()
                client_socket.send(uppercase.encode() + b"\n")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            client_socket.close()
            print(f"👋 {address} left Uppercase Server")


# ==========================================
# EXAMPLE 3: Daytime Server (OOP Version)
# ==========================================
class DaytimeServer(TCPServer):
    """OOP implementation of RFC 867 Daytime Protocol"""

    def handle_client(self, client_socket, address):
        try:
            # Get current time
            current_time = datetime.now().strftime("%A, %d-%b-%Y %H:%M:%S")

            # Send time and close (RFC 867 behavior)
            client_socket.send(current_time.encode())
            print(f"⏰ Sent time to {address}: {current_time}")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            client_socket.close()
            print(f"👋 {address} got the time")


# ==========================================
# EXAMPLE 4: Calculator Server
# ==========================================
class CalculatorServer(TCPServer):
    """Server that performs calculations"""

    def handle_client(self, client_socket, address):
        try:
            welcome = (
                b"Calculator Server!\n"
                b"Send: number operator number (e.g., 5 + 3)\n"
                b"Operators: + - * /\n"
            )
            client_socket.send(welcome)

            while True:
                data = client_socket.recv(1024).decode().strip()
                if not data or data.lower() == 'bye':
                    break

                try:
                    # Parse input: "5 + 3"
                    parts = data.split()
                    if len(parts) == 3:
                        num1 = float(parts[0])
                        operator = parts[1]
                        num2 = float(parts[2])

                        # Calculate
                        if operator == '+':
                            result = num1 + num2
                        elif operator == '-':
                            result = num1 - num2
                        elif operator == '*':
                            result = num1 * num2
                        elif operator == '/':
                            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
                        else:
                            result = "Error: Unknown operator"

                        response = f"Result: {result}\n"
                    else:
                        response = "Error: Format is: number operator number\n"

                    client_socket.send(response.encode())

                except ValueError:
                    client_socket.send(b"Error: Invalid number\n")
                except Exception as e:
                    client_socket.send(f"Error: {e}\n".encode())

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            client_socket.close()
            print(f"👋 {address} left Calculator Server")


# ==========================================
# MAIN - Choose which server to run
# ==========================================
if __name__ == "__main__":
    print("=== OOP Server Examples ===\n")
    print("Choose a server to run:")
    print("1. Echo Server")
    print("2. Uppercase Server")
    print("3. Daytime Server")
    print("4. Calculator Server")

    choice = input("\nEnter choice (1-4): ")

    if choice == '1':
        server = EchoServer(port=9001)
    elif choice == '2':
        server = UppercaseServer(port=9002)
    elif choice == '3':
        server = DaytimeServer(port=9013)
    elif choice == '4':
        server = CalculatorServer(port=9004)
    else:
        print("Invalid choice!")
        exit()

    server.start()
