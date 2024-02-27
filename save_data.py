class SaveData:
    def __init__(self, filename='save_data.cfg'):
        self.filename = filename
        self.data = []

    def readData(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            open(self.filename, 'w', encoding='utf-8').close()
            self.data = []

    def writeData(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for line in self.data:
                file.write(f"{line}\n")

    def getData(self):
        return self.data
