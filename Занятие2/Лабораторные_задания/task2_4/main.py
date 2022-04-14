if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5  # TODO чему равно начальное смещение?
    for offset, char in enumerate(phrase, start=initial_offset):
        print(" " * offset, char)
