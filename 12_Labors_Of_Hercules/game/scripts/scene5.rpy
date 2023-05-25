image bg hercules_house_inside_2 = 'images/scene5/Hercules_house_inside.png'

label scene5:

    hide hera

    scene bg hercules_house_inside_2 with fade

    show hercules at left with easeinright

    'Hercules paces back and forth in his house, deep in thought after his encounter with Hera.'

    show hercules at right with easeinleft

    'He contemplates his next move, torn between two potential paths.'

    show hercules at left with easeinright
    
    hercules 'The time has come to embark on this perilous journey. But where should I begin? Isidore and his bandits in the forest, or the hunters in the village?'

    hercules 'The bandits may hold vital information, but their intentions are unclear. Isidore\'s treachery could lead to unnecessary complications.'

    hercules 'If I choose the bandits, I may have to navigate through their deception and treacherous terrain. But the rewards, the knowledge they possess, could prove invaluable.'

    hercules 'On the other hand, the hunters are skilled trackers. Their expertise in the swamps might aid me in locating the Hydra swiftly.'

    hercules 'The swamps pose their own challenges, teeming with dangerous creatures and treacherous marshes. But with the hunters\' guidance, my chances of success may increase.'

    hercules 'Consider your strengths, Hercules. Are you more inclined towards subterfuge and negotiation, or do you trust in your own skills to navigate hostile environments?'

    menu:
        
        "Go to the forest in the southwest where the bandits led by Isidore":
            jump scene7

        "Go to the village near the river in the West, which is often visited by experienced hunters":
            jump scene6
            
        

