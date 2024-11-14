# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt stopwords wordnet reuters

# Copy the two Python scripts into the container
COPY reuters_data_processing.py .
COPY text_normalization.py .

# Default command to run (you can change this to run a specific script)
CMD ["python", "reuters_data_processing.py"]
