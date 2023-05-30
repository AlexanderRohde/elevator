import usocket

# Set up UDP socket
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)

# Set up server IP address and port
server_ip = '192.168.0.100'  # Replace with the actual IP address of your UDP server
server_port = 12345  # Replace with the actual port number of your UDP server

# Bind socket to Pico's IP address and a random available port
pico_ip = '0.0.0.0'
pico_port = 54321
sock.bind((pico_ip, pico_port))

# Send UDP packet
message = 'Hello, UDP server!'
sock.sendto(message.encode(), (server_ip, server_port))
print('Sent:', message)

# Receive UDP packet
data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
received_message = data.decode()
print('Received:', received_message)

# Close the socket
sock.close()
