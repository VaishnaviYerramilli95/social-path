# Local Setup & Installation Guide

Follow these steps to deploy and execute **SocialPilot** on your machine.

---

## 🛠️ Prerequisites

Ensure you have the following installed:
1. **Node.js** (v18+)
2. **Python** (v3.10+) with `pip`
3. **PowerShell** (For Windows automated scripts) or standard Bash terminals.

---

## 🚀 Recommended Launch (Windows PowerShell)

Windows users can utilize a single scaffolding command to set up environments and start services:

1. Open PowerShell inside the project directory:
   ```powershell
   cd "frontend code"
   ```
2. Unblock script execution (if disabled by local Windows policies):
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
3. Run the setup script:
   ```powershell
   ./start-dev.ps1
   ```

---

## 🔧 Manual Cross-Platform Launch (macOS, Linux, CMD)

### 1. Setup Backend API
Navigate to the backend folder and prepare your Python virtual environment:
```bash
cd "frontend code/backend"

# 1. Create venv
python -m venv venv

# 2. Activate venv
# On Linux / macOS:
source venv/bin/activate
# On Windows CMD:
venv\Scripts\activate.bat

# 3. Install packages
pip install -r requirements.txt
```

Start the FastAPI application server:
```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
*Swagger API playground is now available at http://127.0.0.1:8000/docs*

### 2. Setup React Frontend
Open another terminal, navigate to the frontend folder, and install node packages:
```bash
cd "frontend code/frontend"

# 1. Install packages
npm install

# 2. Launch bundler server
npm run dev
```
*React app is now active at http://localhost:3000*
