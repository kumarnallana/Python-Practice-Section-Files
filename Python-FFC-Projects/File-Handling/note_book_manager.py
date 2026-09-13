from pathlib import Path


class NotesManager:

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.data_folder = self.base_dir / "data"
        self.data_folder.mkdir(parents=True, exist_ok=True)
        self.file_path: Path | None = None

    def create_file(self, filename: str):
        try:
            self.file_path = self.data_folder / filename
            self.file_path.touch(exist_ok=True)

            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(
                    "Developer-Name: kumar Nallana\n Blood: pydantic\n knowledge: Dsa with python"
                )
            return f"File '{filename}' created successfully."
        except Exception as e:
            return f"Error creating file: {e}"

    def add_note(self, new_content: str):
        try:
            if not self.file_path or not self.file_path.exists():
                return "Error: No file has been created yet or file does not exist."

            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(f"\n{new_content}")
            return "Note added successfully."

        except Exception as e:
            return f"Error adding note: {e}"


notes_manager = NotesManager()
print(notes_manager.create_file("demo.txt"))
print(notes_manager.add_note("This is a last message in the end"))

