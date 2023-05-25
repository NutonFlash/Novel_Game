image bg forest_1 = 'images/scene7/forest_1.png'
image bg forest_2 = 'images/scene7/forest_2.png'
image bg forest_3 = 'images/scene7/forest_3.png'

label scene7:

    scene bg forest_1 with fade

    play sound 'forest_sounds.mp3' volume 0.2 loop

    'Hercules ventures into the forest, the air thick with the scent of pine and earth.'

    'As he walks, the growling of his empty stomach compels him to seek sustenance.'

    show hercules with dissolve

    hercules 'I must find sustenance to replenish my energy. A successful hunt shall provide the nourishment I require.'

    show hercules at left with easeinleft
    show deer at right with dissolve
    
    stop sound fadeout 1.0

    deer '"rustling in the bushes, a cautious glance towards Hercules"'

    hercules 'A deer. Swift and agile. It shall be my prey.'

    deer '"sensing danger, it starts to flee, bounding through the forest"'

    play sound 'deer_running.mp3' volume 0.2

    show deer at offscreenright with easeinright

    scene bg forest_2 with fade 

    show hercules at left with dissolve
    show deer at right with easeinright

    stop sound fadeout .5

    hercules 'You will not escape, dear deer! Your flesh shall provide sustenance to fuel my quest!'

    deer '"darting through the underbrush, its hooves thumping against the ground"'

    hercules 'I am Hercules, unmatched in strength and agility. I will capture you, dear deer!'

    deer '"leaping gracefully, its movements blending with the rhythm of the forest"'
    
    play sound 'deer_running.mp3' volume 0.2
    
    show deer at offscreenright with easeinright

    scene bg forest_3 with fade
    
    show hercules at left
    show deer
    with dissolve

    stop sound fadeout 0.5
    
    hercules 'I am closing in! Your fate is sealed, dear deer!'

    deer '"with a final burst of speed, it vanishes deeper into the forest, eluding Hercules"'
    
    play sound 'deer_running.mp3' volume 0.2
    
    show deer at offscreenright with easeinright

    stop sound fadeout 0.5

    jump scene8