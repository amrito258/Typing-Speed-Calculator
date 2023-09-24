from time import *
import random as r


def mistake(para, user_input):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user_input[i]:
                error += 1

        except:
            error += 1

    return error


def speed_time(time_s, time_e, user_input):
    time_delay = time_e - time_s
    speed = len(user_input) / time_delay
    return round(speed, 2)


test = ['Albert Einstein was a German-born physicist who revolutionized our understanding of the universe with his theory of relativity. He was also a passionate advocate for social justice and peace.',
        "Pythagoras was a Greek philosopher and mathematician who is famous for Pythagoras' theorem, which states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
        'Jamal Nazrul Islam was a Bangladeshi mathematical physicist and cosmologist. He made world-class research on the ultimate fate of the universe, and his work has been highly influential in the field of cosmology.',
        "Isaac Newton was an English physicist, mathematician, and astronomer. He's known for his work on gravity, optics, and the laws of motion, which laid the foundation for modern physics.",
        'Chester Bennington was the lead singer of Linkin Park, a rock band that achieved worldwide success. His life and career were tragically cut short when he died by suicide in 2017.',
        'Iron Maiden was formed in 1975 and has become one of the most successful and influential heavy metal bands in history. Their signature sound is characterized by galloping rhythms, melodic vocals, and blistering guitar solos.',
        'Programming is the process of creating instructions for computers to follow. Computer programs are written in programming languages, which tell the computer what to do.',
        'Linux is a free and open-source operating system that is used on millions of computers. It is known for its stability, flexibility, and security, and it powers everything from smartphones to supercomputers.']

test1 = r.choice(test)
print(' : Typing Speed Calculator')
print(' => ' + test1)
print('')
print('')

time1 = time()
test_input = input(' : Enter => ')
time2 = time()

speed = speed_time(time1, time2, test_input)
error = mistake(test1, test_input)

print(f''' : Speed = {speed} word/sec
 : Error = {error}''')

# Advanced Typing calculator

# import tkinter as tk
# import random
# import time

# # Sample paragraphs for typing tests
# paragraphs = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Programming is the art of telling a computer what to do.",
#     "To be or not to be, that is the question.",
# ]

# class TypingSpeedCalculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Typing Speed Calculator")

#         self.current_paragraph = tk.StringVar()
#         self.user_input = tk.StringVar()
#         self.start_time = None

#         self.init_ui()

#     def init_ui(self):
#         self.current_paragraph.set(random.choice(paragraphs))

#         paragraph_label = tk.Label(self.root, textvariable=self.current_paragraph, wraplength=400)
#         paragraph_label.pack(pady=10)

#         input_entry = tk.Entry(self.root, textvariable=self.user_input, width=40)
#         input_entry.pack()

#         start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
#         start_button.pack(pady=10)

#         self.result_label = tk.Label(self.root, text="", fg="green")
#         self.result_label.pack()

#     def start_typing_test(self):
#         self.user_input.set("")  # Clear the input field
#         self.start_time = time.time()
#         self.root.bind("<Key>", self.check_typing)

#     def check_typing(self, event):
#         user_text = self.user_input.get()
#         original_text = self.current_paragraph.get()
        
#         if user_text == original_text:
#             end_time = time.time()
#             time_taken = end_time - self.start_time
#             words_typed = len(original_text.split())
#             speed = words_typed / (time_taken / 60)
#             accuracy = 100.0

#             self.result_label.config(
#                 text=f"Speed: {speed:.2f} words per minute\nAccuracy: {accuracy:.2f}%"
#             )
            
#             self.root.unbind("<Key>")  # Stop checking typing after completion
#         elif original_text.startswith(user_text):
#             self.result_label.config(text="Keep typing...")
#         else:
#             self.result_label.config(text="Typing error!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TypingSpeedCalculator(root)
#     root.mainloop()
