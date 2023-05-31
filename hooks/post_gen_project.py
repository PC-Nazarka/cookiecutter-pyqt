import os


def main():
    if "{{cookiecutter.pyinstaller}}" == "n":
        os.remove("./{{cookiecutter.project_slug}}.spec")


if __name__ == "__main__":
    main()
