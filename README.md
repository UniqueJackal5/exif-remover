This is a Python-based tool for removing EXIF data from JPEG images. It provides both a graphical user interface (GUI) and a web interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/exif-remover.git
   cd exif-remover
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
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