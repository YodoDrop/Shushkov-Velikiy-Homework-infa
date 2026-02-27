import tkinter as tk


def calculate():
    try:
        w = float(weight.get())
        h = float(height.get()) / 100
        bmi = w / (h * h)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            text = "анорексичка"
        elif bmi < 25:
            text = "нормис"
        elif bmi < 30:
            text = "толстый нормис"
        elif bmi < 35:
            text = "перебор 1 степени"
        elif bmi < 40:
            text = "перебор 2 степени"
        else:
            text = "фемка"

        result.config(text=f"ИМТ: {bmi} - {text}")
    except:
        result.config(text="ты чо")


root = tk.Tk()
root.title("ИМТ кулькулятор")

tk.Label(root, text="Вес (кг):").pack()
weight = tk.Entry(root)
weight.pack()

tk.Label(root, text="Рост (см):").pack()
height = tk.Entry(root)
height.pack()

tk.Button(root, text="попробуй", command=calculate).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()