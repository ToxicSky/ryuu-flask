from app import FalloutApp, db


@FalloutApp.cli.command()
def initdb():
    '''Initialize the database.'''
    from app.models.GameSettings import GameSettings
    from app.models.DamageResistanceSettings import DamageResistanceSettings
    from app.models.Weapon import Weapon
    from app.models.WeaponProperty import WeaponProperty
    from app.models.Slot import Slot
    from app.models.Mod import Mod
    from app.models.ModProperty import ModProperty
    from app.models.Location import Location
    # from app.models.LocationAttribute import LocationAttribute
    # from app.models.LocationNotable import LocationNotable
    from app.models.Enemy import EnemyBase, Enemy, EnemyAttribute
    from app.models.User import User
    # from app.models.WeaponSlot import WeaponSlot
    db.create_all()


@FalloutApp.cli.command()
def dropdb():
    db.reflect()
    db.drop_all()


@FalloutApp.cli.command()
def add_weapon():
    '''Add a weapon.'''
    from app.models.Weapon import Weapon
    from app.models.WeaponProperty import WeaponProperty
    from app.models.Slot import Slot
    from app.library.utilities import get_one_or_create

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
    with db.session.no_autoflush:
        try:
            weapon_db = get_one_or_create(Weapon, weapon)

            for slot in slots:
                slots_db = get_one_or_create(
                    Slot, {'label': slot, 'category': 'weapon'}
                )
                db.session.add(slots_db)
                weapon_db.slots.append(slots_db)
            db.session.add(weapon_db)
            db.session.commit()
        except Exception:
            print('Weapon by the name \'{}\' already exists.'.format(
                weapon_db.name)
            )
            db.session.rollback()
            return
        try:
            for key in weapon_properties:
                value_type = type(weapon_properties[key]).__name__
                weapon_property_db = get_one_or_create(WeaponProperty, {
                    'property_key': key,
                    'property_value': weapon_properties[key],
                    'value_type': value_type
                })
                db.session.add(weapon_property_db)
                weapon_db.properties.append(weapon_property_db)

            db.session.commit()
        except Exception:
            db.session.rollback()


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
            value_type = type(mods[index][key]).__name__
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


@FalloutApp.cli.command()
def add_location():
    # from app.models.LocationAttribute import LocationAttribute
    # from app.models.LocationNotable import LocationNotable
    from app.models.Location import (
        Location,
        LocationAttribute,
        LocationNotable
    )
    from app.models.Enemy import EnemyBase, Enemy, EnemyAttribute
    from app.serializers.enemy_schema import EnemySchema

    enemy_base = EnemyBase(name='Molerat')
    enemy = Enemy(name='Molerat', base_id=enemy_base)
    enemy_base.variations.append(enemy)

    db.session.add(enemy_base)
    db.session.commit()

    enemy_schema = EnemySchema(
        many=False
    )
    # enemy = Enemy.query.filter_by(name='Molerat').first()

    location = Location(name='Red Rocket')
    location_attribute = LocationAttribute(zone='4,4')
    location_notable = LocationNotable(
        name='Molerat',
        notable_type='enemy',
        reference='%r' % enemy_schema.dump(enemy).data
    )

    location.attributes.append(location_attribute)
    location.notables.append(location_notable)

    db.session.add(location)
    db.session.commit()


@FalloutApp.cli.command()
def add_user():
    from app.models.User import User
    email = 'contact@example.se'
    password = bcrypt.generate_password_hash('HelloWorld!')

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
