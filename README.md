# Exif Remover

This is a Python-based tool for removing EXIF data from JPEG images. It provides both a graphical user interface (GUI) and a web interface.

A simple Python GUI tool to remove EXIF metadata from images. Helps protect your privacy by stripping personal and location data from photos. You can select individual images or an entire folder, and the original images will be overwritten after cleaning.

## Features
- 🖼 Select single image or folder of images
- 🧹 Removes all EXIF metadata
- 💾 Overwrites original files with cleaned versions
- 🐍 Built with Python, Pillow, and piexif

## Installation

Ensure you have Python installed.

Install the required dependencies:

```bash
pip install pillow piexif
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

1. Clone the repository:
   ```bash
   git clone https://github.com/UniqueJackal5/exif-remover.git
   cd exif-remover
   ```

## Usage

### GUI

To run the GUI, execute the following command:

```bash
python src/main.py
```

### Web Interface

To start the web server, run:

```bash
fastapi dev src/web.py
```

Then, open your web browser and go to `http://localhost:8000`.
