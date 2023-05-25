image bg centaurs_dwelling = 'images/scene10/centaurs_dwelling.png'

label scene10:
    
    scene bg centaurs_dwelling with fade

    'Hercules prepares to embark on his perilous journey to rescue the centaurs daughter from the clutches of Isidore. As he readies himself, a young centaur approaches, brimming with eagerness and determination.'

    show hercules at right
    show young_centaur at left
    with dissolve

    young_centaur 'Hercules, I heard of your noble quest to save my sister. I want to help you. I can be strong and brave!'

    hercules 'Young one, your bravery is commendable, but this task is perilous and fraught with danger. It is no place for one as young as you.'

    young_centaur 'Please, Hercules! I want to prove myself, to show that I can protect my family too. I promise I won\'t be a burden.'
    
    hercules 'I understand your desire to protect your family, but this is a journey that demands experience and strength beyond your years. Your family needs you here, safe and sound.'
    
    young_centaur 'I understand, Hercules. But please, promise me you will bring my sister back safely. I\'ll be waiting for her return.'
    
    hercules 'I give you my word, young centaur. Your sister\'s safety is my utmost priority. I will bring her back to your family\'s embrace, unharmed.'
    
    young_centaur 'Thank you, Hercules. May the gods watch over you on your journey.'
    
    hercules 'Stay strong, young one. Your time to shine will come. For now, protect and support your family. They need you.'

    menu:
        
        "Take the centaur to the battle":
            jump scene12
            
        "Do not take the centaur to the battle":
            jump scene11
        