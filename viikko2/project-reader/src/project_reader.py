from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_str = content
        toml_dict = tomli.loads(toml_str)
        #print(toml_dict)
        return Project(toml_dict["tool"]["poetry"]["name"], toml_dict["tool"]["poetry"]["description"], toml_dict["tool"]["poetry"]["dependencies"], toml_dict["tool"]["poetry"]["group"]["dev"]["dependencies"], toml_dict["tool"]["poetry"]["license"], toml_dict["tool"]["poetry"]["authors"])
