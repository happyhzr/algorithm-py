from time import sleep


def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str) -> None:
    if height < 1:
        return
    move_tower(height - 1, from_pole, with_pole, to_pole)
    move_disk(from_pole, to_pole)
    move_tower(height - 1, with_pole, to_pole, from_pole)
    sleep(1)


def move_disk(from_pole: str, to_pole: str):
    print(f"moving disk from {from_pole} to {to_pole}")


if __name__ == "__main__":
    move_tower(10, "from", "to", "with")
