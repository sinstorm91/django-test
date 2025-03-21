# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install uv (Fast Package Installer)
RUN pip install --upgrade pip && pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies using uv (much faster than pip)
RUN uv pip install --system -r requirements.txt

# Expose necessary ports
EXPOSE 8000

# Start the application with debugging enabled
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
