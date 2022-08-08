FROM python:3.7
RUN mkdir /app_mysql_python_tools

ADD . /app_mysql_python_tools
WORKDIR /app_mysql_python_tools

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "./DumpAndTranslateConf.py"]