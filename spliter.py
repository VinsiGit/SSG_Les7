import yaml
import markdown


def pageSpliter(file):
    """_summary_ : splits the file into frontmatter and backmatter of the pages"""
    return spliter(f"pages/{file}")


def postSpliter(file):
    """_summary_ : splits the file into frontmatter and backmatter of the posts"""

    return spliter(f"posts/{file}")


def spliter(file):
    """_summary_ : splits the file into frontmatter and backmatter"""
    file = open(file, "r")
    fileR = file.read()
    try:
        yaml_end = fileR.index("---", 3)
        frontmatter = fileR[3:yaml_end]
        backmatter = fileR[yaml_end + 3 :]
    except ValueError:
        yaml_end = 0
        frontmatter = ""
        backmatter = fileR[yaml_end:]
        print("No yaml found")
    file.close()
    print(frontmatter)

    try:
        data = yaml.safe_load(frontmatter)
    except:
        print("No yaml found")
        data = {"title": "No title", "date": "No date"}

    try:
        data["title"]
    except:
        data["title"] = "No title"

    try:
        data["date"]
    except:
        data["date"] = "No date"
    try:
        data["author"]
    except:
        data["author"] = "No author"
    html = markdown.markdown(backmatter)
    print(data)

    print(frontmatter)
    print(backmatter)

    print(data["title"])
    return {"yaml": data, "md": html}
