import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set timeout of 5 seconds so client does not hang if server is unreachable
client.settimeout(5.0)

print(f"Connected to Internet Slang Translator at {HOST}:{PORT}")
print("Type your message (or 'exit' / 'quit' to stop):\n")

while True:
    try:
        message = input("Enter text: ").strip()
        if not message:
            continue
        if message.lower() in ("exit", "quit"):
            print("Exiting...")
            break

        client.sendto(message.encode(), (HOST, PORT))
        data, _ = client.recvfrom(2048)
        print("Translated:", data.decode())
        print("-" * 40)
    except KeyboardInterrupt:
        print("\nSession ended.")
        break
    except socket.timeout:
        print("Error: Request timed out. Is the server running?")
    except Exception as e:
        print("Error:", e)

client.close()