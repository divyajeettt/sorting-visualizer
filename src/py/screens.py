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
        "Bubble Sort": 0,
        "Cocktail Shaker Sort": 1,
        "Cycle Sort": 2,
        "Double Selection Sort": 3,
        "Heap Sort": 4,
        "Insertion Sort": 5,
        "Merge Sort": 6,
        "Odd Even Sort": 7,
        "Quick Sort": 8,
        "Reverse Selection Sort": 9,
        "Selection Sort": 10,
        "Tim Sort": 11,
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