import tkinter as tk
from hangmanPOO import Hangman


class HangmanGUI:
    def __init__(self, root, hangman):
        self.root = root
        self.hangman = hangman
        self.root.title("Juego del Ahorcado - Prototipo")
        self.root.geometry("400x350")
        self.root.attributes('-topmost', True)

        # ==========================================
        # SECCIÓN 1: Ingresar la palabra secreta
        # ==========================================
        self.frame_setup = tk.Frame(root, padx=20, pady=20)
        self.frame_setup.pack(fill="both", expand=True)

        tk.Label(self.frame_setup, text="Escribe la palabra a adivinar:", font=("Arial", 12)).pack(pady=5)
        
        self.entry_secret = tk.Entry(self.frame_setup, font=("Arial", 14), show="*", justify="center")
        self.entry_secret.pack(fill="x", pady=10)

        self.btn_start = tk.Button(self.frame_setup, text="Iniciar Juego", font=("Arial", 11), bg="green", fg="white", command=self.iniciar_juego)
        self.btn_start.pack(pady=10)

        # ==========================================
        # SECCIÓN 2: Pantalla del Juego (Oculta al inicio)
        # ==========================================
        self.frame_game = tk.Frame(root, padx=20, pady=20)

        self.lbl_word_display = tk.Label(self.frame_game, text="_ _ _ _", font=("Courier", 22, "bold"))
        self.lbl_word_display.pack(pady=10)

        self.lbl_opportunities = tk.Label(self.frame_game, text=f"Oportunidades restantes: {self.hangman.opportunities}", font=("Arial", 10), fg="gray")
        self.lbl_opportunities.pack(pady=5)

        self.character_label = tk.Label(self.frame_game, text="Ingresa una letra:", font=("Arial", 11))
        self.character_label.pack(anchor="w", pady=5)

        self.entry_letter = tk.Entry(self.frame_game, font=("Arial", 14), justify="center")
        self.entry_letter.pack(fill="x", pady=5)

        self.btn_guess = tk.Button(self.frame_game, text="Probar Letra", font=("Arial", 11), bg="blue", fg="white", command=self.probar_letra)
        self.btn_guess.pack(pady=10)

        # Botón de reiniciar (conectado a su propia función y oculto al inicio)
        self.btn_restart = tk.Button(self.frame_game, text="Reiniciar Juego", font=("Arial", 11), bg="orange", fg="white", command=self.reiniciar_juego)
        self.btn_restart.pack_forget()


    def iniciar_juego(self):
        palabra = self.entry_secret.get()
        if palabra.strip() != "":
            self.hangman.word_to_guess = palabra.strip()
            # Reiniciar oportunidades por si es una nueva partida
            self.hangman.opportunities = 3  # Ajusta según las que uses por defecto
            
            # Ocultamos la pantalla de configuración y mostramos el juego
            self.frame_setup.pack_forget()
            self.frame_game.pack(fill="both", expand=True)
            
            guiones = " ".join(["_" for _ in palabra.strip()])
            self.lbl_word_display.config(text=guiones)
            self.lbl_opportunities.config(text=f"Oportunidades restantes: {self.hangman.opportunities}")
        else:
            print("¡Debes escribir una palabra válida!")


    def probar_letra(self):
        letra = self.entry_letter.get()
        print(f"Letra ingresada: {letra}")
        
        self.entry_letter.delete(0, tk.END)
        self.hangman.replace_words(letra)

        # Actualizar elementos visuales
        guiones_con_espacios = " ".join(self.hangman.hidden_word)
        self.lbl_word_display.config(text=guiones_con_espacios)
        self.lbl_opportunities.config(text=f"Oportunidades restantes: {self.hangman.opportunities}")

        # Comprobar si ganó
        if self.hangman.is_guessed():
            self.lbl_opportunities.config(text="¡FELICIDADES HAS GANADO EL JUEGO!")
            self.entry_letter.pack_forget()
            self.btn_guess.pack_forget()
            self.character_label.pack_forget()
            self.btn_restart.pack(pady=20)

        # Comprobar si perdió
        elif self.hangman.opportunities == 0:
            self.lbl_opportunities.config(text="¡Juego terminado! INTÉNTALO DE NUEVO")
            self.entry_letter.pack_forget()
            self.character_label.pack_forget()
            self.btn_guess.pack_forget()
            self.btn_restart.pack(pady=20)


    def reiniciar_juego(self):
        # 1. Limpiar entradas
        self.entry_secret.delete(0, tk.END)
        self.entry_letter.delete(0, tk.END)

        # 2. Ocultar el botón de reiniciar y la pantalla de juego
        self.btn_restart.pack_forget()
        self.frame_game.pack_forget()

        # 3. Volver a mostrar los elementos de adivinanza por si se habían ocultado
        self.character_label.pack(anchor="w", pady=5)
        self.entry_letter.pack(fill="x", pady=5)
        self.btn_guess.pack(pady=10)

        # 4. Mostrar de nuevo la pantalla de configuración inicial
        self.frame_setup.pack(fill="both", expand=True)


if __name__ == "__main__":
    ventana = tk.Tk()
    hangman = Hangman("", "", 3)
    app = HangmanGUI(ventana, hangman)
    ventana.mainloop()