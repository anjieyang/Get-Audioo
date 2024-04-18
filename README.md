# Get-Audioo

## Prerequisites

### For Python Installation:

- Ensure you have Python 3.6+ installed on your system.
- Ensure `ffmpeg` is installed and accessible from the command line.

### For Docker Installation:

Althernatively, if you are using Docker, follow these steps:

1. Download the `get-audioo-deploy.yml` from [here](https://drive.google.com/uc?export=download&id=1-wvAxlbW3fxk68BvvtXsAohPYbaAzDmv).

2. Modify `YOUR_VIDEO_PATH` in the `dockerhub_deploy.yml` file to the abosolute path where your video is saved.

3. Run the Docker:

```bash
docker-compose -f get-audioo-deploy.yml up -d
```

## Running the Script

1. Clone the repository:

```bash
git clone https://github.com/anjieyang/Get-Audioo.git
cd Get-Audioo
```

2. Edit the `DIRECTORY_PATH` in `config.py` to the path you saved videos.

3. Running the script:

```bash
python3 main.py
```
