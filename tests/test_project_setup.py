import difflib
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional
from urllib.parse import ParseResult, urlparse

import requests
import tomli
from bx_django_utils.filename import clean_filename
from bx_py_utils.path import assert_is_dir, assert_is_file
from packaging.version import Version

import findmydevice


PACKAGE_ROOT = Path(__file__).parent.parent


def assert_file_contains_string(file_path, string):
    with file_path.open('r') as f:
        for line in f:
            if string in line:
                return
    raise AssertionError(f'File {file_path} does not contain {string!r} !')


def get_gitlab_version_tag(gitlab_project_url: str) -> Optional[Version]:
    """
    Returns the last non-prerelease Version objects from gitlab tags.
    """
    assert gitlab_project_url.startswith(
        'https://gitlab.com/'
    ), f'No gitlab Project url: {gitlab_project_url!r}'

    result: ParseResult = urlparse(gitlab_project_url)
    path = result.path  # e.g.: '/jedie/django-find-my-device/'
    path = path.strip('/')  # 'jedie/django-find-my-device'
    assert path.count('/') == 1, f'Wrong path {path!r} from: {gitlab_project_url!r}'
    path_escaped = path.replace('/', '%2F')
    tag_url = f'https://gitlab.com/api/v4/projects/{path_escaped}/repository/tags'
    tags = requests.get(tag_url).json()
    for tag in tags:
        version_str = tag['name']
        ver_obj = Version(version_str)
        if ver_obj.base_version and not ver_obj.is_prerelease:
            return ver_obj

    raise AssertionError(
        f'No version found from gitlab tags: {tag_url} (check: {gitlab_project_url})'
    )


def assert_gitlab_project_version(current_version: str, gitlab_project_url: str) -> None:
    """
    Check that current version is the last version from gitlab tags.
    """
    current_ver_obj = Version(current_version)
    gitlab_ver = get_gitlab_version_tag(gitlab_project_url=gitlab_project_url)
    assert gitlab_ver <= current_ver_obj, (
        f'Current version from {gitlab_project_url} is: {gitlab_ver}'
        f' but current package version is: {current_ver_obj}'
    )


def test_version():
    upstream_version = findmydevice.__version__

    assert_gitlab_project_version(
        current_version=upstream_version,
        gitlab_project_url='https://gitlab.com/jedie/django-find-my-device/',
    )

    pyproject_toml_path = Path(PACKAGE_ROOT, 'pyproject.toml')
    pyproject_toml = tomli.loads(pyproject_toml_path.read_text(encoding='UTF-8'))
    pyproject_version = pyproject_toml['tool']['poetry']['version']
    assert pyproject_version.startswith(f'{upstream_version}+ynh')

    # pyproject.toml needs a PEP 440 conform version and used "+ynh"
    # the YunoHost syntax is: "~ynh", just "convert this:
    manifest_version = pyproject_version.replace('+', '~')

    assert_file_contains_string(
        file_path=Path(PACKAGE_ROOT, 'manifest.json'),
        string=f'"version": "{manifest_version}"',
    )


def poetry_check_output(*args):
    poerty_bin = shutil.which('poetry')

    output = subprocess.check_output(
        (poerty_bin,) + args,
        text=True,
        env=os.environ,
        stderr=subprocess.STDOUT,
        cwd=str(PACKAGE_ROOT),
    )
    print(output)
    return output


def test_poetry_check():
    output = poetry_check_output('check')
    assert output == 'All set!\n'


def test_requirements_txt():
    requirements_txt = PACKAGE_ROOT / 'conf' / 'requirements.txt'
    assert_is_file(requirements_txt)

    output = poetry_check_output('export', '-f', 'requirements.txt')
    assert 'Warning' not in output

    current_content = requirements_txt.read_text()

    diff = '\n'.join(
        difflib.unified_diff(
            current_content.splitlines(),
            output.splitlines(),
            fromfile=str(requirements_txt),
            tofile='FRESH EXPORT',
        )
    )
    print(diff)
    assert diff == '', f'{requirements_txt} is not up-to-date! (Hint: call: "make update")'


def test_screenshot_filenames():
    """
    https://forum.yunohost.org/t/yunohost-bot-cant-handle-spaces-in-screenshots/19483
    """
    screenshot_path = PACKAGE_ROOT / 'doc' / 'screenshots'
    assert_is_dir(screenshot_path)
    renamed = []
    for file_path in screenshot_path.iterdir():
        file_name = file_path.name
        if file_name.startswith('.'):
            continue
        cleaned_name = clean_filename(file_name)
        if cleaned_name != file_name:
            new_path = file_path.with_name(cleaned_name)
            file_path.rename(new_path)
            renamed.append(f'{file_name!r} renamed to {cleaned_name!r}')
    assert not renamed, f'Bad screenshots file names found: {", ".join(renamed)}'
