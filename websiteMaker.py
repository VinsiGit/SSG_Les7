import jinja2
import os
from pathlib import Path
from spliter import pageSpliter, postSpliter
import shutil


# from datetime import datetime
def delete():
    """_summary_ : delete the _site folder"""
    te_verwijderen_directory = Path("_site/")
    try:
        shutil.rmtree(te_verwijderen_directory)
    except OSError as e:
        print(f"Fout: {te_verwijderen_directory} : {e.strerror}")


def make():
    """_summary_ : make the _site folder and moves the css folder to _site folder"""
    shutil.copytree("templates/css", "_site/css")  #  move directory


def site_dr():
    p = Path("_site/")
    try:
        p.mkdir()
    except FileExistsError as exc:
        print(exc)


def pageNav():
    """_summary_ : returns a list with the pages and blog"""
    change = []
    change.append("index")
    change.append("blog")
    for websites in get_titles():
        change.append(websites.replace(" ", "-"))
    return change


def replaces(file):
    """_summary_ : replaces the list with the pages and blog"""
    file = str(file)
    file = file.replace("[", "")
    file = file.replace("]", "")
    file = file.replace("'", "")
    file = file.replace(",", "")
    return file


def get_titles():
    """_summary_ : returns a list with the titles of the pages"""
    titlePages = []
    i = 1
    for dirpath, dirnames, files in os.walk("pages", topdown=False):
        print(f"Directory gevonden: {dirpath}")
        for bestandsnaam in files:
            print(f"Bestand gevonden: {bestandsnaam}")
            title = pageSpliter(bestandsnaam)["yaml"]["title"]
            if title in titlePages:
                titlePages.append(f"{title}-{i}")
                i += 1
            else:
                titlePages.append(title)

    print(titlePages)
    return titlePages


def blogMaker():
    """_summary_: makes the blog.html file"""
    arr = []
    arrData = []
    PATH = "posts"
    for dirpath, dirnames, files in os.walk(PATH, topdown=False):
        for file in files:
            html = postSpliter(file)["md"]
            arr.append(html)
            data = postSpliter(file)["yaml"]
            arrData.append(data)

    print(arr)
    print(arrData)
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/blog.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(
        post=arr, arrData=arrData, CHANGE=pageNav()
    )  # this is where to put args to the template renderer
    print(outputText)

    p = Path("_site/")
    try:
        f = open(f"{p}/blog.html", "x")
    except:
        print("File already exists")
    f = open(f"{p}/blog.html", "w")
    f.write(outputText)
    f.close()


def pageMaker():
    """_summary_: makes the pages.html files"""
    PATH = "pages"
    title = []
    for websites in get_titles():
        title.append(websites)
    i = 0
    for dirpath, dirnames, files in os.walk(PATH, topdown=False):
        for file in files:
            html = pageSpliter(file)["md"]
            data = pageSpliter(file)["yaml"]

            templateLoader = jinja2.FileSystemLoader(searchpath="./")
            templateEnv = jinja2.Environment(loader=templateLoader)
            TEMPLATE_FILE = "templates/felix.html"
            template = templateEnv.get_template(TEMPLATE_FILE)
            outputText = template.render(
                title=data["title"], date=data["date"], page=html, CHANGE=pageNav()
            )  # this is where to put args to the template renderer
            print(outputText)

            p = Path("_site/")
            p = f"{p}/{title[i].replace(' ', '-')}.html"
            try:
                f = open(p, "x")
            except:
                print("File already exists")
            f = open(p, "w")
            f.write(outputText)
            f.close()
            i += 1


def indexMaker():
    """_summary_: makes the index.html file"""
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/index.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(
        CHANGE=pageNav()
    )  # this is where to put args to the template renderer
    print(outputText)

    p = Path("_site/")
    try:
        f = open(f"{p}/index.html", "x")
    except:
        print("File already exists")
    f = open(f"{p}/index.html", "w")
    f.write(outputText)
    f.close()
