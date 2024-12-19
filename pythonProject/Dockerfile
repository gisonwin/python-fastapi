#FROM python:3.10.11
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
MAINTAINER gisonwin@qq.com
RUN mkdir -p /code
COPY requirements.txt /code/requirements.txt
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./history-query /code/history-query
WORKDIR /code/history-query
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8858"]