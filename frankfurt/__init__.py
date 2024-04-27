from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *


def show_card_count() -> None:
    card_count = mw.col.cardCount()
    showInfo("Card count: %d" % card_count)


action = QAction("Show Card Count", mw)
qconnect(action.triggered, show_card_count)
mw.form.menuTools.addAction(action)
