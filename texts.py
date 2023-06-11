class StartPage:
    hello_text = 'Hi! Welcome to our\nEnglish class'
    name = 'What is your name?'


class EndRulePage:
    end_rule = ' , now you\nknow all about\nprepositions of time'
    end_rule_lets = "Let's do some exercises!"


class BufferPage:
    well = "You're doing well!"


def get_practice_insert_texts():
    with open('practice_texts/practice_insert_texts.txt', 'r') as file:
        txt = file.read()
    lines = txt.split('\n')
    return lines


class PracticeInsertPage:
    lines = get_practice_insert_texts()
    answers = 'in, in, on, at, in, on, in, at, in'.split(', ')


def get_exam_texts():
    with open('exam_texsts/questions.txt', 'r') as file:
        txt = file.read()
    lines = txt.split('\n')
    return lines


class ExamPage:
    lines = get_exam_texts()
    answers = 'in, at, on, on/on, on, at, on, at, at, at'.split(', ')


class MenuPage:
    choose = ' choose one\noption'


def get_rule_third_text():
    with open('big_texts/rule_third.txt', 'r') as file:
        return file.read()


def get_rule_second_1():
    with open('big_texts/rule_second_1.txt', 'r') as file:
        return file.read()


def get_rule_second_2():
    with open('big_texts/rule_second_2.txt', 'r') as file:
        return file.read()


def get_rule_second_3():
    with open('big_texts/rule_second_2.txt', 'r') as file:
        return file.read()


class RulePage:
    rule_first_text = '''In this article, we will look at the basic rules\nand give examples to help you deal 
    with\nprepositions of time, and at the end \nyou can pass a test. '''
    rule_third_text = get_rule_third_text()
    rule_second_1 = get_rule_second_1()
    rule_second_2 = get_rule_second_2()
    rule_second_3 = get_rule_second_3()
