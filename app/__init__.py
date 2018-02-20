#!/usr/bin/python
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from app.library.Database import Database

FalloutApp = Flask(__name__)
FalloutApp.config.from_object('config')

#db = Database()
# db.connect(FalloutApp)
db = SQLAlchemy(FalloutApp)

from app.api.calculators import calculators
FalloutApp.register_blueprint(calculators)


@FalloutApp.cli.command()
def initdb():
    """Initialize the database."""
    # click.echo('Init the db')
    from app.models.GameSettings import GameSettings
    from app.models.DamageResistanceSettings import DamageResistanceSettings
    from app.models.Weapon import Weapon
    from app.models.WeaponProperty import WeaponProperty
    from app.models.Slot import Slot
    from app.models.Mod import Mod
    from app.models.ModProperty import ModProperty
    # from app.models.WeaponSlot import WeaponSlot
    db.drop_all()
    db.create_all()


@FalloutApp.cli.command()
def add_weapon():
    """Add a weapon."""
    from app.models.Weapon import Weapon
    from app.models.WeaponProperty import WeaponProperty
    from app.models.Slot import Slot

    weapon = {
        'name': '10mm Pistol'
    }

    weapon_properties = {
        'damage': 18,
        'range': 83,
        'fire_rate': 46,
        'weight': 3.5,
        'accuracy': 60
    }

    slots = ['receiver', 'barrel']
    weapon_tmp = Weapon.query.filter_by(id=1).first()

    try:
        weapon_db = Weapon(name=weapon['name'])
        db.session.add(weapon_db)
        db.session.commit()
        weapon = Weapon.query.first()
        for slot in slots:
            slots_db = Slot(label=slot, category='weapon')
            db.session.add(slots_db)
            weapon.slots.append(slots_db)
        db.session.commit()
    except Exception:
        print('Weapon by the name \"{}\" already exists.'.format(
            weapon['name'])
        )
        return

    for key in weapon_properties:
        value_type = 'float' if type(
            weapon_properties[key]
        ) == int else type(weapon_properties[key]).__name__

        weapon_property_db = WeaponProperty(
            item_id=weapon.id,
            property_key=key,
            property_value=weapon_properties[key],
            value_type=value_type
        )
        db.session.add(weapon_property_db)
        db.session.commit()


@FalloutApp.cli.command()
def add_mods():
    from app.models.Weapon import Weapon
    from app.models.Slot import Slot
    from app.models.Mod import Mod
    from app.models.ModProperty import ModProperty

    mod_names = ['Automatic receiver', 'Long light ported barrel']
    mods = [{
        'prefix': 'Automatic',
        'damage': -4,
        'range': -12,
        'fire_rate': 81,
        'weight': 0.5,
        'accuracy': -12
    }, {
        'range': 36,
        'accuracy': 3
    }]

    slots = [1, 2]
    weapon = Weapon.query.filter_by(id=1).first()
    for index, value in enumerate(mod_names):
        slot = Slot.query.filter_by(id=slots[index]).first()
        mod = Mod(name=value, slot_id=slot.id, weapon_id=weapon.id)
        db.session.add(mod)
        db.session.commit()
        for key in mods[index]:
            value_type = 'float' if type(
                mods[index][key]
            ) == int else type(mods[index][key]).__name__
            modProperty = ModProperty(
                property_key=key,
                property_value=mods[index][key],
                mod_id=mod.id,
                value_type=value_type
            )

            mod.properties.append(modProperty)
        db.session.commit()


@FalloutApp.cli.command()
def mod_weapon():
    from app.library.WeaponAssembler import WeaponAssembler
    from app.models.Weapon import Weapon
    from app.models.Mod import Mod

    wa = WeaponAssembler()
    weapon_id = 1

    mods = Mod.query.filter_by(weapon_id=1).all()
    weapon = Weapon.query.filter_by(id=weapon_id).first()
    wa.set_weapon(weapon.flat_result())
    for slot in weapon.slots:
        wa.add_slot(slot.label)

    for mod in mods:
        wa.add_mod(mod.to_array())

    result = wa.assemble()
    print(result)
