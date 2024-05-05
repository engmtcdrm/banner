from contextlib import nullcontext as does_not_raise
import os

import pytest

# from contextlib import nullcontext as does_not_raise
from src.proem import Proem

@pytest.mark.parametrize('app_nm, flavor_text, version, repo_url, width, border_char, border_color, description, expected_build_text, expected_except', [
    ("test-app", None, None, None, 1, '#', 'magenta', None, '', pytest.raises(AssertionError)),
])

def test_build_func(app_nm, flavor_text, version, repo_url, width, border_char, border_color, description, expected_build_text, expected_except):

    with expected_except:
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
