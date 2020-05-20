# p2p-msg-grpc

gRPC installation:

```python -m pip install grpcio```
```python -m pip install grpcio-tools```

The first user must launch app in server mode:

```peer.py --server <port> <username>```

Another user can connect to the server using the following command:

```peer.py <server's ip address> <port> <username>```
