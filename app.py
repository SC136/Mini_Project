import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Text Adventure Game")
root.geometry("600x600")

# Function to update the image
def update_image(image_path):
    img = Image.open(image_path)
    img = img.resize((400, 400))  # Resize the image to fit the label
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

# Function to handle command input and update image dynamically
def process_command():
    command = command_entry.get().strip().lower()
    
    if command == "help":
        # Show available commands when the user types 'help'
        output_label.config(text="""Available Commands:
- look: Look around to describe your surroundings.
- move north: Move north towards a new location.
- move south: Move south towards a new location.
- take [item]: Take an item from the environment.
- inventory: Show your inventory of collected items.
- dance: Make your character dance.
- sing: Make your character sing a song.
- jump: Make your character jump high.
- help: Show this list of commands.
        """)
        # Hide the command entry and submit button
        command_entry.pack_forget()
        submit_button.pack_forget()
        
        # Show back button to return to normal state
        back_button.pack(pady=10)
        update_image("help_image.jpg")  # Example image when 'help' is shown

    elif command == "look":
        output_label.config(text="You look around and see a beautiful landscape.")
        update_image("landscape.jpg")  # Change to an image of the landscape
    elif command == "move north":
        output_label.config(text="You move north to a dark forest.")
        update_image("dark_forest.jpg")  # Change to an image of the dark forest
    elif command == "move south":
        output_label.config(text="You move south to a peaceful meadow.")
        update_image("peaceful_meadow.jpg")  # Change to an image of the meadow
    elif command == "take sword":
        output_label.config(text="You have taken the sword.")
        update_image("sword.jpg")  # Change to an image of the sword
    elif command == "inventory":
        output_label.config(text="Your inventory contains: sword, map.")
        update_image("inventory.jpg")  # Change to an image of the inventory
    elif command == "dance":
        output_label.config(text="Your character starts dancing joyfully!")
        update_image("dance.jpg")  # Change to an image of the character dancing
    elif command == "sing":
        output_label.config(text="Your character sings a beautiful song!")
        update_image("singing.jpg")  # Change to an image of the character singing
    elif command == "jump":
        output_label.config(text="Your character jumps high into the air!")
        update_image("jump.jpg")  # Change to an image of the character jumping
    else:
        output_label.config(text="I don't understand that command.")
        update_image("error.jpg")  # Show an error image for unrecognized commands
    
    command_entry.delete(0, tk.END)  # Clear the entry box

# Function to go back after help command
def go_back():
    output_label.config(text="You can type commands here:")
    # Show the command entry and submit button again
    command_entry.pack(padx=10, pady=20, fill="x")
    submit_button.pack(pady=10)
    # Hide the back button
    back_button.pack_forget()
    update_image("default.jpg")  # Reset image to default state

# Layout for displaying the game info
image_label = tk.Label(root)
image_label.pack(pady=20)  # Padding around the image label

output_label = tk.Label(root, text="Welcome to the game! Type 'help' for commands.", font=("Helvetica", 12), anchor="w", justify="left")
output_label.pack(padx=10, pady=10, fill="both")  # Padding and fill for the output label

command_entry = tk.Entry(root, font=("Helvetica", 14))
command_entry.pack(padx=10, pady=20, fill="x")  # Padding and fill for the command entry box

submit_button = tk.Button(root, text="Submit Command", font=("Helvetica", 12), command=process_command)
submit_button.pack(pady=10)

back_button = tk.Button(root, text="Back", font=("Helvetica", 12), command=go_back)

# Initial image display
update_image("fire_dragon.jpg")  # Display the default starting image

# Run the Tkinter event loop
root.mainloop()
