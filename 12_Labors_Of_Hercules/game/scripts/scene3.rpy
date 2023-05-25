image bg tavern_outside = 'images/scene3/tavern_outside.png'
image bg tavern_intside_1 = 'images/scene3/tavern_inside_1.png'
image bg tavern_intside_2 = 'images/scene3/tavern_inside_2.png'

label scene3:

    stop sound fadeout 1
    
    scene bg tavern_outside with fade

    'After exhausting training and dialogue with Eurystheus, Hercules got hungry and decided to go to his favorite tavern for a snack.'

    scene bg tavern_intside_1 with fade

    show hercules at left
    show iolaus at right
    with dissolve

    hercules 'Iolaus! It warms my heart to see you again after all these years. May I join you?'

    iolaus 'Hercules! Of course, my friend. It\'s been far too long. Sit, sit!'

    hercules 'Ah, the memories flood back, don\'t they? The battles we fought, the triumphs we celebrated. Those were truly remarkable times.'

    iolaus 'Indeed, my friend. The victories, the camaraderie... There was a sense of invincibility when we stood together.'

    hercules 'To those days and the bond we forged. No challenge was too great when we fought side by side.'

    iolaus 'To the memories, Hercules. They will forever remain etched in my heart.'

    scene bg tavern_intside_2 with fade
    
    show hercules at left
    show iolaus at right
    with dissolve

    hercules 'Iolaus, I have been tasked with a great challenge - to slay the Hydra. I would be honored if you joined me once more, to face this danger together.'

    iolaus 'Hercules, you know I hold our memories dear. But I have found solace in a quiet life now. My days of perilous adventures are behind me.'

    hercules 'Iolaus, I understand. Life takes us on different paths. But know that the bond we share will never fade. Farewell, my friend.'

    iolaus 'Farewell, Hercules. May the gods guide you on your journey. Stay safe.'

    jump scene4