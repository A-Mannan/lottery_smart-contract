from http.client import NETWORK_AUTHENTICATION_REQUIRED
from brownie import network
import pytest
from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.deploy import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    account = get_account()
    lottery = deploy_lottery()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(240)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
