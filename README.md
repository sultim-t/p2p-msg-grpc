# p2p-msg-grpc

## Manual run

Requires Python 3.7 and higher.

Firstly, install required packages and generate gRPC files from .proto:

```python -m pip install -r requirements.txt```

```python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. p2p-msg.proto```

The first user must launch app in server mode:

```peer.py --server <port> <username>```

Another user can connect to the server using the following command:

```peer.py <server's ip address> <port> <username>```

## Docker run

Building:

```sudo docker build --tag p2p-msg-grpc:1.0 .```

Starting server:

```sudo docker run -a stdin -a stdout -i -t p2p-msg-grpc:1.0 --server <port> <username>```

Starting client:

```sudo docker run -a stdin -a stdout -i -t p2p-msg-grpc:1.0 <server's ip address> <port> <username>```

Note: ```-a stdin -a stdout -i -t``` are required for STDIN and STDOUT, i.e. listening user input and showing messages from other peer.

## Container's IP address

To get server's ip address while using docker, firstly, we need to get a name of the server's container by listing all of them:

```docker ps```

Then, using the command below, ```IP Address``` field can be found which can be used by clients to connect to a server:

```docker inspect <container's name>```



