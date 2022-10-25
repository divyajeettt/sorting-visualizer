import tkinter as tk
import tkinter.messagebox as msg


def start(var: tk.IntVar) -> None:
    global algo

    algo = var.get()
    root.destroy()


def ending(text: str) -> int:
    temp = tk.Tk()
    temp.withdraw()

    return msg.askyesno(
        title="Array Sorted", message=f"Do you want to simulate the sorting again?",
        parent=temp
    )


def main() -> None:
    global root

    root = tk.Tk()
    root.title("Welcome to Sorting-Visualizer")

    tk.Label(
        text="Please select one of the following \nsorting algorithms:",
        font=("consolas", 12, "bold")
    ).pack()

    var = tk.IntVar(root, 1)
    values = {
        "Bubble Sort": 1,
        "Double Selection Sort": 2,
        "Heap Sort": 3,
        "Insertion Sort": 4,
        "Merge Sort": 5,
        "Quick Sort": 6,
        "Reverse Selection Sort": 7,
        "Selection Sort": 8,
    }

    for (text, value) in values.items():
        tk.Radiobutton(
            root, text=text.ljust(25), variable=var, value=value, indicator=0,
            background="light gray", font=("consolas", 12, "bold")
        ).pack(fill=tk.X)

    tk.Button(
        root, text="START!", width=45, bd=3, command=(lambda: start(var)),
        font=("consolas", 12, "bold")
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
    print(algo)