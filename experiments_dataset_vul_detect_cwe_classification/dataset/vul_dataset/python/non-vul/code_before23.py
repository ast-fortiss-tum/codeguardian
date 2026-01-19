# Source: Row 9 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_863.xlsx

def get_by_name(self, name, project):
    return (
        Person.query.filter(Person.name == name)
        .filter(Project.id == project.id)
        .one()
    )