import tkinter as tk
from tkinter import ttk

class ArtworkInformation:
    def __init__(self, master):
        self.master = master
        self.master.title("Masterpiece finder")
        self.master.geometry("500x400")

        self.artworks = [
            ("The Card Players", "Paul Cezanne", "$250 million", "While there are, in total, five paintings of card players by Cézanne, the final three works were\n similar in composition and number of players (two), causing them to sometimes be grouped \ntogether as one version.[10] The exact dates of the paintings are uncertain, but it is long believed \nCézanne began with larger canvases and pared down in size with successive versions, though\n research in recent years has cast doubt on this assumption"),
            ("Nafea Faa Ipoipo", "Paul Gauguin", "$300 million"),
            ("Number 17A", "Jackson Pollock", "$200 million"),
            ("Women of Algiers", "Pablo Picasso", "$160 million"),
            ("Les Femmes d'Alger", "Pablo Picasso", "$160 million"),
            ("No. 6 (Violet, Green and Red)", "Mark Rothko", "$186 million"),
            ("No. 61 (Brown and Big Orange)", "Mark Rothko", "$186 million")
        ]

        self.selected_artwork = tk.StringVar()
        self.selected_artwork.set("Select an artwork")

        self.dropdown = ttk.Combobox(self.master, textvariable=self.selected_artwork, state="readonly")
        self.dropdown["values"] = [artwork[0] for artwork in self.artworks]
        self.dropdown.pack()

        self.title_label = tk.Label(self.master, text="Title:")
        self.title_label.pack()

        self.artist_label = tk.Label(self.master, text="Artist:")
        self.artist_label.pack()

        self.value_label = tk.Label(self.master, text="Value:")
        self.value_label.pack()
       
        self.title_display = tk.Label(self.master, text="")
        self.title_display.pack()

        self.artist_display = tk.Label(self.master, text="")
        self.artist_display.pack()

        self.value_display = tk.Label(self.master, text="")
        self.value_display.pack()

        self.dropdown.bind("<<ComboboxSelected>>", self.update_display)
        

    def update_display(self, event):
        title = self.selected_artwork.get()
        for artwork in self.artworks:
            if title == artwork[0]:
                self.title_display["text"] = artwork[0]
                self.artist_display["text"] = artwork[1]
                self.value_display["text"] = artwork[2]
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ArtworkInformation(root)
    root.mainloop()
