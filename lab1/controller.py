import os
from lab1.spiders.kpi_spider import KPISpider
from lab1.spiders.repka_spider import RepkaSpider

from consolemenu import SelectionMenu


def run_menu():
    menu = SelectionMenu([
        'Crawl www.kpi.ua',
        'Get average texts fragments count',
        'Crawl www.repka.ua',
        'Create XHTML table with laptops from repka.ua'
    ], title='Welcome!')
    menu.show()
    option = menu.selected_option
    if menu.is_selected_item_exit():
        print('Quitting...')
    elif option == 0:
        crawl_kpi()
    elif option == 1:
        get_average_texts_count()
    elif option == 2:
        crawl_repka()
    elif option == 3:
        create_xhtml()


def crawl_kpi():
    os.system('scrapy crawl kpi')
    input(f'kpi.ua was crawled, results are saved to output/kpi.xml')
    run_menu()


def crawl_repka():
    os.system('scrapy crawl repka')
    input(f'repka.ua was crawled, results are saved to output/repka.xml')
    run_menu()


def get_average_texts_count():
    average = KPISpider.get_average_texts_count()
    print(f'Average text fragments: {average}')
    input('Press enter...')
    run_menu()


def create_xhtml():
    RepkaSpider.create_xhtml()
    input('Table created and is available at output/table.xhtml')
    run_menu()


if __name__ == '__main__':
    run_menu()
