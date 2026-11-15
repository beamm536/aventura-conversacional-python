FROM python:3.13-slim

# instalamos las librerias tkinter y pygame
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# instalar pygame
RUN pip install --no-cache-dir pygame

COPY . .

CMD [ "tail", "-f", "/dev/null" ]