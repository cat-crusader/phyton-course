from AgencyDataBaseManager import AgencyDataBaseManager as adbm
from utils import print_categories, print_news

def demo():
    print("\n\n********** initial data in data base *******\n")
    agency = adbm()
    print("Categories:")
    print_categories(agency.get_all_categories())
    print("\nNews:")
    print_news(agency.get_all_news())

    print("\n*************** adding *******************\n")
    # valid adding
    print(agency.add_category(3, 'Politic'), "\n")
    print(agency.add_news(3, 3, "impichment", 6, "ronald"), "\n")
    print(agency.add_news(4, 1, "ufc", 9, "rick"), "\n")
    # invalid adding
    print(agency.add_category(3, "cooking"), "\n")
    print(agency.add_news(1, 3, "basketball", 6, "ihor"), "\n")
    print(agency.add_news(5, 5, "aircraft", 60, "ronald"), "\n")
    print("Categories:")
    print_categories(agency.get_all_categories())
    print("\nNews:")
    print_news(agency.get_all_news())

    print("\n*************** search *******************\n")
    print_news(agency.get_news_by_parameter("author", "rick"))
    print()
    print_news(agency.get_news_by_parameter("num_pages", 6))
    print()
    print_categories(agency.get_categories_by_parameter("id", 2))
    print()
    print(" num:", agency.count_news_by_category(1), "\n")
    print(" num:", agency.count_news_by_category(2), "\n")
    print(" num:", agency.count_news_by_category(10), "\n")

    print("\n**************** change ********************\n")
    print(agency.change_category(3, "name", "geo-political"), "\n")
    print(agency.change_news(4, "num_pages", 99), "\n")
    print("Categories:")
    print_categories(agency.get_all_categories())
    print("\nNews:")
    print_news(agency.get_all_news())

    print("\n*************** removing *****************\n")
    print(agency.remove_news(3), "\n")
    print(agency.remove_news(4), "\n")
    print(agency.remove_category(3), "\n")
    print("Categories:")
    print_categories(agency.get_all_categories())
    print("\nNews:")
    print_news(agency.get_all_news())

if __name__ == '__main__':
    demo()