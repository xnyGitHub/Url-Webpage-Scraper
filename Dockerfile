FROM python

#Install firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox

#Set working directory
WORKDIR /app

#Set environment
ENV FLASK_APP=flask_app.py

ENV FLASK_RUN_HOST=0.0.0.0

#Copy requirments.txt
COPY requirements.txt requirements.txt

#Install the dependencies
RUN pip install -r requirements.txt

#Expose the port
EXPOSE 5000

#Copy the files in
COPY . .

#Set the commands
CMD ["flask","run"]

