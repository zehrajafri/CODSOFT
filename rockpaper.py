import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("450x800")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)
        
        # Game state
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        # Choice mappings
        self.choice_emojis = {'r': '🗿', 'p': '📄', 's': '✂️'}
        self.choice_names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
        
        self.setup_ui()
    
    def setup_ui(self):
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎮 ROCK PAPER SCISSORS", 
            font=('Arial', 20, 'bold'),
            bg='#2C3E50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg='#34495E', relief='raised', bd=2)
        score_frame.pack(pady=9, padx=20, fill='x')
        
        # Score labels
        score_title = tk.Label(score_frame, text="SCORE", font=('Arial', 12, 'bold'), bg='#34495E', fg='white')
        score_title.pack(pady=4)
        
        scores_container = tk.Frame(score_frame, bg='#34495E')
        scores_container.pack(pady=4)
        
        # Wins
        wins_frame = tk.Frame(scores_container, bg='#34495E')
        wins_frame.pack(side='left', padx=20)
        self.wins_label = tk.Label(wins_frame, text="0", font=('Arial', 24, 'bold'), bg='#34495E', fg='#2ECC71')
        self.wins_label.pack()
        tk.Label(wins_frame, text="Wins", font=('Arial', 10), bg='#34495E', fg='white').pack()
        
        # Losses
        losses_frame = tk.Frame(scores_container, bg='#34495E')
        losses_frame.pack(side='left', padx=20)
        self.losses_label = tk.Label(losses_frame, text="0", font=('Arial', 24, 'bold'), bg='#34495E', fg='#E74C3C')
        self.losses_label.pack()
        tk.Label(losses_frame, text="Losses", font=('Arial', 10), bg='#34495E', fg='white').pack()
        
        # Ties
        ties_frame = tk.Frame(scores_container, bg='#34495E')
        ties_frame.pack(side='left', padx=20)
        self.ties_label = tk.Label(ties_frame, text="0", font=('Arial', 24, 'bold'), bg='#34495E', fg='#F39C12')
        self.ties_label.pack()
        tk.Label(ties_frame, text="Ties", font=('Arial', 10), bg='#34495E', fg='white').pack()
        
        # Game area
        game_frame = tk.Frame(self.root, bg='#2C3E50')
        game_frame.pack(pady=18, fill='both', expand=True)
        
        # Choice buttons
        choices_label = tk.Label(game_frame, text="Choose your move:", font=('Arial', 14), bg='#2C3E50', fg='white')
        choices_label.pack(pady=9)
        
        buttons_frame = tk.Frame(game_frame, bg='#2C3E50')
        buttons_frame.pack(pady=9)
        
        # Rock button
        rock_btn = tk.Button(
            buttons_frame,
            text="🗿\nROCK",
            font=('Arial', 16, 'bold'),
            width=8,
            height=3,
            bg='#95A5A6',
            fg='white',
            relief='raised',
            bd=3,
            command=lambda: self.play_game('r')
        )
        rock_btn.pack(side='left', padx=10)
        
        # Paper button
        paper_btn = tk.Button(
            buttons_frame,
            text="📄\nPAPER",
            font=('Arial', 16, 'bold'),
            width=8,
            height=3,
            bg='#3498DB',
            fg='white',
            relief='raised',
            bd=3,
            command=lambda: self.play_game('p')
        )
        paper_btn.pack(side='left', padx=10)
        
        # Scissors button
        scissors_btn = tk.Button(
            buttons_frame,
            text="✂️\nSCISSORS",
            font=('Arial', 16, 'bold'),
            width=8,
            height=3,
            bg='#E67E22',
            fg='white',
            relief='raised',
            bd=3,
            command=lambda: self.play_game('s')
        )
        scissors_btn.pack(side='left', padx=10)
        
        # VS section
        vs_frame = tk.Frame(game_frame, bg='#34495E', relief='sunken', bd=2)
        vs_frame.pack(pady=20, padx=20, fill='x')
        
        vs_container = tk.Frame(vs_frame, bg='#34495E')
        vs_container.pack(pady=15)
        
        # Player choice
        player_frame = tk.Frame(vs_container, bg='#34495E')
        player_frame.pack(side='left', padx=30)
        self.player_display = tk.Label(player_frame, text="❓", font=('Arial', 40), bg='#34495E', fg='white')
        self.player_display.pack()
        tk.Label(player_frame, text="YOU", font=('Arial', 12, 'bold'), bg='#34495E', fg='white').pack()
        
        # VS label
        vs_label = tk.Label(vs_container, text="VS", font=('Arial', 18, 'bold'), bg='#34495E', fg='#F39C12')
        vs_label.pack(side='left', padx=20)
        
        # Computer choice
        computer_frame = tk.Frame(vs_container, bg='#34495E')
        computer_frame.pack(side='left', padx=30)
        self.computer_display = tk.Label(computer_frame, text="❓", font=('Arial', 40), bg='#34495E', fg='white')
        self.computer_display.pack()
        tk.Label(computer_frame, text="COMPUTER", font=('Arial', 12, 'bold'), bg='#34495E', fg='white').pack()
        
        # Result display
        self.result_label = tk.Label(
            game_frame,
            text="Choose your move!",
            font=('Arial', 16, 'bold'),
            bg='#2C3E50',
            fg='white',
            pady=14
        )
        self.result_label.pack(pady=10)
        
        # Reset button
        reset_btn = tk.Button(
            game_frame,
            text="🔄 Reset Game",
            font=('Arial', 12, 'bold'),
            bg='#8E44AD',
            fg='white',
            relief='raised',
            bd=3,
            padx=20,
            pady=5,
            command=self.reset_game
        )
        reset_btn.pack(pady=9)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Click on Rock, Paper, or Scissors to play!\nPress 'R', 'P', or 'S' keys for quick play",
            font=('Arial', 10),
            bg='#2C3E50',
            fg='#BDC3C7'
        )
        instructions.pack(pady=9)
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
    
    def play_game(self, player_move):
        # Generate computer move (same logic as original)
        random_number = random.randint(1, 3)
        if random_number == 1:
            computer_move = 'r'
        elif random_number == 2:
            computer_move = 'p'
        else:
            computer_move = 's'
        
        # Update displays
        self.player_display.config(text=self.choice_emojis[player_move])
        self.computer_display.config(text=self.choice_emojis[computer_move])
        
        # Determine winner (same logic as original)
        if player_move == computer_move:
            result_text = "It's a tie! 🤝"
            result_color = '#F39C12'
            self.ties += 1
        elif ((player_move == 'r' and computer_move == 's') or
              (player_move == 'p' and computer_move == 'r') or
              (player_move == 's' and computer_move == 'p')):
            result_text = f"You win! 🎉\n{self.choice_names[player_move]} beats {self.choice_names[computer_move]}"
            result_color = '#2ECC71'
            self.wins += 1
        else:
            result_text = f"You lose! 😢\n{self.choice_names[computer_move]} beats {self.choice_names[player_move]}"
            result_color = '#E74C3C'
            self.losses += 1
        
        # Update result display
        self.result_label.config(text=result_text, fg=result_color)
        
        # Update score
        self.update_score()
    
    def update_score(self):
        self.wins_label.config(text=str(self.wins))
        self.losses_label.config(text=str(self.losses))
        self.ties_label.config(text=str(self.ties))
    
    def reset_game(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        self.update_score()
        
        self.player_display.config(text="❓")
        self.computer_display.config(text="❓")
        self.result_label.config(text="Choose your move!", fg='white')
    
    def on_key_press(self, event):
        key = event.char.lower()
        if key in ['r', 'p', 's']:
            self.play_game(key)
        elif event.keysym == 'Escape':
            self.reset_game()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
