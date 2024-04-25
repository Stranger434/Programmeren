import time, math, random
# Houd huidige kamer bij
huidige_kamer = 1
aantal_ruppees = 0
zwaard = False
schild = False
sleutel = False
Bom = False
dolk = False
BossKey = False
Balista = False

player_attack = 1
player_defense = 0
player_health = 3
# hoe maak ik een log boek met dit?


# === [kamer 1] === #
#    +++ [01] +++   #
if huidige_kamer == 1:
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je.')
    print('Je gaat naar binnen')
    print('')
    time.sleep(1)
    huidige_kamer = 7

# === [kamer 7] === #
#    +++ [07] +++   #
if huidige_kamer == 7:
    kans = random.randint(1,10)
    if kans <= 9:
        aantal_ruppees += 1
        print('je ziet een ruppee liggen')
        print('Je besluit de ruppee mee te nemen')
        
    print('Je ziet 2 deuren 1 voor je.')
    print('en de ander rechts van je.')
    print('kies een deur rechtdoor of rechts?')
    Deur = input('').lower()
    if Deur == 'rechts':
        huidige_kamer = 8
        time.sleep(1)
        print('')
    else:
        huidige_kamer = 2
        time.sleep(1)
        print('')

# === [kamer 2] === #
#    +++ [02] +++   #
if huidige_kamer == 2:
    # Pakt random 2 nummers
    getal1 = random.randint(10, 25)
    getal2 = random.randint(-5, 75)
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een ruppee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    # Kijkt of getal 2 een min getal is.
    # Als dat zo is, dan word het niet 15+-5 maar gewoon 15-5.
    if getal2 >= 0:
        print(f'Daarboven zie je een som staan {getal1}+{getal2}=?')
    else:
        print(f'Daarboven zie je een som staan {getal1}{getal2}=?')

    # Heb je de som op het Numpad goed geeft hij hier de ruppee of niet
    antwoord = int(input('Wat toest je in? '))
    if antwoord == getal1+getal2:
        print('')
        print('Het standbeeld laat de ruppee vallen en je pakt het op') 
        aantal_ruppees += 1
    else:
        print('')
        print('Er gebeurt niets....')
        print('Je hoort een geluid uit de kamer Rechtdoor van je komen')

    print('Je ziet 2 deuren 1 Rechtdoor.')
    print('en de ander naar Rechts.')
    print('kies een deur Rechtdoor of Rechts')
    Deur = input('').lower()
    if Deur == 'rechts':
        huidige_kamer = 8
        time.sleep(1)
        print('')
    else:
        huidige_kamer = 6
        time.sleep(1)
        print('')

# === [kamer 6] === #
#    +++ [06] +++   #
if huidige_kamer == 6:
    # Als je van kamer 2 naar 6 gaat kom je hieruit
    # Hier kom je een zombie tegen en word er dus uitgerekend
    # Wat de schade is die de speler krijgt en de zombie doet
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor Bob, hij kan je geen schade doen.')
    else:
        zombie_hit_damage = (zombie_attack - player_defense)
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)

        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        player_health = player_health - (player_attack_amount * zombie_attack)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} ronde(s) versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            print('De zombie heeft een sleutel laten vallen.')
            sleutel = True
            print('Je hebt de sleutel opgepakt')

        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    if antwoord == getal1+getal2:
        print('')
        print('Na het verslaan van de zombie zie je nog 2 deuren.')
        print('Een deur naar Boven en een deur naar Rechts')
        print('Kies welke deur je wilt openen.')
        print('Boven of Rechts?')
        Deur = input('').lower()
        if Deur == 'rechts':
            huidige_kamer = 8
            time.sleep(1)
            print('')
        elif Deur == 'boven':
            huidige_kamer = 3
            time.sleep(1)
            print('') 
    else:
        print('')
        print('Na het verslaan van de zombie zie je nog 3 deuren.')
        print('Een deur naar boven en een deur naar rechts')
        print('ook zie je nu een deur naar links')
        print('Kies welke deur je wilt openen.')
        print('boven / rechts / links')
        Deur = input('').lower()
        if Deur == 'rechts':
            huidige_kamer = 8
            time.sleep(1)
            print('')
        elif Deur == 'boven':
            huidige_kamer = 3
            time.sleep(1)
            print('') 
        elif Deur == 'links':
            huidige_kamer = 15
            time.sleep(1)
            print('')

# === [kamer 15] === #
#    +++ [15] +++    #
if huidige_kamer == 15:
    print('Je ziet in deze kamer een grote balista staan')
    print('Deze is gericht op de Boss')
    print('Je gebruikt de balista om de Boss te doden?')
    Balista = True
    huidige_kamer = 10


# === [kamer 8] === #
#    +++ [08] +++   #
if huidige_kamer == 8:
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer is een gokmachine')
    print(f'gokmachine werkt als volgt:')
    print(f'Er worden 2 (zeszijdige) dobbelstenen gerold.')
    print('Is het totaal meer dan 7 dan verdubbelt het aantal rupees.')
    print('Is het totaal aantal minder dan 7 dan verliest je 1 health..')
    print('Is het totaal gelijk aan 7 dan krijgt de speler 1 ruppee en 4 health.')
    print('Ga je de gokmachine gebruiken? (Ja / Nee)')
    gokmachine = input('').lower()
    if gokmachine == 'ja':
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        UitkomstGok = dobbelsteen1 + dobbelsteen2
        print(UitkomstGok)
        if UitkomstGok > 7:
            aantal_ruppees = aantal_ruppees * 2
            print(f'Je hebt {aantal_ruppees} ruppees')
        elif UitkomstGok == 7:
            aantal_ruppees += 1
            print(f'Je hebt {aantal_ruppees} ruppees')
            player_health = player_health + 4
            print(f'Je hebt {player_health} health')
        elif UitkomstGok == 0:
            print('Je hebt 0 gegooit')
            print('Game Over')
            exit()
        else:
            if UitkomstGok < 7:
                player_health = player_health - 1
                print(f'Je hebt nog maar {player_health} health')
        print('In de kamer zie je 3 deuren')
        print('een deur links een deur rechts en 1 rechtdoor')
        print('kies welke kant je op wilt')
        print('Linksboven / Rechtsboven / Rechts')
        Deur = input('').lower()
        if Deur == ('linksboven'):
            huidige_kamer = 3
        elif Deur == ('rechtsboven'):
            huidige_kamer = 9
        elif Deur == ('rechts'):
            huidige_kamer = 14
    else:
        print('In de kamer zie je 2 deuren')
        print('een deur links en een deur rechts')
        print('kies welke kant je op wilt')
        print('Linksboven / Rechtsboven / Rechts')
        Deur = input('').lower()
    if Deur == ('linksboven'):
        huidige_kamer = 3
    elif Deur == ('rechtsboven'):
        huidige_kamer = 9
    elif Deur == ('rechts'):
        huidige_kamer = 14

# === [kamer 14] === #
#    +++ [14] +++    # 
if huidige_kamer == 14:
    BossKey = True
    print('In de kamer vind je een BossKey')
    print('Met deze BossKey')
    print ('Kan je de deur naar de Boss open maken')
    print('Je ziet in de kamer ook nog een deur')
    print('en je besluit de kamer in te gaan')
    print('')
    huidige_kamer = 9


# === [kamer 9] === #
#    +++ [09] +++   #
if huidige_kamer == 9:
    print('Op deze kamer zit een betovering')
    print('als je in deze kamer komt krijg je een betovering')
    betovering = random.choice(['defence','health'])
    if betovering == 'defence':
        player_defense += 1
        print(f'De betovering is {betovering}')
        print(f'Je bent nu verdedigend met +1 defense')
        print(f'je hebt nu {player_defense} defence')
    elif betovering == 'health':
        player_health += 2
        print(f'De betovering is {betovering}')
        print(f'Je hebt +2 health gekregen')
        print(f'je hebt nu {player_health} health')
    print('Je ziet 2 deuren kies een deur')
    print('Links / Boven')
    Deur = input('').lower()
    if Deur == ('links'):
        huidige_kamer = 3
    elif Deur == ('boven'):
        huidige_kamer = 4

# === [kamer 3] === #
#    +++ [03] +++   #
if huidige_kamer == 3:
    print(f'In deze kamer zit een goblin die zijn items verkoopt voor ruppees.')
    print(f'De Goblin heeft een zwaard een schild en een sleutel in de aanbieding')
    print(f'1 ruppee per item')
    print('Met een schild krijg je +1 defense.')
    print('Met een bom kan je de houten deur openen.')
    print('Met de sleutel kan je de eind kist open maken.')
    print('Je kan alles maar 1x kopen.')
    print(f'De goblin voelt aan dat je {aantal_ruppees} ruppee(s) bij hebt')
    print(f'Met {aantal_ruppees} ruppee(s) kan je {aantal_ruppees} item kopen')

    while True:
        print('Wil je een Bom kopen?')
        item = input('').lower()
        if item == "ja":
            Bom = True
            aantal_ruppees -= 1
            if aantal_ruppees == 0:
                print('De goblin wijst je naar de volgende 2 kamers')
                print('Linksboven / Rechtsboven')
                Deur = input('').lower()
                if Deur == ('linksboven'):
                    huidige_kamer = 11
                    break
                elif Deur == ('rechtsboven'):
                    huidige_kamer = 4
                    break

        print('Wil je een schild kopen?')
        item = input('').lower()
        if item == 'ja':
            schild = True
            player_defense += 1
            aantal_ruppees -= 1
            if aantal_ruppees == 0:
                print('De goblin wijst je naar de volgende 2 kamers')
                print('Linksboven / Rechtsboven')
                Deur = input('').lower()
                if Deur == ('linksboven'):
                    huidige_kamer = 11
                    break
                elif Deur == ('rechtsboven'):
                    huidige_kamer = 4
                    break

        print('Wil je een dolk kopen?')
        item = input('').lower()
        if item == 'ja':
            dolk = True
            player_attack += 1
            aantal_ruppees -= 1
            if aantal_ruppees == 0:
                print('De goblin wijst je naar de volgende 2 kamers')
                print('Linksboven / Rechtsboven')
                Deur = input('').lower()
                if Deur == ('linksboven'):
                    huidige_kamer = 11
                    break
                elif Deur == ('rechtsboven'):
                    huidige_kamer = 4
                    break

        if dolk == True and schild == True and Bom == True:
            print("Je hebt al alle items gekocht")
            print('De goblin wijst je naar de volgende 2 kamers')
            print('Linksboven / Rechtsboven')
            Deur = input('').lower()
            if Deur == ('linksboven'):
                huidige_kamer = 11
                break
            elif Deur == ('rechtsboven'):
                    huidige_kamer = 4
                    break
        
            elif item == 'nee':
                print('De goblin wijst je naar de volgende 2 kamers')
                print('Linksboven / Rechtsboven')
                Deur = input('').lower()
                if Deur == ('linksboven'):
                    huidige_kamer = 11
                    break
                elif Deur == ('rechtsboven'):
                    huidige_kamer = 4
                    break
        
        
            

# === [kamer 11] === #
#    +++ [11] +++    #
if huidige_kamer == 11:
    print('In deze kamer komen er pijlen uit de muren')
    print('De enige manier om hier levend uit te komen')
    print('is om de pijlen te blokkeren met een schild')
    if schild == True:
        print('Gelukkig heb je een schild.')
        print('en kan je de pijlen gemakkelijk tegenhouden')
        print('Je bent aan gekomen aan de andere kant van de pijlen')
        print('er is hier een deur')
        huidige_kamer = 10
    else:
        print('Sorry, je hebt nog geen schild')
        print('je moet een schild hebben om hier doorheen te komen')
        print('Game Over')
        exit()

# === [kamer 4] === #
#    +++ [04] +++   #
if huidige_kamer == 4:
# Hier kom je Bob tegen en word er dus uitgerekend
# Wat de schade is die de speler krijgt en de Bob doet
    bob_attack = 2
    bob_defense = 0
    bob_health = 3
    print('')
    print(f'Dapper met je nieuwe items loop je de kamer binnen.')
    print('Je loopt tegen Bob aan.')

    bob_hit_damage = (bob_attack - player_defense)
    if bob_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor Bob, hij kan je geen schade doen.')
    else:
        bob_hit_damage = (bob_attack - bob_defense)
        bob_attack_amount = math.ceil(player_health / bob_hit_damage)

        player_hit_damage = (player_attack - bob_defense)
        player_attack_amount = math.ceil(bob_health / player_hit_damage)

        player_health = player_health - (player_attack_amount * bob_attack)

        if player_attack_amount < bob_attack_amount:
            print(f'In {player_attack_amount} ronde(s) versla je de bob.')
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is bob te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    print('Na het verslaan van de bob zie je 3 deuren.')
    print('Een deur naar links en naar boven')
    print('En een houten deur.')
    print('Je moet de houten deur eerst opblazen om naar binnen te kunnen')
    print('Voor de kamer naar boven heb je of een Bosskey of een Bom nodig')
    if Bom == True:
        print('Wil je je bom gebruiken?')
        Bomkeuze = input('').lower()
        if Bomkeuze == 'ja':
            print('Voor welke deur wil je de bom gebruiken')
            print('Boven / Links')
            Deur = input('').lower()
            if Deur == 'Boven':
                Bom -= 1
                huidige_kamer = 10
                print('Je hebt de BossDeur opgeblazen')
            elif Deur == 'links':
                Bom -= 1
                huidige_kamer = 13
    else:
        if BossKey == True:
            print('Wil je je BossKey gebruiken')
            KeyKeuze = input('').lower()
            if KeyKeuze == 'ja':
                BossKey -= 1
                print('Je hebt de BossDeur geopent')
                huidige_kamer = 10
            else:
                print('Je hebt niets met de sleutel gedaan')
                print('er is nog maar 1 mogelijkheid en dat is de linker deur')
                huidige_kamer = 12

        else:
            print('Je hebt geen bom en geen Bosskey')
            print('Dus kan je alleen de linker deur openen')
            huidige_kamer = 12

# === [kamer 13] === #
#    +++ [13] +++    # 
if huidige_kamer == 13:
    print('Je hebt de linker deur opgeblazen')
    print('Achter de deur is een kamer met een zwaard')
    player_attack += 2
    print(f'Je hebt nu {player_attack} attack')
    print('Je loopt weer uit de kamer en ziet weer de andere 2 deuren')
    print('Rechts / Boven')
    if BossKey == True:
        Deur = input('').lower()
        if Deur == 'boven':
            huidige_kamer = 10
        elif Deur == 'rechts':
            huidige_kamer = 12
    else:
        print('Je hebt geen bom en geen Bosskey')
        print('Dus kan je alleen de linker deur openen')
        huidige_kamer = 12

    


# === [kamer 12] === #
#    +++ [12] +++    # 
if huidige_kamer == 12:
    print('Deze kamer is een instant-death room')
    print('Oftewel')
    print('Game Over')
    exit()

# === [kamer 10] === #
#    +++ [10] +++    #
if huidige_kamer == 10:
# Hier kom je Bob tegen en word er dus uitgerekend
# Wat de schade is die de speler krijgt en de Bob doet
    
    if Balista == True:
        print(f'Het is gelukt')
        print('Je hebt de Boss gedood')
        print('Je ziet een deur in de kamer waar de boss dood ligt')
        huidige_kamer = 5

    else:
        boss_attack = 3
        boss_defense = 1
        boss_health = 5
        print(f'je gaat de kamer binnen')
        print('en loop je zo tegen de boss aan.')

        boss_hit_damage = (boss_attack - player_defense)
        player_hit_damage = (player_attack - boss_defense)
        if boss_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de boss, hij kan je geen schade doen.')

        elif player_hit_damage <= 0:
            print('De boss heeft een te goede verdedigign, jij kan hem geen schade doen.')
            print('Game Over')
            exit()
        else:
            boss_hit_damage = (boss_attack - boss_defense)
            boss_attack_amount = math.ceil(player_health / boss_hit_damage)

            player_hit_damage = (player_attack - boss_defense)
            player_attack_amount = math.ceil(boss_health / player_hit_damage)

            player_health = player_health - (player_attack_amount * boss_attack)

            if player_attack_amount < boss_attack_amount:
                print(f'In {player_attack_amount} ronde(s) versla je de bob.')
                print(f'Je health is nu {player_health}.')
            else:
                print('Helaas is de boss te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        print('Na het verslaan van de boss zie je nog een deur.')
        print('')
        huidige_kamer = 5
        time.sleep(1)


# === [kamer 5] === #
#    +++ [05] +++   #
if huidige_kamer == 5:
    print('Voorzichtig open je de deur, je wilt niet nog een boss tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    # Er wordt gecontroleerd of je de sleutel bij je hebt
    if sleutel == True:
        print('Je hebt de schatkist geopend met de sleutel en de dungeon overleeft')
        exit()
    elif Bom == True:
        print('Je hebt het slot van de schatkist eraf geblazen')
        print('Je hebt de kist geopend en de dungeon overleeft')
        exit()
    else:
        print('Je hebt de sleutel niet!')
        print('En je kan niet meer terug')
        print('Game over.')
        exit()