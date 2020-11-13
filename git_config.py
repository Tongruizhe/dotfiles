#! /bin/python3

import subprocess
import re


def set_user_info(key):
    def prompt_value():
        print(f"User: Please type config {key}: ", end="")
        return input()

    def prompt_keep(origin_value):
        print(f"User: Keep config {key} [{origin_value}]? [y/n] ", end="")
        return input()

    def set_key(value):
        cmd = f"git config --global user.{key} {value}"
        print(cmd)
        subprocess.run(f"git config --global user.{key} '{value}'",
                       shell=True, check=True, capture_output=True)

    try:
        p = subprocess.run(f"git config --global user.{key}",
                           shell=True, check=True, capture_output=True, encoding='ASCII')
        origin_value = p.stdout.strip()
        while True:
            choice = prompt_keep(origin_value)
            if choice.lower() == 'n':
                value = prompt_value()
                if value:
                    set_key(value)
                break
            elif choice.lower() == 'y' or not choice:
                break

    except subprocess.CalledProcessError:
        value = prompt_value()
        if value:
            set_key(value)


def set_alias(alias, command, info=None):
    cmd = f"git config --global alias.{alias} '{command}'"
    print(f"Alias: {cmd}")
    subprocess.run(args=cmd, shell=True, check=True)


def set_editor_vscode():
    print("Core: Use [VSCode] for default editor")
    print("Core: You can change the editor by setting the GIT_EDITOR env")
    subprocess.run(args="git config --global core.editor 'code --wait'",
                   shell=True, check=True)


if __name__ == "__main__":
    set_user_info("name")
    set_user_info("email")
    set_editor_vscode()
    set_alias("co", "checkout")
    set_alias("st", "status")
    set_alias("ci", "commit")
    set_alias("br", "branch")
    set_alias("lg", "log --graph --oneline --decorate --all")
    set_alias("lgg", "log --graph --abbrev-commit --decorate --date=relative --all")
