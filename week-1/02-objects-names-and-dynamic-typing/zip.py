def main() -> None:
    names = ["Cedrick", "Alice", "Bob"]
    scores = [98, 99, 100]

    for name, score in zip(names, scores):
        print(f"{name}", ""*1, f"{score}")

if __name__ == '__main__':
    main()