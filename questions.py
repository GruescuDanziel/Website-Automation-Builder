import PyInquirer as pi

def listChoice(listOfOptions):
    question = [{
        'type' : 'list',
        'name' : 'choice',
        'message' : 'Which one will you chose?',
        'choices' : listOfOptions,
        }]
    return pi.prompt(question)['choice']

def inputQuestion():
    question = [{

        'type' : 'input',
        'name' : 'choice',
        'message' : 'What will you name it',

    }]
    return pi.prompt(question)['choice']

def confirmQuestion():
    question = [{

        'type' : 'confirm',
        'name' : 'choice',
        'message' : 'Do you wish to exit?',
        'default' : False
    }]
    return pi.prompt(question)['choice']

def editQuestion(default):
    question = [{
        'type': 'editor',
        'name': 'data',
        'default': default,
        'message': 'What do you wish to input inside your tag',
        'eargs': {
            'editor':'vim'
        }
    }]
    return pi.prompt(question)['data']
