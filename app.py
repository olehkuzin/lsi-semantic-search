import os
import subprocess
import time

# Change working directory to "backend" before running server.py
os.chdir("backend")

FLASK_SERVER_PATH = "server.py"
FRONTEND_COMMAND = ["npm", "start"]
FRONTEND_DIR = "../frontend"  # Adjusted path since we're inside "backend" now

def run_flask():
    """Starts the Flask server."""
    print("🚀 Starting Flask server...")
    return subprocess.Popen(["python", FLASK_SERVER_PATH])

def run_frontend():
    """Starts the React frontend."""
    print("🌍 Starting React frontend...")
    return subprocess.Popen(FRONTEND_COMMAND, cwd=FRONTEND_DIR)

if __name__ == "__main__":
    flask_process = run_flask()
    time.sleep(3)
    frontend_process = run_frontend()

    try:
        flask_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n⏹ Stopping servers...")
        flask_process.terminate()
        frontend_process.terminate()
