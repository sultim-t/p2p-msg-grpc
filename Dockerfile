FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org grpcio grpcio-tools
RUN python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. p2p-msg.proto
ENTRYPOINT ["python3.7", "peer.py"]
