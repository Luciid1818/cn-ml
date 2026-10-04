import socket
import pickle
HOST ="127.0.0.1"
PORT=5000
n=int(input("enter the order of the matrix"))
matrix=[]
print("\n enter the elemnets row by row:")
for i in range(n):
    row=list(map(int,input(f"enter row{i+1}:").split()))
    while len(row)!=n:
        print("enter exact n elements")
        row=list(map(int,input(f"enter row{i+1}").split()))
    matrix.append(row)
print("enterd matrix")
for row in matrix:
    print(row)
client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
client.send(pickle.dumps(matrix))
result = client.recv(1024).decode()
print("\n matrix type:",result)
client.close()
