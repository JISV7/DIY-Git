class Rama:
    def __init__(self, name, commit=None):
        self.name = name
        self.commit = commit

    def show_branch(self):
        return f"Branch: {self.name}\nLast commit: {self.commit}"
