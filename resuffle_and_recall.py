import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class ShuffleAndRecall:
    def __init__(self):
        self.cards = ['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H']
        self.revealed = [False] * 16
        self.matched = [False] * 16
        self.score = 0
        self.attempts = 0
        
    def initialize_game(self):
        # Fisher-Yates Shuffle
        for i in range(15, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
    def display_board(self):
        clear_screen()
        print("═══════════════════════════════════════")
        print("        🎮 SHUFFLE AND RECALL 🎮        ")
        print("═══════════════════════════════════════")
        print(f"Score: {self.score}  |  Attempts: {self.attempts}")
        print("---------------------------------------")
        
        for row in range(4):
            for col in range(4):
                index = row * 4 + col
                if self.matched[index]:
                    print(f"[✓{self.cards[index]}] ", end="")
                elif self.revealed[index]:
                    print(f"[ {self.cards[index]} ] ", end="")
                else:
                    print("[ ? ] ", end="")
            print()
        print("═══════════════════════════════════════")
    
    def select_card(self, card_num):
        while True:
            try:
                position = int(input(f"Pilih kartu ke-{card_num} (1-16): ")) - 1
                if position < 0 or position > 15:
                    print("❌ Posisi tidak valid!")
                elif self.revealed[position] or self.matched[position]:
                    print("❌ Kartu sudah terbuka atau cocok!")
                else:
                    return position
            except ValueError:
                print("❌ Masukkan angka!")
    
    def check_match(self, pos1, pos2):
        self.attempts += 1
        self.revealed[pos1] = True
        self.revealed[pos2] = True
        self.display_board()
        
        if self.cards[pos1] == self.cards[pos2]:
            print(f"✅ COCOK! Kartu {self.cards[pos1]} ditemukan!")
            self.matched[pos1] = True
            self.matched[pos2] = True
            self.score += 10
            time.sleep(1)
        else:
            print(f"❌ TIDAK COCOK! {self.cards[pos1]} vs {self.cards[pos2]}")
            time.sleep(2)
            self.revealed[pos1] = False
            self.revealed[pos2] = False
    
    def check_game_over(self):
        return all(self.matched)
    
    def play(self):
        self.initialize_game()
        
        while True:
            self.display_board()
            
            # Pilih 2 kartu
            first_card = self.select_card(1)
            self.revealed[first_card] = True
            self.display_board()
            
            second_card = self.select_card(2)
            
            if second_card == first_card:
                print("❌ Pilih kartu yang berbeda!")
                self.revealed[first_card] = False
                time.sleep(1)
            else:
                self.check_match(first_card, second_card)
            
            if self.check_game_over():
                break
        
        self.display_board()
        print("🎉 SELAMAT! ANDA MENANG! 🎉")
        print(f"Total Skor: {self.score}")
        print(f"Total Percobaan: {self.attempts}")
        print(f"Akurasi: {(8/self.attempts * 100):.1f}%")

# Jalankan game
if __name__ == "__main__":
    game = ShuffleAndRecall()
    game.play()