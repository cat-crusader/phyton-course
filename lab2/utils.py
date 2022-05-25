def print_categories(categories):
    for row in categories:
        id_ca = row[0]
        name = row[1]
        print('%d\t%s' % (id_ca, name))

def print_news(news):
    for row in news:
        id_ne = row[0]
        id_ca = row[1]
        name = row[2]
        pages = row[3]
        author = row[4]
        print('%d\t%d\t%s\t%d\t%s' % (id_ne, id_ca, name, pages, author))