# Knock-Knock Joke Server
# This server tells jokes following a specific protocol (conversation rules)

import socket
import random

# List of jokes (you can add more!)
jokes = [
    ("Lettuce", "Lettuce in, it's cold out here!"),
    ("Boo", "Don't cry, it's just a joke!"),
    ("Tank", "You're welcome!"),
    ("Orange", "Orange you glad I didn't say banana?"),
    ("Nobel", "Nobel, that's why I knocked!")
]

# Create and setup server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5001))
server_socket.listen(1)
print("🎭 Knock-Knock Joke Server is ready!")
print("📍 Listening on port 5001...")

while True:
    # Accept client connection
    client_socket, address = server_socket.accept()
    print(f"
🎉 Client connected from {address}")

    # Pick a random joke
    joke_name, punchline = random.choice(jokes)
    print(f"🎲 Selected joke: {joke_name}")

    # STATE 0: Start the joke
    client_socket.send("Knock! Knock!".encode())
    print("📤 Server: Knock! Knock!")

    # Wait for "Who's there?"
    response = client_socket.recv(1024).decode().strip()
    print(f"📥 Client: {response}")

    # STATE 1: Send the name
    if "who" in response.lower():
        client_socket.send(joke_name.encode())
        print(f"📤 Server: {joke_name}")

        # Wait for "[name] who?"
        response = client_socket.recv(1024).decode().strip()
        print(f"📥 Client: {response}")

        # STATE 2: Send the punchline
        if "who" in response.lower():
            client_socket.send(punchline.encode())
            print(f"📤 Server: {punchline}")
            print("✅ Joke complete!")

    # Close this client connection
    client_socket.close()
    print("👋 Client disconnected\n")
    print("⏳ Waiting for next client...")
