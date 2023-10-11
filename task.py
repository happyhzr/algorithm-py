import random


class Task:
    def __init__(self, time: int):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self) -> int:
        return self.timestamp

    def get_pages(self) -> int:
        return self.pages

    def wait_time(self, current_time: int) -> int:
        return current_time - self.timestamp
