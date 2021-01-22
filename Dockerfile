FROM python:3.9.1-buster

WORKDIR /similarity

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy source code
COPY /similarity .

# Application launch
CMD ["python", "server.py"]