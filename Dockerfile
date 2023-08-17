FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=nointeractive

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y git wget vim

RUN apt-get install -y python3-pip
RUN apt-get install -y libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get install libmagic1

RUN pip3 install --upgrade pip
RUN pip3 install numpy
RUN pip3 install opencv-python
RUN pip3 install streamlit
RUN pip3 install matplotlib
RUN pip3 install pandas
RUN pip3 install tqdm
RUN pip3 install seaborn

RUN pip3 install langflow
RUN pip3 install langchain
RUN pip3 install webuiapi
RUN pip3 install gradio
RUN pip3 install openai
RUN pip3 install chromadb
RUN pip3 install tiktoken
RUN pip3 install unstructured
