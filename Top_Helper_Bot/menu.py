"""Main Bot menu"""

from sort import main as sort_main
from note_functions import run_notes as nb_main
from ab_functions import main as ab_main
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_menu():
    work_loop = True
    while work_loop:
        user_input = input(
            '\nBot Main menu\n1 - AdressBook\n2 - NoteBook\n3 - FileSorter\n0 - Exit\n\nBot waiting '
            '... press button >>> ')
        if user_input == "1":  # 1 - AdressBook
            print('Start AdressBook application')
            ab_main()
            print('Finish AdressBook application')
        elif user_input == "2":  # 2 - NoteBook
            print('Start NoteBook application')
            nb_main()
            print('Finish NoteBook application')
        elif user_input == "3":  # 3 - FileSorter
            print('Start FileSorter application')
            sort_main()
            print('Finish FileSorter application')
            pass
        elif user_input == 5:
            pass
        elif user_input == 6:
            pass
        elif user_input == '0':
            work_loop = False
        else:
            continue

    pass


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
