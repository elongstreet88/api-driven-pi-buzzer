# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:3.8-alpine

RUN set -ex && \
    apk add --no-cache git gcc musl-dev

RUN git clone https://github.com/elongstreet88/Adafruit_Python_DHT
RUN cd Adafruit_Python_DHT/; python3 setup.py install --force-pi

# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
COPY api.py /

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
CMD [ "python", "./api.py" ]