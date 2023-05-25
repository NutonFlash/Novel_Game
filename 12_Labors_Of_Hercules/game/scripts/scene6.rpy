image bg village_outside = 'images/scene6/village_outside.png'
image bg village_inside = 'images/scene6/village_inside.png'

label scene6:

    scene bg village_outside with fade

    play sound 'village_in_fire.mp3' volume 0.05 loop

    'Following Eurystheus directions, Hercules makes his way to the village of the hunters, a place once teeming with life and prosperity.'

    'However, the aftermath of a Hydra\'s rampage has left the village in a state of despair.'

    stop sound fadeout 1.0
    
    scene bg village_inside with fade
    
    show hercules at left with dissolve

    hercules 'This must be the village Eurystheus mentioned. The Hydra\'s wrath has taken its toll. I must find someone who can shed light on the creature\'s whereabouts.'

    show hunter at right with dissolve

    hunter 'Stranger, what brings you to our ravaged village? Have you come to witness the aftermath of the Hydra\'s fury?'

    hercules 'I am Hercules, and I have been sent here by Eurystheus to face the Hydra. Tell me, what transpired here?'

    hunter 'Just a few days ago, the Hydra descended upon our village. It devoured our livestock and left our homes in ruins. We barely managed to escape with our lives.'

    hercules 'I am here to end the Hydra\'s reign of terror. Can you guide me to its lair? Where did it disappear after the attack?'

    hunter 'The Hydra\'s tracks led deep into the forest, to the east. Be warned, Hercules, for the creature is cunning and dangerous. But I have faith in your strength and bravery.'

    hercules 'Thank you for your guidance. I will do everything in my power to bring an end to this menace and restore peace to your village. Stay safe, and may the gods watch over you.'

    hunter 'May the gods grant you victory, Hercules. May your path be paved with triumph and the Hydra\'s threat be vanquished.'

    jump scene7