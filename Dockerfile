FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org grpcio grpcio-tools
ENTRYPOINT ["python3.7", "peer.py"]
