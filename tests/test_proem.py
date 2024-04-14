import pytest
from json import JSONDecodeError
# from contextlib import nullcontext as does_not_raise
from proem import Proem
import os

@pytest.mark.parametrize('app_nm, flavor_text, version, repo_url, width, border_char, border_color, description, expected_build_text, expected_except', [
    ("test-app", None, None, None, 1, '#', 'magenta', None, '', ValueError),
])

def test_build_func(app_nm, flavor_text, version, repo_url, width, border_char, border_color, description, expected_build_text, expected_except):

    proem = Proem(
        app_nm,
        flavor_text,
        version,
        repo_url,
        width,
        border_char,
        border_color,
        description
    )

    build_text = proem.build()

    assert build_text == expected_build_text
