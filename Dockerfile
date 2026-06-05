# 1. Start from an official, lightweight Linux image with Python 3.12 pre-installed
FROM python:3.12-slim

# 2. Set the working directory inside the container's virtual file system
WORKDIR /app

# 3. Copy just the requirements file first to take advantage of Docker's caching system
COPY requirements.txt .

# 4. Run the pip install command inside the container to install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your local application code (main.py, test_main.py, etc.) into /app
COPY . .

# 6. Expose the port that FastAPI will run on inside the container
EXPOSE 8000

# 7. The command that executes automatically when the container boots up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]