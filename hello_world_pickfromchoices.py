import inquirer
#meeting the requirements using inquirer extension
questions = [
  inquirer.List('greeting',
                message="Pick your greeting?",
                choices=['Southern', 'A', 'B', 'C', 'D', 'E'],
            ),
]

answers = inquirer.prompt(questions)

print("Hello Nishaya, welcome", answers["greeting"])
