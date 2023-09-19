FROM jupyter/base-notebook
USER root
RUN conda install --yes numpy
USER fode
ENV NB_USER fode
WORKDIR /home/$fode/work
