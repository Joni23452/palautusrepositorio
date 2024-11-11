class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list_authors(self, authors):
        auth_str = ""
        for author in authors:
            auth_str+=author+"\n"
        return auth_str


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            #f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors:"
            f"\n{self._list_authors(self.authors)}"
            f"\n"
            f"\nDependencies:"
            f"\n{self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
