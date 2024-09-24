from tkinter import Tk, Canvas


def draw_dots(a, b, coords, M=400):
    # Create the main window

    PADDING_LEFT = 20
    
    WIDTH = 1200
    
    root = Tk()
    root.geometry(f"{WIDTH+PADDING_LEFT*2}x300")

    # canvas.update_idletasks()
    a *= M
    b *= M
    coords = [c * M for c in coords]

    # Create a canvas widget
    canvas = Canvas(root, width=WIDTH+PADDING_LEFT*2, height=300)
    canvas.pack()

    print(a, b, *coords)

    canvas.update_idletasks()
    line_length = b - a
    line_y = 150  # Fixed y-coordinate for the line

    # Draw the line from (a, line_y) to (b, line_y)
    canvas.create_line(PADDING_LEFT, line_y, PADDING_LEFT + WIDTH, line_y, fill="black", width=2)
    
    normalized_x = PADDING_LEFT + (a - a) * (WIDTH / line_length)
    canvas.create_oval(normalized_x - 5, line_y - 5, normalized_x + 5, line_y + 5, fill="blue")
    normalized_x = PADDING_LEFT + (b - a) * (WIDTH / line_length)
    canvas.create_oval(normalized_x - 5, line_y - 5, normalized_x + 5, line_y + 5, fill="red")

    for index, x in enumerate(coords):
        # Normalize x to fit within the range [a, b]
        normalized_x = PADDING_LEFT + (x - a) * (WIDTH / line_length)

        canvas.create_oval(normalized_x - 5, line_y + 5, normalized_x + 5, line_y + 15, fill="green")

        # Add text label with index of coordinate
        canvas.create_text(normalized_x, line_y + 25,
                           text=str(index + 1), font=("Arial", 10))

    # Run the application
    root.mainloop()
