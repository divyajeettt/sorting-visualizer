import tkinter as tk
import tkinter.messagebox as msg


def start(var: tk.IntVar) -> None:
    global algo

    algo = var.get()
    root.destroy()


def main() -> None:
    global root

    root = tk.Tk()
    root.title("Welcome to Sorting Visualizer")

    tk.Label(
        text="Please select one of the following \nsorting algorithms:",
        font=("consolas", 12, "bold")
    ).pack()

    var = tk.IntVar(root, 0)
    values = {
        "Bitonic Sort": 0,
        "Bubble Sort": 1,
        "Cocktail Shaker Sort": 2,
        "Cycle Sort": 3,
        "Double Selection Sort": 4,
        "Heap Sort": 5,
        "Insertion Sort": 6,
        "Merge Sort": 7,
        "Odd Even Sort": 8,
        "Quick Sort": 9,
        "Reverse Selection Sort": 10,
        "Selection Sort": 11,
        "Tim Sort": 12,
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

    root.bind("<Return>", (lambda evt: start(var)))
    root.mainloop()


if __name__ == "__main__":
    main()
    print(algo)