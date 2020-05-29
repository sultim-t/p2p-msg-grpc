# p2p-msg-grpc

## Manual run

Requires Python 3.7 and higher.

gRPC installation:

```python -m pip install grpcio```

```python -m pip install grpcio-tools```

The first user must launch app in server mode:

```peer.py --server <port> <username>```

Another user can connect to the server using the following command:

```peer.py <server's ip address> <port> <username>```

## Docker run

Building:

```sudo docker build --tag p2p-msg-grpc:1.0 .```

Starting server:

```sudo docker run p2p-msg-grpc:1.0 --server <port> <username>```

Starting client:

```sudo docker run p2p-msg-grpc:1.0 <server's ip address> <port> <username>```

## Container's IP address

To get server's ip address while using docker, firstly, we need to get a name of the server's container by listing all of them:

```docker ps```

Then, using the command below, ```IP Address``` field can be found which can be used by clients to connect to a server:

```docker inspect <container's name>```



