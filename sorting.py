from tkinter import *
from tkinter import ttk, messagebox
import random
from algos import *

root = Tk()
root.title("Sorting Algorithms Visualiser")
root.maxsize(1000, 600)
root.config(bg='black')

# Variables
algos_used = ['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Heap Sort', 'Insertion Sort', 'Selection Sort']
selected_alg = StringVar()
data = []


def draw_data(data, colour_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 6.5
    spacing = 0
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        # Top Right
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour_array[i])
    root.update_idletasks()


def generate():
    global data
    min_val = 0
    max_val = 0
    size = 0
    try:
        min_val = int(minEntry.get())
    except ValueError:
        messagebox.showerror("Error", "Please Enter Positive Integer As Min Value")
    try:
        max_val = int(maxEntry.get())
    except ValueError:
        messagebox.showerror("Error", "Please Enter Positive Integer As Max Value")
    try:
        size = int(sizeEntry.get())
    except ValueError:
        messagebox.showerror("Error", "Please Enter Positive Integer As Size")

    if min_val < 0:
        messagebox.showerror("Error", "Please Enter Positive Integer As Min Value")
        raise ValueError
    if min_val > max_val:
        messagebox.showerror("Error", "Please Enter Min Value Lower Than Max Value")
        raise ValueError
    if size < 3:
        messagebox.showerror("Error", "Insufficient Size Value. Minimum: 3.")
        raise ValueError
    if size > 250:
        messagebox.showerror("Error", "Size Value Too High. Maximum: 250.")
        raise ValueError
    data = []
    for _ in range(size):
        data.append(random.randrange(min_val, max_val + 1))
    draw_data(data, ['cyan' for x in range(len(data))])


def start_algorithm():
    global data
    time_tick = speedScale.get() / 100
    if not data: return
    if selected_alg.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_data, time_tick)
    elif selected_alg.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, time_tick)
    elif selected_alg.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, draw_data, time_tick)
    elif selected_alg.get() == 'Heap Sort':
        heapsort(data, draw_data, time_tick)
    elif selected_alg.get() == 'Insertion Sort':
        insertionsort(data, draw_data, time_tick)
    else:
        selectionsort(data, draw_data, time_tick)
    draw_data(data, ['green2' for x in range(len(data))])


# UI Frame
UI_frame = Frame(root, width=600, height=200, bg='gray10')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(master=root, width=600, height=380, bg='gray15')
canvas.grid(row=1, column=0, padx=10, pady=2.5)


# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm", bg='gray10', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=algos_used)
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Label(UI_frame, text="Data Size", bg='gray10', fg='white').grid(row=0, column=2, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
sizeEntry.insert(0, "50")

# Row [1]
Label(UI_frame, text="Speed (ms)", bg='gray10', fg='white').grid(row=1, column=0, padx=5, pady=5, sticky=W)
speedScale = Scale(UI_frame, from_=0, to=10, length=140, resolution=0.1, orient=HORIZONTAL)
speedScale.grid(row=1, column=1, padx=5, pady=5)
speedScale.set(5)

Label(UI_frame, text="Min Value", bg='gray10', fg='white').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
minEntry.insert(0, "1")

# Row [2]
Label(UI_frame, text="Max Value", bg='gray10', fg='white').grid(row=2, column=2, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
maxEntry.insert(0, "100")

Button(UI_frame, text="Generate Data", command=generate, bg='gray15', fg='white').grid(row=2, column=0, padx=5, pady=5, sticky=W + E)
Button(UI_frame, text="Start Visualisation", command=start_algorithm, bg='gray15', fg='white').grid(row=2, column=1, padx=5, pady=5, sticky=W + E)


root.mainloop()
