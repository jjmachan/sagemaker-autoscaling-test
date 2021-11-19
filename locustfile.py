import io
import random
import numpy as np
from PIL import Image
from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    wait_time = between(5, 20)

    def on_start(self):
        w, h = random.randint(500, 1500), random.randint(500, 1500)
        image = np.random.randint(
            0,
            255,
            (h, w, 3),
            dtype="uint8",
        )
        data = io.BytesIO()
        Image.fromarray(image).save(data, format="JPEG")
        self.data = data.getvalue()

        self.client.headers["Content-Type"] = "image/jpeg"
        self.client.headers["Content-Length"] = str(len(self.data))

        print(f"Image size: {w}x{h}, {len(self.data)} bytes!")

    @task
    def predict(self):
        self.client.post(
            "/predict",
            data=self.data,
        )
