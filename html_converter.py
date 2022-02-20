import os


import pdfkit
import imgkit


def check_folder(folder):
    """
    Check if a folder exists, if not, create it
    
    :param folder: the name of the folder where the data will be saved
    """
    if not os.path.isdir(f'./{folder}'):
        os.makedirs(f'./{folder}')


def convert_html_url_to_pdf(html_url: str, save_name: str) -> object:
    """
    Convert an url to a pdf file
    :param html_url: The URL of the HTML page to convert to PDF
    :type html_url: str
    :param save_name: The name of the PDF file you want to save as
    :type save_name: str
    """
    pdfkit.from_url(html_url, f'./outputs/{save_name}.pdf')


def convert_html_url_to_img(html_url: str, save_name: str) -> object:
    """
    Convert a html url to an image file
    :param html_url: The URL of the HTML page you want to convert to an image
    :type html_url: str
    :param save_name: The name of the image file to be saved
    :type save_name: str
    """
    imgkit.from_url(html_url, f'./outputs/{save_name}.svg')


def convert_html_file_to_pdf(html_file: str, save_name: str) -> object:
    """
    Convert a html file to pdf
    :param html_file: File name of the HTML file to convert to PDF
    :type html_file: str
    :param save_name: The name of the PDF file you want to save as
    :type save_name: str
    """
    pdfkit.from_file(f'./src/{html_file}.html', f'./outputs/{save_name}.pdf')


def convert_html_file_to_img(html_file: str, save_name: str) -> object:
    """
    Converts a html file to an image file
    :param html_file: File name of the HTML file you want to convert to an image
    :type html_file: str
    :param save_name: The name of the image file that will be saved
    :type save_name: str
    """
    imgkit.from_file(f'./src/{html_file}.html', f'./outputs/{save_name}.png')


def ask_input():
    """
    Ask the user to choose what to do.
    :return: The function ask_input() returns the value of the variable question.
    """
    question = int(input(
'''
Choose what I should to do:
1. Convert HTML URL to PDF;
2. Convert HTML URL to Image.

Type here: '''))
    print()
    return question


def ask_user():
    """
    It asks the user to choose between converting a URL to PDF or to image
    :return: Nothing.
    """
    conditions = (1, 2)
    answer = ask_input()
    while True:
        if answer not in conditions:
            print('Wrong input!!!')
            answer = ask_input()
            continue
        break

    extension = 'PDF' if answer == 1 else 'Image'
    url = input(f'Input URL that I should convert to {extension}: ')
    try:
        save_name = url.split('//')[1][:-1].split('.')[0]
    except:
        print('\nInput full adress with https\n')
    return convert_html_url_to_pdf(url, save_name) if answer == 1 else convert_html_url_to_img(url, save_name)


if __name__ == '__main__':
    check_folder('outputs')
    ask_user()
    print('\nFile is ready.')
