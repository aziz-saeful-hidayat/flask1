FROM python:2.7-alpine
MAINTAINER Muhamad Fahrur <Rasyid mfahrurashyid@gmail.com>

ENV INSTALL_PATH /web_app
RUN mkkdir -p $INSTALL_PATH

WORKDIR  $INSTALL_PATH
