import json
import os
from datetime import datetime


class MemoryModule:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump([], f, indent=4)

    def log_trade(self, bot_name, trade):
        trades = self.load_trades()
        trades.append({
            "timestamp": datetime.now().isoformat(),
            "bot_name": bot_name,
            **trade
        })
        self.save_trades(trades)

    def load_trades(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def save_trades(self, trades):
        with open(self.path, 'w') as f:
            json.dump(trades, f, indent=4)
