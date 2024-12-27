# **Simple Flask Redis App**

This is a simple Flask application that uses Redis as a backend to count the number of visits to the homepage. Follow the steps below to install and run the project.

---

## **Prerequisites**
Before running the project, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- Redis

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/adzinzhalifunnas/simple-flask-redis-app.git
cd simple-flask-redis-app
```

### **2. Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Python Dependencies**
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **4. Install Redis**
1. Install Redis using Homebrew:
```bash
brew install redis
```

2. Start Redis as a background service:
```bash
brew services start redis
```

3. Verify Redis is running:
```bash
redis-cli ping
```

If it responds with `PONG`, Redis is running successfully.

---

## **Running the Project**

1. Ensure Redis is running on your machine (by following the installation steps above).
2. Start the Flask application:
```bash
python app.py
```
3. Open your browser and navigate to `http://localhost:8080`. You should see a message displaying how many times the page has been visited.

---
