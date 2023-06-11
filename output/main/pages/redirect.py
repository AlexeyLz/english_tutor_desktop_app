from user import User


def redirect_to_rule_page(window, frame):
    frame.destroy()
    from pages.rule_page import rule_frame
    rule_frame(window=window)


def redirect_to_menu(window, frame):
    frame.destroy()
    from pages.menu_page import menu_frame
    menu_frame(window)


def redirect_to_practice(window, frame):
    frame.destroy()
    User.question = 0
    from pages.practice_page import practice_frame
    practice_frame(window)
