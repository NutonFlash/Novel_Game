define hercules = Character('Hercules', who_color='#E2C717')
define iolaus = Character('Iolaus', who_color='#1798E2')
define zeus = Character('Zeus', who_color='#0039D7')
define arms_dealer = Character('Arms Dealer', who_color='#2ADE3C')
define eurystheus = Character('Eurystheus', who_color='#902ADE')
define hunter = Character('Surviving Hunter', who_color='#18D476')
define deer = Character('Deer', who_color='#D41876')
define centaur_father = Character('Centaur Father', who_color='#1798E2')
define centaur_mother = Character('Centaur Mother', who_color='#2ADE3C')
define young_centaur = Character('Young Centaur', who_color='#D41876')
define isidore = Character('Isidore', who_color='#FF0E0E')
define hydra = Character('Hydra', who_color='#FF0E0E')
define hera = Character('Hera', who_color='#FF0E0E')
define bandits = Character('Bandits', who_color='#FF0E0E')

image hercules = 'images/characters/Hercules.png'
image iolaus = 'images/characters/Iolaus.png'
image zeus = 'images/characters/Zeus.png'
image arms_dealer = 'images/characters/arms_dealer.png'
image eurystheus = 'images/characters/Eurystheus.png'
image hunter = 'images/characters/hunter.png'
image deer = 'images/characters/deer.png'
image centaur_father = 'images/characters/centaur_father.png'
image centaur_mother = 'images/characters/centaur_mother.png'
image young_centaur = 'images/characters/young_centaur.png'
image isidore = 'images/characters/Isidore.png'
image hydra = 'images/characters/hydra.png'
image hera = 'images/characters/Hera.png'

transform left_for_200:
    yanchor -.35
    xoffset 200

transform left_for_350:
    yanchor -.35
    xoffset 350


label start:
    jump scene0