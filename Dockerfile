FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# FROM python:3.11

# WORKDIR /app

# RUN python -m pip install --upgrade pip

# # optimizing the docker caching behaviour
# COPY requirements.txt .
# RUN python -m pip install --no-cache-dir -r requirements.txt
# COPY . .

# RUN python manage.py collectstatic --noinput

# CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
