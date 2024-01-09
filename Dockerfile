# Base image
FROM python:alpine

# Working directory (current directory)
WORKDIR /app/backend



# Copy both requirements files
COPY app/requirements*.txt .

# Install dependencies from both requirements files
RUN pip install -r requirements.txt -r requirements-dev.txt

# Copy the rest of the application files
COPY app/ .


# Hint to the container runtime of ports being used
EXPOSE 8080

# Entrypoint to be executed when the container runs, can be overriden
ENTRYPOINT [ "uvicorn" ]

# Legacy usage: To be used without entrypoint
# Arguments to the entrypoint, can be overriden easily for reusability
CMD [ "main:app", "--host=0.0.0.0", "--port=8080" ]