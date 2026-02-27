import tkinter as tk


def update_color():
    color = entry.get().strip().upper()
    if not color.startswith('#'):
        color = '#' + color

    if len(color) == 7:
        try:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            comp_color = f"#{0xFF - r:02X}{0xFF - g:02X}{0xFF - b:02X}"

            color1.config(bg=color, text=color)
            color2.config(bg=comp_color, text=comp_color)
        except:
            pass


root = tk.Tk()

tk.Label(root, text="Введите HEX цвет:").pack(pady=10)
entry = tk.Entry(root, justify='center')
entry.pack(pady=5)
entry.bind('<KeyRelease>', lambda e: update_color())

colors_frame = tk.Frame(root)
colors_frame.pack(pady=20)

color1 = tk.Label(colors_frame, width=12, height=4, relief='solid')
color1.pack(side=tk.LEFT, padx=10)

color2 = tk.Label(colors_frame, width=12, height=4, relief='solid')
color2.pack(side=tk.RIGHT, padx=10)

root.mainloop()