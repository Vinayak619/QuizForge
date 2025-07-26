import os
from extractor import extract_text
from gemini import setup, question_generator

def main():
    file_path = input("Enter path to your PDF or TXT file: ")
    text = extract_text(file_path)
    
    if not text:
        print("No text extracted.")
        return

    print("\nText extracted successfully!\n")

    model = setup("API_KEY_HERE")

    questions = question_generator(model, text)
    while True:
        file_name = input("Enter a name for the output file (without .txt): ").strip()
        print("\nGenerating questions...\n")
        if os.path.isfile(f"{file_name}.txt"):
            print("File with the same name already exist.")
        else:
            with open(f"{file_name}.txt", "w") as f:
                f.write(questions)
                break

if __name__ == "__main__":
    main()
