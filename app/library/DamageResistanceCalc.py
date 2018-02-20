from app.models.DamageResistanceSettings import DamageResistanceSettings
import math


class DamageResistanceCalc:
    coeff = 0
    fPhysicalDamageFactor = 0
    fPhysicalArmorDmgReductionExp = 0.365
    target = 'player'

    def set_target(self, target='player'):
        self.target = target

    def calc_coeff(self, damage, damage_resist):
        if float(damage) <= 0:
            damage = 1
        if float(damage_resist) <= 0:
            damage_resist = 1

        damage = float(damage)
        resist = damage / float(damage_resist) * 0.15
        result = min([0.99, resist ** 0.365]) * self.fPhysicalDamageFactor

        damage_coeff = 1 - result
        calc = damage * damage_coeff

        return round(damage - calc)

    def set_difficulty(self, difficulty_name):
        difficulty_levels = [
            {'name': 'very_easy', 'p_damage': 2.0,  'e_damage': 0.5},
            {'name': 'easy',      'p_damage': 1.5,  'e_damage': 0.75},
            {'name': 'normal',    'p_damage': 1.0,  'e_damage': 1.0},
            {'name': 'hard',      'p_damage': 0.75, 'e_damage': 1.5},
            {'name': 'very_hard', 'p_damage': 0.5,  'e_damage': 2.0},
            {'name': 'survival',  'p_damage': 4.75, 'e_damage': 4.0}
        ]

        opted_difficulty = None
        for difficulty in difficulty_levels:
            if difficulty['name'] == difficulty_name:
                opted_difficulty = difficulty

        if self.target == 'player':
            sel_target = 'e_damage'
        elif self.target == 'enemy':
            sel_target = 'p_damage'

        if (opted_difficulty != None):
            self.fPhysicalDamageFactor = opted_difficulty[sel_target]
        else:
            self.fPhysicalDamageFactor = 1
