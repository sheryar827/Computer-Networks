# 🚀 Quick Start Guide - Lab 3
## For BS CS Semester 4 Students

---

## ⚡ Fastest Way to Get Started

### 1. Download all files to one folder

### 2. Open TWO terminals/command prompts in that folder

### 3. Try the simplest example first:

**Terminal 1 (Server):**
```bash
python 1_simple_server.py
```

**Terminal 2 (Client):**
```bash
python 1_simple_client.py
```

That's it! You just did network programming! 🎉

---

## 📊 What Each File Does (Simple Version)

| File | What it Does | Difficulty |
|------|-------------|------------|
| `1_simple_server.py` | Accepts 1 client, sends hello | ⭐ Easy |
| `1_simple_client.py` | Connects and receives message | ⭐ Easy |
| `2_knockknock_server.py` | Tells jokes using protocol | ⭐⭐ Medium |
| `2_knockknock_client.py` | Receives jokes | ⭐⭐ Medium |
| `3_udp_server.py` | Handles many clients (UDP) | ⭐⭐ Medium |
| `3_udp_client.py` | Sends messages via UDP | ⭐⭐ Medium |
| `4_tcp_multiserver.py` | Handles many clients (TCP+threads) | ⭐⭐⭐ Hard |
| `4_tcp_multiclient.py` | Chat client | ⭐⭐ Medium |
| `5_file_server.py` | Sends files to clients | ⭐⭐⭐ Hard |
| `5_file_client.py` | Downloads files | ⭐⭐ Medium |
| `6_daytime_server.py` | **ASSIGNMENT** - Sends time | ⭐⭐ Medium |
| `6_daytime_client.py` | Gets time from server | ⭐ Easy |
| `7_oop_base_server.py` | Reusable server class | ⭐⭐⭐ Hard |
| `7_oop_custom_servers.py` | 4 server examples using OOP | ⭐⭐⭐ Hard |

---

## 🎯 Assignment Checklist

### Required Programs to Submit:

- [ ] **Knock-Knock Server & Client** (Files: 2_knockknock_*.py)
  - Show multiple jokes working
  - Screenshot of conversation

- [ ] **UDP Multi-Client** (Files: 3_udp_*.py)
  - Screenshot showing 3 clients connected
  - All sending messages simultaneously

- [ ] **TCP Multi-Client** (Files: 4_tcp_*.py)
  - Screenshot showing multiple clients
  - Show thread count increasing

- [ ] **File Server** (Files: 5_file_*.py)
  - Transfer a text file successfully
  - Show file before & after transfer

- [ ] **Daytime Server** (Files: 6_daytime_*.py) ⭐ MAIN ASSIGNMENT
  - Functional version (basic)
  - OOP version (bonus marks!)
  - Screenshot showing time received

---

## 💻 How to Test Each Part

### Test 1: Simple TCP
```bash
# Start server:
python 1_simple_server.py

# In another terminal, start client:
python 1_simple_client.py

# Expected output:
Client: "Server says: Welcome to my first TCP server! 🚀"
```

---

### Test 2: Knock-Knock Jokes
```bash
# Start server:
python 2_knockknock_server.py

# Run client multiple times to get different jokes:
python 2_knockknock_client.py
python 2_knockknock_client.py
python 2_knockknock_client.py
```

---

### Test 3: UDP (Multiple Clients!)
```bash
# Start server ONCE:
python 3_udp_server.py

# Open 3+ terminals and run client in each:
# Terminal 2:
python 3_udp_client.py

# Terminal 3:
python 3_udp_client.py

# Terminal 4:
python 3_udp_client.py

# All clients can send at the same time!
```

---

### Test 4: TCP Multi-Client (Threading)
```bash
# Start server:
python 4_tcp_multiserver.py

# Open multiple terminals and connect:
python 4_tcp_multiclient.py  # Terminal 2
python 4_tcp_multiclient.py  # Terminal 3
python 4_tcp_multiclient.py  # Terminal 4

# Watch server show: "Active clients: 3"
```

---

### Test 5: File Transfer
```bash
# Server automatically creates sample.txt
python 5_file_server.py

# In another terminal:
python 5_file_client.py
# When asked, type: sample.txt

# Check folder for: downloaded_sample.txt
```

---

### Test 6: Daytime Server (YOUR ASSIGNMENT!)
```bash
# Start daytime server:
python 6_daytime_server.py

# Connect and get time:
python 6_daytime_client.py

# Expected: "Tuesday, 10-Feb-2026 17:30:45"
```

---

## 🐛 Troubleshooting

### Problem: "Connection refused"
**Why**: Server not running
**Fix**: Start server first!

### Problem: "Address already in use"
**Why**: Previous server still running
**Fix**: 
- Wait 30 seconds, OR
- Press Ctrl+C on old server, OR
- Change port number (5000 → 5001)

### Problem: Can't find python command
**Try**:
```bash
python3 1_simple_server.py
```

### Problem: encode/decode errors
**Remember**:
- **Sending**: use `.encode()` → "hello".encode()
- **Receiving**: use `.decode()` → data.decode()

---

## 📝 Important Concepts (Exam Material!)

### What is a Socket?
A socket is like a telephone connection between two programs.
- One program can be on your computer
- Other can be on any computer in the world!

### TCP vs UDP?

**TCP (SOCK_STREAM)**:
- Like a phone call
- Reliable (guaranteed delivery)
- Ordered (messages arrive in order)
- Connection-based (must connect first)
- Use for: chat, file transfer, web browsing

**UDP (SOCK_DGRAM)**:
- Like sending postcards
- Fast but no guarantee
- No connection needed
- Use for: video calls, games, live streaming

### What is Threading?
- Doing multiple things at once
- Each client gets own thread
- Threads run independently

### What is a Protocol?
- Set of rules for communication
- Both sides must follow same rules
- Example: Knock-knock joke has 5 steps

---

## 🎓 Study Tips

1. **Run the programs yourself**
   - Don't just read - execute!
   - Change values and see what happens

2. **Read the comments**
   - Every file has detailed comments
   - Comments explain WHY, not just WHAT

3. **Start simple**
   - Master files 1_* before moving to 7_*
   - Build confidence gradually

4. **Break when stuck**
   - Take a break, come back fresh
   - Explain problem to a friend (rubber duck debugging!)

5. **Use print() statements**
   - Add prints to see what's happening
   - Debug by seeing values

---

## 🌟 Bonus: Testing with Telnet

You can test servers without writing a client!

```bash
# Start any server, then:
telnet 127.0.0.1 5000

# Type messages and press Enter
# Great for quick testing!
```

---

## 📱 Pakistani Context Examples

### Replace Boring Examples:
Instead of "Hello World", use:
- "Assalam-o-Alaikum from Islamabad! 🇵🇰"
- "Welcome to Air University Server!"
- "Pakistan Zindabad! 🎉"

### File Transfer Ideas:
- Transfer a Quran surah (text file)
- Share course notes
- Send assignment PDFs

---

## ✅ Before Submission

- [ ] All programs run without errors
- [ ] Code has comments explaining logic
- [ ] Screenshots show successful execution
- [ ] README file included
- [ ] Your name and registration number in files

---

## 🆘 Still Confused?

### Watch Output Carefully:
- Server prints what it receives
- Client prints what it sends
- Follow the flow!

### Compare with Examples:
- Look at working code
- See patterns
- Copy structure, then modify

### Ask Questions:
- In lab session
- On class forum
- Email instructor

---

## 🎯 Success Criteria

You know you've mastered this when you can:
1. ✅ Explain difference between TCP and UDP
2. ✅ Create a simple server from scratch
3. ✅ Handle multiple clients using threading
4. ✅ Transfer files over network
5. ✅ Implement a custom protocol
6. ✅ Use OOP for server design

---

## 🚀 After Completing Lab 3

You now understand:
- How WhatsApp works (client-server)
- How file sharing works (FTP concept)
- How websites work (HTTP basics)
- How games handle multiplayer (threading)

**You're a network programmer now! 🎓💪**

---

**Remember**: Every expert was once a beginner. Keep practicing!

---

Generated for BS Computer Science students
Air University Islamabad
