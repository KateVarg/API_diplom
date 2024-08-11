import os
import API_autotest_diplom
from pathlib import Path


def abs_path_from_project(relative_path: str):
    return (
        Path(API_autotest_diplom.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
