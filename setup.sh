#!/bin/bash
# Setup script for auto system updates and docker image updates
# Copies service, timer, and main script to appropriate locations and enables the timer

set -e

# Copy and rename main.py to /opt/auto_updates.py
sudo cp main.py /opt/auto_updates.py
sudo chmod 755 /opt/auto_updates.py

# Copy service file to systemd location
sudo cp auto_updates.service /etc/systemd/system/auto-update.service
sudo chmod 644 /etc/systemd/system/auto-update.service

# Copy timer file to systemd location
sudo cp auto_updates.timer /etc/systemd/system/auto-update.timer
sudo chmod 644 /etc/systemd/system/auto-update.timer

# Reload systemd, enable and start the timer
sudo systemctl daemon-reload
sudo systemctl enable auto-update.timer
sudo systemctl start auto-update.timer

echo "Setup complete. Auto update timer is enabled and started."
