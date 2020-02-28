import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class DefeatRoachesBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        for unit in self.units:
            enemies = self.enemy_units
            if enemies:                
                lowest = enemies[0]
                lowest_life = lowest.health
                for roach in enemies:
                    if roach.health < lowest_life:
                        lowest = roach
                self.do(unit.attack(lowest))

run_game(maps.get("DefeatRoaches"), [
    Bot(Race.Terran, DefeatRoachesBot())
], realtime=True)