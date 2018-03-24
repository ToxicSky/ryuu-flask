
class WeaponAssembler:
    mods = []
    slots = []
    slots_taken = []
    weapon = {}

    # Sets the default weapon values.
    def set_weapon(self, weapon):
        self.weapon = weapon

    # Add a slot to the weapon.
    def add_slot(self, slot):
        self.slots.append(slot)

    # Add a mod to weapon.
    def add_mod(self, mod):
        self.mods.append(mod)

    # Assembles all parts and generates the values.
    def assemble(self):
        result = {}
        name = ''
        prefix = ''
        suffix = ''

        for key in self.weapon:
            result[key] = self.weapon[key]

        for mod in self.mods:
            if not self.free_slot(mod['slot']):
                continue
            for key in mod:
                value = mod[key]
                if not isinstance(value, (int, float)):
                    continue
                if key in self.weapon:
                    try:
                        result[key] += value
                    except Exception:
                        return
            if 'prefix' in mod:
                prefix += mod['prefix'] + ' '
            if 'suffix' in mod:
                suffix += ' ' + mod['suffix']
        name = prefix + self.weapon['name'] + suffix
        result['name'] = name
        return result

    # Checks wether the weapon has a free slot for the mod.
    def free_slot(self, slot=''):
        if slot in self.slots and not slot in self.slots_taken:
            self.slots_taken.append(slot)
            return True
        return False
