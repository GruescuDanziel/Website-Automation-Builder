posibleChoices = ['getData', 'createFolder', 'goBackAFolder','createFile', 'checkEntireStructure', 'checkCurrentFolder', 'editFile', 'changeFolder', 'endEditing']
questions = [
    {
        'type' : 'list',
        'name' : 'choice',
        'message' : 'Which one will you chose?',
        'choices' : posibleChoices
    },
    {

        'type' : 'input',
        'name' : 'choice',
        'message' : 'What will you name it',

    },
    {

        'type' : 'confirm',
        'name' : 'confirmation',
        'message' : 'Do you wish to exit?',
        'default' : False
    },
    {
        'type': 'editor',
        'name': 'data',
        'message': 'What do you wish to input inside your tag',
        'eargs': {
            'editor':'vim'
        }
    }
]


