from websiteMaker import *  # import all function from function.py


def main():
    """main function to run the program"""
    delete()  # delete the _site folder
    make()  # make the _site folder
    blogMaker()
    pageMaker()
    indexMaker()
    get_titles()


# yamle to data
# markdown to html
# jinja = html + data
if __name__ == "__main__":
    main()
