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

Build:

```sudo docker build --tag p2p-msg-grpc:1.0 .```

Start server:

```sudo docker run p2p-msg-grpc:1.0 --server <port> <username>```

Start client:

```sudo docker run p2p-msg-grpc:1.0 <server's ip address> <port> <username>```


