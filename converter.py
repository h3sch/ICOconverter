import os
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD

# ------------------------
# SETUP
# ------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = TkinterDnD.Tk()
app.title("ICO-Konverter")
app.geometry("1200x600")
app.config(bg="#2b2b2b")

selected_image = None  # global gespeichert für späteres Konvertieren


# ------------------------
# FUNKTIONEN
# ------------------------

def choose_file():
    global selected_image
    path = ctk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if path:
        bit_depth = int(bit_depth_var.get())
        selected_image = Image.open(path).convert("RGBA" if bit_depth == 32 else "RGB")
        show_preview(selected_image)
        convert_button.configure(state="normal")


def handle_drop(event):
    global selected_image
    file_path = event.data.strip('{}')
    if os.path.isfile(file_path):
        bit_depth = int(bit_depth_var.get())
        selected_image = Image.open(file_path).convert("RGBA" if bit_depth == 32 else "RGB")
        show_preview(selected_image)
        convert_button.configure(state="normal")


def show_preview(pil_image):
    img = pil_image.copy()
    img.thumbnail((160, 160), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(img)
    preview_label.configure(image=tk_image, text="")
    preview_label.image = tk_image


def convert_image():
    if not selected_image:
        ctk.CTkMessagebox(title="Fehler", message="Kein Bild ausgewählt.", icon="cancel")
        return

    selected_sizes = [size for size, var in size_vars.items() if var.get()]
    if not selected_sizes:
        ctk.CTkMessagebox(title="Achtung", message="Bitte mindestens eine Größe auswählen!", icon="warning")
        return

    output_dir = ctk.filedialog.askdirectory(title="Zielordner wählen")
    if not output_dir:
        return

    file_name = "converted_icon"  # Standardname
    base_name = file_name

    save_path = os.path.join(output_dir, f"{base_name}.ico")
    icon_sizes = [(s, s) for s in selected_sizes]
    resized_images = [selected_image.resize((s, s), Image.LANCZOS) for s in selected_sizes]

    bit_depth = int(bit_depth_var.get())

    try:
        resized_images[0].save(save_path, format='ICO', sizes=icon_sizes, bits=bit_depth)
        ctk.CTkMessagebox(title="Erfolg", message=f"Icon gespeichert:\n{save_path}", icon="check")
    except Exception as e:
        ctk.CTkMessagebox(title="Fehler", message=str(e), icon="cancel")


# ------------------------
# GUI
# ------------------------

main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

layout = ctk.CTkFrame(main_frame)
layout.pack(padx=10, pady=10, fill="both", expand=True)

# Vorschau-Container links
preview_container = ctk.CTkFrame(layout, width=180, height=180)
preview_container.pack(side="left", padx=10, pady=10)
preview_label = ctk.CTkLabel(preview_container, text="Noch kein Bild", width=160, height=160,
                              fg_color="#444444", corner_radius=8, anchor="center")
preview_label.pack(padx=10, pady=10)

# Einstellungen rechts
options_container = ctk.CTkFrame(layout)
options_container.pack(side="left", padx=20, pady=10, fill="both", expand=True)

# Titel
ctk.CTkLabel(options_container, text="ICO-Konverter", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=5)

# Größen
ctk.CTkLabel(options_container, text="Größen:").pack()
size_frame = ctk.CTkFrame(options_container)
size_frame.pack(pady=5)

sizes = [16, 32, 48, 64, 128, 256]
size_vars = {}
for s in sizes:
    var = ctk.BooleanVar(value=(s in [32, 48, 64, 128]))
    cb = ctk.CTkCheckBox(size_frame, text=f"{s}px", variable=var)
    cb.pack(side="left", padx=5)
    size_vars[s] = var

# Bit-Tiefe
ctk.CTkLabel(options_container, text="Bit-Tiefe:").pack(pady=(10, 0))
bit_depth_var = ctk.StringVar(value="32")
bit_dropdown = ctk.CTkComboBox(options_container, variable=bit_depth_var, values=["16", "32"], width=80)
bit_dropdown.pack()

# Datei auswählen
ctk.CTkButton(options_container, text="Bild auswählen", command=choose_file).pack(pady=10)

# Drag & Drop
drop_zone = ctk.CTkLabel(options_container, text="Oder Bild hierher ziehen", height=200, width=450,
                         fg_color="#333333", corner_radius=8)
drop_zone.pack(pady=5)
drop_zone.drop_target_register(DND_FILES)
drop_zone.dnd_bind('<<Drop>>', handle_drop)

# Konvertieren-Button
convert_button = ctk.CTkButton(options_container, text="Konvertieren", command=convert_image, state="disabled")
convert_button.pack(pady=10)

# ------------------------
# START
# ------------------------

app.mainloop()
