FROM python:3

ADD index.py /

RUN pip install telepot

CMD [ "python", "./index.py" ]