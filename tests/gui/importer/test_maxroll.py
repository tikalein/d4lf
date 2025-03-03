import pytest
from pytest_mock import MockerFixture

from src.dataloader import Dataloader
from src.gui.importer.maxroll import import_maxroll

URLS = [
    "https://maxroll.gg/d4/build-guides/double-swing-barbarian-guide",
    "https://maxroll.gg/d4/build-guides/frozen-orb-sorcerer-guide",
    "https://maxroll.gg/d4/build-guides/minion-necromancer-guide",
    "https://maxroll.gg/d4/build-guides/shadow-minion-necromancer-guide",
    "https://maxroll.gg/d4/planner/1i5tt0c0#2",
    "https://maxroll.gg/d4/planner/ailu5022#4",
    "https://maxroll.gg/d4/planner/cm6pf0xa#5",
    "https://maxroll.gg/d4/planner/dq1q601f#2",
    "https://maxroll.gg/d4/planner/dqih026y#3",
    "https://maxroll.gg/d4/planner/r61bp0om#11",
    "https://maxroll.gg/d4/planner/ubaoz02q#1",
]


@pytest.mark.parametrize("url", URLS)
@pytest.mark.requests()
def test_import_maxroll(url: str, mock_ini_loader: MockerFixture, mocker: MockerFixture):
    Dataloader()  # need to load data first or the mock will make it impossible
    mocker.patch("builtins.open", new=mocker.mock_open())
    import_maxroll(url=url)
