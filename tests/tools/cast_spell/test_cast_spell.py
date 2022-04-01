from unittest import mock
from src.tools.cast_spell import cast_spell

import pytest


@pytest.fixture
def mock_client():
    with mock.patch(
        "src.tools.helpers.general.Client",
        autospec=True,
    ) as mock_client:
        yield mock_client


def test_cast_spell(mock_client):

    mock_client.spells.cast = mock.Mock(return_value="Potter casted lumos!")

    print(f"ID of `mock_client` in `test_cast_spell` is {id(mock_client)}")

    actual = cast_spell.main()
    expected = "Potter casted lumos!"

    assert actual == expected
