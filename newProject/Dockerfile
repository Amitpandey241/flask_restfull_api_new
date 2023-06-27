FROM python:3.9-slim
#RUN mkdir /app/
WORKDIR /app
#COPY newProject/requirements.txt /app
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=views.py
CMD ["flask", "run", "--host=0.0.0.0"]
