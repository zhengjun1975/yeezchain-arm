FROM aarch64/ubuntu:latest

RUN apt-get -y update
RUN apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
RUN apt -y install net-tools iputils-ping iproute2
RUN apt -y install python3-pip
RUN pip3 install toml --user
RUN curl -sL https://deb.nodesource.com/setup_10.x | /bin/bash
RUN apt -y install nodejs
RUN apt -y install git

COPY ./libcrypto.so.1.1 ./libssl.so.1.1 /lib/aarch64-linux-gnu/
WORKDIR /root

COPY ./yeez .
COPY ./start_chain.sh .

COPY ./rpc/ /rpc
COPY ./transaction_generator.sh .

COPY ./yeezchain-explorer /www
RUN cd /www && npm install
COPY ./start_explorer.sh .

COPY ./run.sh .
CMD [ "/bin/bash", "./run.sh" ]
