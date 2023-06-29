import hashlib
import os
import string
from threading import Thread


class BruteForce:
    def __init__(self, pwd, length):
        self.pwd = pwd
        self.chars = "ABC123"# string.ascii_letters + string.digits
        self.chars_indices = [[a, b, c, d, e, f, g, h]
                              for a in range(len(self.chars))
                              for b in range(len(self.chars))
                              for c in range(len(self.chars))
                              for d in range(len(self.chars))
                              for e in range(len(self.chars))
                              for f in range(len(self.chars))
                              for g in range(len(self.chars))
                              for h in range(len(self.chars))
                              ]
        self.found = False
        self.length = length

    def combination(self, t):
        def text_to_md5(text):
            encoded_text = hashlib.md5(text.encode())
            return encoded_text.hexdigest()
        for i in range(0 + t, len(self.chars_indices), 8):
            if self.found:
                break
            generated_text = ""
            for index in self.chars_indices[i]:
                generated_text += self.chars[index]
                print(f"Thread {t} is trying:  {generated_text}")
            if text_to_md5(generated_text) == self.pwd:
                self.found = True
                print(f"Found: {generated_text}")
                quit()


if __name__ == "__main__":
    brute_force = BruteForce("16b949fd29d0be4a18dc96f200f027e0", 8)
    threads = []
    for k in range(os.cpu_count()):
        threads.append(Thread(target=brute_force.combination, args=(k, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
