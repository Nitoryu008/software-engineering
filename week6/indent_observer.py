from filesystem import Observer
from filesystem import Entry


class IndentObserver(Observer):
    # 木構造eの中のEntryの数を返す．
    def count_entries(self, e: Entry) -> int:
        count = 1
        for child in e.get_children():
            count += self.count_entries(child)
        return count

    def update(self, e: Entry) -> None:
        self.print_entries(0, e)

    def print_entries(self, depth: int, e: Entry) -> None:
        print("  " * depth + e.get_name())
        if len(e.get_children()) > 0:
            for c in e.get_children():
                self.print_entries(depth + 1, c)
