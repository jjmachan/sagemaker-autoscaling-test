import random
from time import time

import cv2
import numpy as np

from bentoml import env, api, BentoService
from bentoml.adapters import ImageInput


@env(
    pip_packages=["opencv-python", "imageio"],
    docker_base_image="bentoml/model-server:0.13.1-slim-py38",
    setup_sh="""\
#!/bin/bash
set -e

apt-get --allow-releaseinfo-change update
apt-get -y install libgl1 libglib2.0-0 libsm6 libxrender1 libxext6
pip install -U pip --no-cache-dir
apt-get -y clean
  """,
)
class OpenCVBlur(BentoService):
    @api(input=ImageInput())
    def predict(self, image: np.ndarray):
        times = []
        m = random.randint(10, 100)
        for _ in range(m):
            t0 = time()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
            image = cv2.GaussianBlur(image, (3, 3), 0)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            noise = np.random.randint(0, 255, size=image.shape, dtype=image.dtype)
            image = cv2.addWeighted(image, 0.95, noise, 0.05, 0)
            times.append(time() - t0)
        total_time = sum(times)
        return dict(
            _count=m,
            _total=total_time,
            _avg=total_time / len(times),
            times=times,
        )


if __name__ == "__main__":
    # from time import sleep

    svc = OpenCVBlur()
    svc.save()
    # svc.start_dev_server()
    # while True:
    #     sleep(1)
