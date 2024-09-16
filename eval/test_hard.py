"""100 hard cases proposed in:
ELLA-V: Stable Neural Codec Language Modeling with Alignment-guided Sequence Reordering
Each sentence paired with a 3 second prompt.
"""

test_set = [
    (
        0,
        "1089_134686_000032_000008",
        "Active artists always appreciate artistic achievements and applaud awesome artworks.",
    ),
    (
        1,
        "1188_133604_000026_000001",
        "Brave bakers boldly baked big batches of brownies in beautiful bakeries.",
    ),
    (
        2,
        "121_127105_000037_000000",
        "Clever cats carefully crafted colorful collages, creating cheerful compositions.",
    ),
    (
        3,
        "1284_1180_000044_000001",
        "Daring dancers dazzled during dynamic dance displays, drawing delighted crowds.",
    ),
    (
        4,
        "1320_122617_000033_000000",
        "Excited engineers eagerly enjoyed exploring enormous engineering exhibits.",
    ),
    (
        5,
        "1580_141083_000019_000001",
        "Friendly farmers faithfully fostered fields, favoring fruitful crops.",
    ),
    (
        6,
        "1995_1837_000020_000000",
        "Gallant gophers gracefully gambled golden gooseberries on grandiose glaciers.",
    ),
    (
        7,
        "2300_131720_000016_000004",
        "Happy hikers harmoniously hiked through hilly landscapes on heavenly holidays.",
    ),
    (
        8,
        "237_134493_000015_000004",
        "Inquisitive individuals ingeniously invented innovative inventions.",
    ),
    (
        9,
        "260_123288_000019_000001",
        "Jovial joggers joyfully joined jogging jaunts, justifying joyful jolliness.",
    ),
    (
        10,
        "2830_3980_000018_000001",
        "Keen kids keenly knitted knotted knots in kindergartens.",
    ),
    (
        11,
        "2961_961_000004_000007",
        "Lively librarians lazily leafed through large literary collections.",
    ),
    (
        12,
        "3570_5694_000009_000002",
        "Merry musicians melodiously meandered through memorable melodies.",
    ),
    (
        13,
        "3575_170457_000029_000000",
        "Nifty nurses navigated nearby neighborhoods, noting necessary nuances.",
    ),
    (
        14,
        "3729_6852_000040_000002",
        "Optimistic office workers openly observed office occurrences, offering opinions.",
    ),
    (
        15,
        "4077_13754_000013_000005",
        "Playful puppies passionately played, producing playful puppy pandemonium.",
    ),
    (
        16,
        "4446_2271_000011_000001",
        "Quick quilters quietly quilted quality quilts, quickly quelling queries.",
    ),
    (
        17,
        "4507_16021_000036_000001",
        "Radiant readers radiantly recited rhythmic rhymes, receiving round applause.",
    ),
    (
        18,
        "4970_29093_000050_000008",
        "Silly siblings silently signaled silly signals, sparking silly scenarios.",
    ),
    (
        19,
        "4992_23283_000004_000000",
        "Tenacious teachers tirelessly taught tricky topics, taking time to tutor.",
    ),
    (
        20,
        "5105_28241_000002_000000",
        "Unwavering umpires upheld umpiring rules, understanding umpire responsibilities.",
    ),
    (
        21,
        "5142_33396_000006_000001",
        "Vivacious volunteers voraciously volunteered, validating valuable ventures.",
    ),
    (
        22,
        "5639_40744_000027_000004",
        "Witty writers wittily wrote whimsical words, weaving wonderful worlds.",
    ),
    (
        23,
        "5683_32866_000047_000003",
        "Xylophone xylophonists expertly executed exciting xylophone exhibitions.",
    ),
    (
        24,
        "672_122797_000002_000002",
        "Young yogis yearned for yogic yearning, yielding youthful yawns.",
    ),
    (
        25,
        "6829_68771_000046_000000",
        "Zany zookeepers zealously zipped through zoos, zealously zeroing in on zebras.",
    ),
    (
        26,
        "6930_75918_000032_000001",
        "Adventurous ants anxiously ate apples, adventurous adventurous apples.",
    ),
    (
        27,
        "7021_79730_000047_000001",
        "Playful pandas prattled playfully, playful playfully peaches.",
    ),
    (
        28,
        "7127_75946_000027_000000",
        "Colorful cats cheerfully chased colorful colorful critters.",
    ),
    (
        29,
        "7176_92135_000083_000005",
        "Confused canines clumsily crunched confused confused cookies.",
    ),
    (
        30,
        "7729_102255_000002_000001",
        "Expressive eagles elegantly echoed expressive expressive echoes.",
    ),
    (
        31,
        "8224_274384_000017_000000",
        "Silly squirrels stumbled stumblingly, silly silly feathers.",
    ),
    (32, "8230_279154_000004_000008", "Happy horses happily hopped, happy happy hops."),
    (
        33,
        "8455_210777_000067_000000",
        "Clumsy cats carelessly caught clumsy clumsy butterflies.",
    ),
    (
        34,
        "8463_294825_000050_000000",
        "Mixed-up mice munched mixed-up mixed-up muffins.",
    ),
    (
        35,
        "8555_284449_000044_000000",
        "Curious koalas curiously climbed curious curious climbers.",
    ),
    (
        36,
        "908_157963_000010_000001",
        "Chatty chipmunks chatted chattily, chatty chatty chats.",
    ),
    (37, "1089_134686_000032_000008", "Sad snakes sadly sighed sad sad sighs."),
    (
        38,
        "1188_133604_000026_000001",
        "Funny ferrets fumbled fumblingly, funny funny feathers.",
    ),
    (
        39,
        "121_127105_000037_000000",
        "Excited elephants excitedly explored excited excited explorations.",
    ),
    (
        40,
        "1284_1180_000044_000001",
        "Confused crabs confusedly cracked confused confused crab cakes.",
    ),
    (
        41,
        "1320_122617_000033_000000",
        "Joyful jaguars joyfully jumped joyful joyful jumps.",
    ),
    (
        42,
        "1580_141083_000019_000001",
        "Lost lions lazily lounged lost lost landscapes.",
    ),
    (
        43,
        "1995_1837_000020_000000",
        "Noisy newts nonsensically nibbled noisy noisy nibbles.",
    ),
    (
        44,
        "2300_131720_000016_000004",
        "Eager otters eagerly overcame eager eager obstacles.",
    ),
    (
        45,
        "237_134493_000015_000004",
        "Puzzled penguins puzzledly pondered puzzled puzzled ponderings.",
    ),
    (
        46,
        "260_123288_000019_000001",
        "Quaint quokkas quietly questioned quaint quaint queries.",
    ),
    (
        47,
        "2830_3980_000018_000001",
        "Restless rabbits rambled restlessly, restless restless radishes.",
    ),
    (
        48,
        "2961_961_000004_000007",
        "Happy hummingbirds happily hovered, happy happy hums.",
    ),
    (49, "3570_5694_000009_000002", "Crazy cats crazily cavorted crazy crazy cavorts."),
    (
        50,
        "3575_170457_000029_000000",
        "Worried walruses worriedly waddled, worried worried waddles.",
    ),
    (
        51,
        "3729_6852_000040_000002",
        "Xenial xenophobes xenially xeroxed xenial xenial xylophones.",
    ),
    (
        52,
        "4077_13754_000013_000005",
        "Yearning yaks yawned yearningly, yearning yearning yawns.",
    ),
    (53, "4446_2271_000011_000001", "Zany zebras zanily zigzag, zany zany zigzag."),
    (54, "4507_16021_000036_000001", "l l l l l l b v p d s s s s s l"),
    (
        55,
        "4970_29093_000050_000008",
        "forty five to five hundred and eleven Fail - one to zero Cancelled - zero - zero Total",
    ),
    (
        56,
        "4992_23283_000004_000000",
        "two thousand two hundred twenty two happily happy two hundred and twenty-two",
    ),
    (57, "5105_28241_000002_000000", "g 2 p 2 g 2 p 2 g 2 p 2 p 2 p"),
    (58, "5142_33396_000006_000001", "F 1 F 2 F 4 F 8 H 16 H 32 H 64"),
    (
        59,
        "5639_40744_000027_000004",
        "Amidst the towering skyscrapers, the bustling cityscape echoed with the incessant hum hum hum hum hum of commerce and ambition.",
    ),
    (
        60,
        "5683_32866_000047_000003",
        "As the ancient ancient ancient ancient ancient ancient manuscript was deciphered, the archaeologist unearthed a trove of forgotten forgotten forgotten forgotten forgotten forgotten wisdom embedded in in in in in in the crumbling parchment.",
    ),
    (
        61,
        "672_122797_000002_000002",
        "As the cosmic cosmic cosmic cosmic cosmic cosmic dance of the stars unfolds in in in in in in silence, revealing the mystical mysteries of the celestial celestial celestial celestial celestial celestial realm.",
    ),
    (
        62,
        "6829_68771_000046_000000",
        "As the quantum physicist delved into the quantum realm, the enigmatic entanglement of particles perplexed even the most astute astute astute astute astute astute minds.",
    ),
    (
        63,
        "6930_75918_000032_000001",
        "Beneath the celestial canopy, the twinkling stars whispered tales of timeless timelessness and cosmic conspiracies.",
    ),
    (
        64,
        "7021_79730_000047_000001",
        "Beneath the moonlit night, the solitary wolf’s haunting howl howl howl howl howl echoed through the ancient forest, embodying the primal spirit of the wilderness.",
    ),
    (
        65,
        "7127_75946_000027_000000",
        "Beneath the shimmering sheen of the silken fabric fascinated the fashionistas, creating a cacophony of compliments.",
    ),
    (
        66,
        "7176_92135_000083_000005",
        "Coding in in in in in in solitude, the programmer uncovered the intricate intricacies of the algorithm, unveiling a hidden hidden hidden layer of complexity.",
    ),
    (
        67,
        "7729_102255_000002_000001",
        "Crafting a symphony of flavors, the skilled chef orchestrated a culinary masterpiece that left an indelible mark mark mark mark mark on the palates of the discerning diners.",
    ),
    (
        68,
        "8224_274384_000017_000000",
        "Delving into the dense foliage, the intrepid explorer uncovered the cryptic trail trail trail trail trail leading to an undiscovered waterfall deep in the heart of the jungle.",
    ),
    (
        69,
        "8230_279154_000004_000008",
        "In the bustling bustling bustling bustling bustling bustling metropolis, the rhythmic rhythm of life beats to the pulsating pulsating pulsating pulsating pulsating heartbeat of the city streets.",
    ),
    (
        70,
        "8455_210777_000067_000000",
        "In the enigmatic enigmatic enigmatic enigmatic enigmatic enigmatic maze, the elusive solution remained hidden behind layers of intricate intricacies.",
    ),
    (
        71,
        "8463_294825_000050_000000",
        "In the realm of robotics, replicating the nuanced nuances of human emotions remains a formidable formidable formidable formidable formidable challenge.",
    ),
    (
        72,
        "8555_284449_000044_000000",
        "In the timeless tapestry of the galaxy, the mesmerizing dance dance dance dance dance of celestial bodies unveiled the cosmic secrets of the universe.",
    ),
    (
        73,
        "908_157963_000010_000001",
        "In the vast vast vast vast vast vast landscape of knowledge, the voracious voracious voracious voracious voracious voracious reader explored the depths of literature, extracting pearls of wisdom hidden within within within within within within the pages.",
    ),
    (
        74,
        "1089_134686_000032_000008",
        "Navigating through through through through through through the dense forest, the intrepid explorer discovered an ancient ancient ancient ancient ancient ancient relic buried beneath layers of thick underbrush.",
    ),
    (
        75,
        "1188_133604_000026_000001",
        "Navigating through the labyrinthine labyrinthine labyrinthine labyrinthine labyrinthine labyrinthine code, the programmer discovered an elusive bug.",
    ),
    (
        76,
        "121_127105_000037_000000",
        "Precision in decision-making is paramount, as an error could cost countless countless countless countless countless countless countless lives.",
    ),
    (
        77,
        "1284_1180_000044_000001",
        "Strategically strategizing strategy in the fast-paced world of e-sports demands a dexterous dexterous dexterous dexterous dexterous dexterous mind.",
    ),
    (
        78,
        "1320_122617_000033_000000",
        "The clandestine clandestine clandestine clandestine clandestine clandestine mission required a meticulous analysis of encrypted encryptions and covert communications.",
    ),
    (
        79,
        "1580_141083_000019_000001",
        "The entrepreneur, driven by an insatiable insatiable insatiable insatiable insatiable desire for success, embarked on a journey filled with challenges, challenges, challenges, challenges, challenges, challenges, and triumphs.",
    ),
    (
        80,
        "1995_1837_000020_000000",
        "The hypnotic sway sway sway sway sway of the pendulum clock echoed through the dimly lit room, creating an atmosphere of temporal contemplation.",
    ),
    (
        81,
        "2300_131720_000016_000004",
        "The relentless relentless relentless relentless relentless relentless pursuit of perfection in in in in in in in in in craftsmanship led the artisan to create an exquisite masterpiece admired for its meticulous meticulous meticulous meticulous meticulous meticulous details.",
    ),
    (
        82,
        "237_134493_000015_000004",
        "The resounding echoes of the ancient drums resonated through the cavern, revealing the sacred rhythm rhythm rhythm rhythm rhythm of the hidden rituals.",
    ),
    (
        83,
        "260_123288_000019_000001",
        "The shimmering sheen of the silken fabric fascinated the fashionistas, creating a cacophony of compliments.",
    ),
    (
        84,
        "2830_3980_000018_000001",
        "Theoretical thespians theatrically theorized thematic thesauri theses.",
    ),
    (
        85,
        "2961_961_000004_000007",
        "Through the misty morning, the distant call call call call call of migratory birds echoed, heralding the arrival of the changing seasons.",
    ),
    (
        86,
        "3570_5694_000009_000002",
        "Within the labyrinthine corridors, the footsteps footsteps footsteps footsteps footsteps of the inquisitive investigator echoed, unraveling the enigma of the haunted mansion.",
    ),
    (
        87,
        "3575_170457_000029_000000",
        "A journey of a thousand miles begins begins begins begins begins with a single step. Step by step, step by step, step by step, progress is made.",
    ),
    (
        88,
        "3729_6852_000040_000002",
        "The impact of technology on society is society is society is society is society is profound. Profound Profound Profound Profound Consideration of consequences is imperative in technological innovation.",
    ),
    (
        89,
        "4077_13754_000013_000005",
        "The future belongs to belongs to belongs to belongs to belongs to those who believe in the beauty of the beauty of the beauty of the beauty of the beauty of their dreams.",
    ),
    (
        90,
        "4446_2271_000011_000001",
        "Silence is a source of great strength. Strength lies in lies in lies in lies in inner resilience.",
    ),
    (
        91,
        "4507_16021_000036_000001",
        "In the realm of possibilities, possibilities, possibilities, possibilities, possibilities, the only limitation is imagination.",
    ),
    (
        92,
        "4970_29093_000050_000008",
        "Learning from mistakes is is is is is is a crucial part of the journey to success.",
    ),
    (
        93,
        "4992_23283_000004_000000",
        "Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop not to stop not to stop not to stop not to stop questioning.",
    ),
    (
        94,
        "5105_28241_000002_000000",
        "Creativity is intelligence is intelligence is having fun. The only limit to our realization of tomorrow is our doubts of today.",
    ),
    (
        95,
        "5142_33396_000006_000001",
        "In the world of technology, the only constant is the only constant is the only constant is change. Change is inevitable, but progress is optional.",
    ),
    (
        96,
        "5639_40744_000027_000004",
        "The best way to predict the best way to predict the future is to create it, but sometimes, the best way to predict the future is to prevent it.",
    ),
    (
        97,
        "5683_32866_000047_000003",
        "Life is like a bicycle, to keep your balance, you must keep moving keep moving keep moving keep moving keep moving. The more you know, the more you realize you don’t know, but knowing that you don’t know is the beginning of wisdom.",
    ),
    (
        98,
        "672_122797_000002_000002",
        "The early bird gets the early bird gets the early bird gets the worm, but the second mouse gets the worm, but the second mouse gets the cheese.",
    ),
    (
        99,
        "6829_68771_000046_000000",
        "Communication is the key to success. Success breeds success breeds success breeds success breeds success.",
    ),
]
