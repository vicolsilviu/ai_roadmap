# import time
# import socket
# from sklearn.datasets import load_iris

# data=load_iris()
# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(("0.0.0.0",9999))
# server.listen()

# while True:
#     client,addr=server.accept()
#     print("Connection from",addr)
#     client.send("You are connected!\n".encode())
#     client.send(f"{data['data'][:,0]}\n".encode())
#     time.sleep(2)
#     client.send("You are being deisconnected!\n".encode())
#     client.close()
# # print("Hello, World!")

def return_sum(a,b):
    sum=a+b
    return sum
print(return_sum(1,2))
print(return_sum(2,3))
print(return_sum(3,4))
print(return_sum(4,5))
print(return_sum(5,6))
print(return_sum(6,7))



