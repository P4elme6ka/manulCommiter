import pymorphy2
from num2words import num2words
import git
import os

morph = pymorphy2.MorphAnalyzer()

gitRepoPath = "./"

repoFilePath = "manuls.txt"

remoteName = "origin"


def get_manul_phrase(num):
    txt_number_of_manuls = num2words(num, lang="ru")
    manul_token = morph.parse("манул")[0]
    return txt_number_of_manuls + " " + manul_token.make_agree_with_number(num).word


def main():
    repo = git.cmd.Repo(gitRepoPath)
    repo.git.pull()
    file_path = os.path.join(gitRepoPath, repoFilePath)
    with open(file_path, "rb") as f:
        file_manul_count = sum(1 for _ in f)
    with open(file_path, "a") as f:
        f.write(get_manul_phrase(file_manul_count + 1) + "\n")

    repo.git.add(repoFilePath)
    repo.index.commit(f"manuls update #{file_manul_count}")
    origin = repo.remote(name=remoteName)
    origin.push()


if __name__ == "__main__":
    main()
