
from django.http import HttpResponse
from agency.data_base.agency_data_base import AgencyDataBaseManager
import agency.data_base.config as config

styles = """
<style>
    body {
        font-family: arial, sans-serif;
        width: 500px;
        margin: auto;
    }
    h3 {
        text-align: center;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    thead tr {
        background-color: #ffc0cb;
    }
    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
"""

manager = AgencyDataBaseManager(config.url, config.database, config.username, config.password)


def category_to_html(category_id: int, name: str):
    return """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td><a href="news/%s">%s</a></td>
    </tr>""" % (category_id, name, category_id, name)


def news_to_html(news_id: int, category_id: int, name: str, pages: int, author: str):
    return """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>""" % (news_id, category_id, name, pages, author)


def categories(request):
    _categories = manager.get_all_categories()
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Categories</title>
        %s
    </head>
    <body>
        <h3>Categories</h3>
        <table>
            <thead>
                <tr>
                    <th>Category id</th>
                    <th>Name</th>
                    <th>News in this category<th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
    """ % (styles, ''.join([category_to_html(category[0], category[1]) for category in _categories])))


def news(request, category_id):
    _news = manager.get_news_by_parameter("category", category_id)
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>News</title>
        %s
    </head>
    <body>
        <h3>News</h3>
        <table>
            <thead>
                <tr>
                    <th>News id</th>
                    <th>Category id</th>
                    <th>Name</th>
                    <th>Num pages</th>
                    <th>Author</th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
    """ % (styles, ''.join([news_to_html(nw[0], nw[1], nw[2], nw[3], nw[4]) for nw in _news])))
