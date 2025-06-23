# 🛡️ Automated Linux System & Docker Updater

A simple, robust solution for keeping your Linux system packages and Docker images up-to-date automatically using systemd timers and Python. This tool is ideal for sysadmins and developers who want hands-off, scheduled updates with logging and error handling.

---

## ✨ Features
- Automated system package updates, upgrades, and cleanup (APT & Snap)
- Automated Docker image pulls for all local images
- Colorful, readable terminal output
- Logging of all actions and errors to a file (`auto_update.log`)
- Runs as a systemd service and timer for scheduled execution
- Easy setup with a single script

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/auto_system_updates.git
   cd auto_system_updates
   ```

2. **(Optional) Review or edit the Python script and service/timer files as needed.**

3. **Run the setup script:**
   ```sh
   chmod +x setup.sh
   ./setup.sh
   ```
   This will:
   - Copy and rename `main.py` to `/opt/auto_updates.py`
   - Copy `auto_updates.service` to `/etc/systemd/system/system-update.service`
   - Copy `auto_updates.timer` to `/etc/systemd/system/system-update.timer`
   - Reload systemd and enable/start the timer

---

## ⚙️ How It Works
- The Python script updates system packages (APT & Snap) and all Docker images.
- All actions and errors are logged to `/var/log/auto_update.log`.
- The systemd timer schedules the update job (edit the timer file to change the schedule).

---

## 🚀 Usage
- After setup, updates will run automatically as scheduled.
- To check status or logs:
  ```sh
  sudo systemctl status system-update.timer
  sudo systemctl status system-update.service
  tail -f /var/log/auto_update.log
  ```
- To run the update manually:
  ```sh
  sudo python3 /opt/auto_updates.py
  ```

---

## 📝 Customization
- Edit `/etc/systemd/system/system-update.timer` to change the schedule (see [systemd.timer documentation](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)).
- Edit `/opt/auto_updates.py` to add/remove update steps as needed.

---

## 🤝 Contributing
Pull requests and suggestions are welcome!

---

## 📄 License
MIT License. See the LICENSE file for details.
