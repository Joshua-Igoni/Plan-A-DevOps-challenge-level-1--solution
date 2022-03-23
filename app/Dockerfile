FROM python:3.10

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY ./ /app/

# Install packages from requirements.txt

RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose container port
EXPOSE 5000

CMD [ "python3", "devops.py" ]