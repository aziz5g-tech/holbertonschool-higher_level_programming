#!/usr/bin/python3
# ABDULAZIZ ALRSHEDI <11937@holbertonschool.com>
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name)
