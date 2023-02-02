def get_heroes(number_heroes):
    for _ in range(number_heroes):
        current_hero = input().split()
        name, hp, mp = current_hero[0], int(current_hero[1]), int(current_hero[2])
        hero_dict[name] = [hp, mp]


def heal(hero, hp):
    hp_used = 0
    for _ in range(hp):
        if hero_dict[hero][0] == 100:
            break
        hero_dict[hero][0] += 1
        hp_used += 1
    return f"{hero} healed for {hp_used} HP!"


def recharge(hero, mana):
    mana_used = 0
    for _ in range(mana):
        if hero_dict[hero][1] == 200:
            break
        hero_dict[hero][1] += 1
        mana_used += 1
    return f"{hero} recharged for {mana_used} MP!"


def take_dmg(hero, damage, attacker):
    hero_dict[hero][0] -= damage
    if hero_dict[hero][0] > 0:
        return f"{hero} was hit for {damage} HP by {attacker} and now has {hero_dict[hero][0]} HP left!"
    else:
        del hero_dict[hero]
        return f"{hero} has been killed by {attacker}!"


def cast_spell(name, mp, spell):
    hero_dict[name][1] -= mp
    print(f"{name} has successfully cast {spell} and now has {hero_dict[name][1]} MP!")


n = int(input())
hero_dict = {}
get_heroes(n)

command = input()
while True:
    if command == 'End':
        break
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        hero, mana, spell = command[1], int(command[2]), command[3]
        if hero_dict[hero][1] >= mana:
            cast_spell(hero, mana, spell)
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")
    elif command[0] == 'TakeDamage':
        hero, damage, attacker = command[1], int(command[2]), command[3]
        print(take_dmg(hero, damage, attacker))
    elif command[0] == 'Recharge':
        hero_name, amount_mana = command[1], int(command[2])
        print(recharge(hero_name, amount_mana))
    elif command[0] == 'Heal':
        hero, amount_hp = command[1], int(command[2])
        print(heal(hero, amount_hp))

    command = input()

for hero_alive in hero_dict.keys():
    print(f"{hero_alive}\n  HP: {hero_dict[hero_alive][0]}\n  MP: {hero_dict[hero_alive][1]}")
