import random

from pythonds3.basic import Queue

from printer import Printer
from task import Task


def simulation(num_seconds: int, pages_per_minutes: int) -> None:
    lab_printer = Printer(pages_per_minutes)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(f"Average Wait {average_wait} secs {print_queue.size()} tasks remaining.")


def new_print_task() -> bool:
    num = random.randrange(1, 181)
    return num == 180


if __name__ == "__main__":
    for _ in range(10):
        simulation(3600, 10)
