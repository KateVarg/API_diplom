import reqres_in_project_tests
from pathlib import Path


def abs_path_from_project(relative_path: str):
    return (
        Path(reqres_in_project_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
