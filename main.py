from archivo import Archivo
from repositorio import Repositorio
import datetime


def main():
    repo = Repositorio()
    commands = {
        "create_branch": "create_branch <branch_name>",
        "change_branch": "change_branch <branch_name>",
        "make_commit": "make_commit <author> <message> <file1> [<file2> ...]",
        "merge_branch": "merge_branch <source_branch> <target_branch>",
        "list_commits": "list_commits",
        "create_file": "create_file <file_name.xxx> <text>",
        "append_file": "append_file <file_name.xxx> <text>",
        "exit": "exit",
        "help": "help",
    }

    while True:
        command = input("Enter command: ").strip().split()
        if not command:
            continue
        cmd = command[0].lower()

        try:
            if cmd == "create_branch":
                if len(command) != 2:
                    print(f"Usage: {commands['create_branch']}")
                    continue
                repo.create_branch(command[1])
                print("New branch created")
                print()

            elif cmd == "change_branch":
                if len(command) != 2:
                    print(f"Usage: {commands['change_branch']}")
                    continue
                repo.change_branch(command[1])
                print("Branch changed")
                print()

            elif cmd == "make_commit":
                if len(command) < 4:
                    print(f"Usage: {commands['make_commit']}")
                    continue
                author = command[1]
                message = command[2]
                files = [Archivo(file_name) for file_name in command[3:]]
                date = datetime.datetime.now()
                repo.make_commit(author, message, files, date)
                print("Commit created")
                print()

            elif cmd == "merge_branch":
                if len(command) != 3:
                    print(f"Usage: {commands['merge_branch']}")
                    continue
                repo.merge_branch(command[1], command[2])
                print("Source merged into target")
                print()

            elif cmd == "list_commits":
                commits = repo.list_commits()
                for commit in commits:
                    print(commit.show_commit())
                print()

            elif cmd == "create_file":
                if len(command) < 3:
                    print(f"Usage: {commands['create_file']}")
                    continue
                file_name = command[1]
                text = " ".join(command[2:])
                archivo = Archivo(file_name)
                archivo.write(text)
                print(f"File '{file_name}' created with text: {text}")
                print()

            elif cmd == "append_file":
                if len(command) < 3:
                    print(f"Usage: {commands['append_file']}")
                    continue
                file_name = command[1]
                text = " ".join(command[2:])
                archivo = Archivo(file_name)
                try:
                    archivo.add(text)
                    print(f"Text appended to '{file_name}': {text}")
                except FileNotFoundError as e:
                    print(e)
                print()

            elif cmd == "help":
                for cmd, usage in commands.items():
                    print(f"{cmd}: {usage}")

            elif cmd == "exit":
                break

            else:
                print("Unknown command. Escribe 'help' para ver todos los comandos.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
