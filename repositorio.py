from rama import Rama
from commit import Commit


class Repositorio:
    def __init__(self):
        self.branches = {}
        self.actual_branch = None

    def create_branch(self, name):
        if name in self.branches:
            raise ValueError(f"La rama '{name}' ya existe.")
        new_branch = Rama(name)
        self.branches[name] = new_branch
        if self.actual_branch is None:
            self.actual_branch = new_branch

    def make_commit(self, author, message, archives, date):
        if not self.actual_branch:
            raise ValueError("No hay una rama seleccionada para hacer un commit.")
        new_commit = Commit(author, message, archives, self.actual_branch.commit, date)
        self.actual_branch.commit = new_commit

    def change_branch(self, name):
        if name not in self.branches:
            raise ValueError(f"La rama '{name}' no existe.")
        self.actual_branch = self.branches[name]

    def merge_branch(self, source_branch_name, target_branch_name):
        if (
            source_branch_name not in self.branches
            or target_branch_name not in self.branches
        ):
            raise ValueError("Una o ambas ramas no existen.")
        source_branch = self.branches[source_branch_name]
        target_branch = self.branches[target_branch_name]
        target_branch.commit = source_branch.commit

    def list_commits(self):
        if not self.actual_branch:
            raise ValueError("No hay una rama seleccionada.")
        commits = []
        current_commit = self.actual_branch.commit
        while current_commit:
            commits.append(current_commit)
            current_commit = current_commit.parent_commit
        return commits

    def __str__(self):
        estado_ramas = [
            f"{rama} -> Commit: {rama.commit}" for rama in self.branches.values()
        ]
        return "\n".join(estado_ramas)
