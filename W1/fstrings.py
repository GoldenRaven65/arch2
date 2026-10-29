
def fstring(template: str, *contents: str, **names: str) -> str:
    for index, content in enumerate(contents):
        template = template.replace("/" + str(index) + "/", content)
        for key, value in names.items():
            template = template.replace("/" + key + "/", value)
    return template

print(fstring(f"mijn naam is /myname/ en niet /notmyname/",
            myname = "martijn", notmyname = "de balzakaap"))
print(fstring("mijn collega heet /coworker/", coworker = "gerline"))
