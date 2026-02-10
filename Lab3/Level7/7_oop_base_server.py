# OOP-Based Server (Base Class)
# This is a reusable server class that you can extend

import socket
import threading

class TCPServer:
    """
    Base TCP Server Class
    Students can inherit from this to create custom servers easily!
    """

    def __init__(self, host='127.0.0.1', port=5000):
        """Initialize the server with host and port"""
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        print(f"🔧 Server initialized on {host}:{port}")

    def start(self):
        """Start the server and begin accepting clients"""
        try:
            # Bind and listen
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True

            print(f"✅ Server started on {self.host}:{self.port}")
            print("⏳ Waiting for clients...\n")

            # Accept clients in a loop
            self.accept_clients()

        except Exception as e:
            print(f"❌ Error starting server: {e}")

    def accept_clients(self):
        """Main loop that accepts client connections"""
        while self.running:
            try:
                # Accept new client
                client_socket, address = self.server_socket.accept()
                print(f"🎉 New client: {address}")

                # Create thread to handle this client
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket, address)
                )
                client_thread.start()

                # Show active connections
                active = threading.active_count() - 1
                print(f"📊 Active clients: {active}\n")

            except KeyboardInterrupt:
                print("\n🛑 Stopping server...")
                self.stop()
                break

    def handle_client(self, client_socket, address):
        """
        Handle one client - OVERRIDE THIS in your subclass!
        This is a simple example implementation
        """
        try:
            # Send welcome message
            client_socket.send(b"Hello from OOP Server!\n")

            # Echo loop
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                client_socket.send(b"Echo: " + data)

        except Exception as e:
            print(f"❌ Error with {address}: {e}")
        finally:
            client_socket.close()
            print(f"👋 {address} disconnected")

    def stop(self):
        """Stop the server"""
        self.running = False
        self.server_socket.close()
        print("🛑 Server stopped")


# Example usage
if __name__ == "__main__":
    # Create and start a basic server
    server = TCPServer(host='127.0.0.1', port=9000)
    server.start()
