from scripts.helpful_scripts import (
    get_account,
    fund_with_link,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import time
from brownie import network
import pytest


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    # lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    # Act
    lottery.enter({"from": account, "value": lottery.getEntranceFee})
    lottery.enter({"from": account, "value": lottery.getEntranceFee})
    fund_with_link(lottery)
    lotter.endLottery({"from": account})
    time.sleep(180)
    # Assert
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
