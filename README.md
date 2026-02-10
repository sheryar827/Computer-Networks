# Lab 3: Network Programming in Python
## BS Computer Science - Semester 4

Welcome! This lab covers client-server programming using Python sockets.

---

## 📚 What's Included

### Part 1: Basic TCP (Simple)
- `1_simple_server.py` - Basic TCP server (one client)
- `1_simple_client.py` - Basic TCP client

### Part 2: Protocol Example (Knock-Knock Joke)
- `2_knockknock_server.py` - Implements knock-knock joke protocol
- `2_knockknock_client.py` - Client that follows the protocol

### Part 3: UDP Multi-Client
- `3_udp_server.py` - UDP server (handles multiple clients naturally)
- `3_udp_client.py` - UDP client

### Part 4: TCP Multi-Client (Threading)
- `4_tcp_multiserver.py` - TCP server using threads for multiple clients
- `4_tcp_multiclient.py` - TCP client (run multiple copies!)

### Part 5: File Transfer
- `5_file_server.py` - Sends files to clients
- `5_file_client.py` - Downloads files from server

### Part 6: Daytime Server (Assignment)
- `6_daytime_server.py` - RFC 867 implementation
- `6_daytime_client.py` - Daytime client

### Part 7: OOP Approach
- `7_oop_base_server.py` - Reusable server base class
- `7_oop_custom_servers.py` - Examples (Echo, Uppercase, Daytime, Calculator)

---

## 🚀 How to Run

### Step 1: Open Two Terminal Windows
- Terminal 1: For SERVER
- Terminal 2: For CLIENT

### Step 2: Run Server First
```bash
python 1_simple_server.py
```

### Step 3: Run Client
```bash
python 1_simple_client.py
```

---

## 💡 Important Tips

1. **Always run SERVER before CLIENT**
   - Server must be listening before client tries to connect

2. **Port numbers must match**
   - If server uses port 5000, client must connect to port 5000

3. **One server can serve multiple clients** (if using threading or UDP)

4. **To stop a server**: Press `Ctrl+C`

5. **If you get "Address already in use" error**:
   - Wait 30 seconds, or
   - Change the port number, or
   - Kill the process: `lsof -ti:5000 | xargs kill` (Mac/Linux)

---

## 📝 Testing Guide

### Test 1: Simple TCP (Warmup)
```bash
# Terminal 1:
python 1_simple_server.py

# Terminal 2:
python 1_simple_client.py
```
✅ Expected: Client receives welcome message

---

### Test 2: Knock-Knock Joke
```bash
# Terminal 1:
python 2_knockknock_server.py

# Terminal 2:
python 2_knockknock_client.py
# Run multiple times to see different jokes!
```
✅ Expected: Complete knock-knock joke exchange

---

### Test 3: UDP Multi-Client
```bash
# Terminal 1:
python 3_udp_server.py

# Terminal 2:
python 3_udp_client.py

# Terminal 3 (open another!):
python 3_udp_client.py

# Terminal 4 (one more!):
python 3_udp_client.py
```
✅ Expected: All clients can send messages simultaneously!

---

### Test 4: TCP Multi-Client with Threading
```bash
# Terminal 1:
python 4_tcp_multiserver.py

# Open 3 more terminals and run:
python 4_tcp_multiclient.py
```
✅ Expected: All clients connected at once, each can chat

---

### Test 5: File Transfer
```bash
# Terminal 1:
python 5_file_server.py
# Server creates sample.txt automatically

# Terminal 2:
python 5_file_client.py
# When prompted, type: sample.txt
```
✅ Expected: File downloaded as "downloaded_sample.txt"

---

### Test 6: Daytime Server (Assignment)
```bash
# Terminal 1:
python 6_daytime_server.py

# Terminal 2:
python 6_daytime_client.py
```
✅ Expected: Client receives current date/time

---

### Test 7: OOP Servers
```bash
# Terminal 1:
python 7_oop_custom_servers.py
# Choose server type (1-4)

# Terminal 2:
# Use telnet to test:
telnet 127.0.0.1 9001
# Or use appropriate client
```

---

## 🎯 Assignment Requirements

### Required Implementations:
1. ✅ Knock-Knock Joke Server & Client
2. ✅ UDP Multi-Client Communication
3. ✅ TCP Multi-Client with Threading
4. ✅ TCP File Server
5. ✅ Daytime Server (Functional version)
6. ✅ Daytime Server (OOP version)

### Submission Format:
- All `.py` files
- Screenshots of running programs
- Short documentation explaining each part

---

## 🐛 Common Errors & Solutions

### Error: "Connection refused"
**Problem**: Server is not running
**Solution**: Start server first!

### Error: "Address already in use"
**Problem**: Port is busy
**Solution**: Wait 30 seconds or use different port

### Error: "No module named 'socket'"
**Problem**: Python not installed properly
**Solution**: Reinstall Python

### Server hangs after one client
**Problem**: Not using threading
**Solution**: Use the multi-client versions (4_tcp_multiserver.py)

---

## 📖 Concepts Explained

### TCP vs UDP
- **TCP**: Like phone call (reliable, ordered, connection-based)
- **UDP**: Like postcard (fast, connectionless, no guarantee)

### Threading
- Allows one program to do multiple things at once
- Each client gets own thread = can serve many clients

### Protocol
- Set of rules both sides follow
- Example: Knock-knock joke has specific steps

### Socket
- Endpoint for network communication
- Like a phone socket you plug into

---

## 🎓 Learning Path

1. **Level 1**: Understand basic TCP (files 1_*)
2. **Level 2**: Learn protocols (files 2_*)
3. **Level 3**: Master UDP (files 3_*)
4. **Level 4**: Threading & multi-client (files 4_*)
5. **Level 5**: File transfer (files 5_*)
6. **Assignment**: Daytime server (files 6_*)
7. **Advanced**: OOP approach (files 7_*)

---

## 📞 Need Help?

- Read the comments in each file
- Try the simple examples first
- Test locally before testing on network
- Google the error message
- Ask your instructor

---

## 🌟 Bonus Challenges

1. Create a chat room server (broadcast messages to all clients)
2. Add username/password authentication
3. Implement a simple HTTP server
4. Create a multiplayer game server
5. Build a file sharing system

---

Good luck with your lab! Remember: start simple, test often, and don't give up! 💪

---

**Course**: Computer Networks Lab
**Institution**: Air University Islamabad
**Semester**: 4 (BS Computer Science)
