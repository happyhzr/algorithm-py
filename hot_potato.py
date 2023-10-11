from typing import List

from pythonds3.basic import Queue


def hot_potato(name_list: List[str], num: int) -> str:
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


if __name__ == "__main__":
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
