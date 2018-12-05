#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:20:07 2018

@author: dsambugaro
"""

MAPS_DIR = 'maps'
HEROES_SPRITES_DIR = 'art/heroine'
ENEMIES_SPRITES_DIR = 'art/enemies'
OBJECTS_SPRITES_DIR = 'art/objects'

SCENARIO_SPRITES_DIR = 'art/scenario'
UI_SPRITES_DIR = 'art/interface'

TEMPLE = 'temple.tmx'

HAS_SAVE = False

# UI settings
HP_SIZE = 50
HEARTS = 5

# Weapons settings
WEAPONS = {}

WEAPONS['rusty_sword'] = {
        'damage': 1,
        'critical':0.1,
        'sprite': 'weapon_rusty_sword.png'
        }

WEAPONS['regular_sword'] = {
        'damage': 3,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

WEAPONS['regular_sword'] = {
        'damage': 3,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

# Enemies
ENEMIES = {}

ENEMIES[''] = {
        'damage': 3,
        'hp': 10,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

# Dialogs
DIALOGS = {}

DIALOGS['intro'] = [
        [
                'Você é uma guardiã. Sua vida inteira passou protegendo',
                'o Templo de Crest contra ameaças externas, e sabe que',
                'é o que vai continuar fazendo pelo resto dela. Ninguém',
                'sabe de onde você veio, e você não se lembra. Não se',
                'lembra nem do seu nome, mas os cidadãos do vilarejo de',
                'Forrest, ao pé do templo, se acostumaram a te chamar',
                'pelo seu título.'
        ],
        [
                'Uma noite frio de inverno, o vilarejo se silencia',
                'enquanto a lua sobe aos céus. As noites quietas são',
                'sempre as mais tensas, mais propícias a perturbações,',
                'o que requer vigilância constante.'
        ],
        [
                'Uma brisa gelada parece cortar o seu rosto, juntando-se',
                'às gotas de água que caem e  criam poças na terra aos',
                'seus pés. O vento aumenta, transformando-se abruptamente',
                'em uma ventania que quase te empurra pra trás, suas',
                'botas fundido-se à lama. Um brilho verde corta os céus',
                'e uma sombra parece jorrar da abertura, acompanhando',
                'algo grande e nebuloso que obscurece o brilho do luar.
        ],
        [
                 'Espada em mãos, tentando se firmar no solo molhado,',
                 'você se prepara para o impacto ao ver a sombra caindo',
                 'em sua direção, mais rápido que qualquer vento comum.',
                 'Quando se chocam, sua lâmina rubi parece arrancar um',
                 'pedaço dela, espalhando um véu de fumaça pelo pátio do',
                 'templo, e a onda de choque te arremessa contra a parede',
                 'dos portões. As portas do templo se fecham com um baque',
                 'à sua frente, você fora e a criatura dentro, ambos',
                 'machucados. Sua lâmina parece mais leve e você percebe',
                 'que ela se partiu.'
        ]
    ]

DIALOGS['entrance'] = [
        [
                '“O que raios foi aquilo? Nuvens não se movem daquele,',
                'jeito muito menos sombras. Preciso encontrá-la antes',
                'que faça mais estragos.”'
        ]
    ]

DIALOGS['first_door'] = [
        [
                'Ao se aproximar da porta, você encontra uma espada',
                'antiga de treinamento, já enferrujada, e a levanta.'
        ],
        [
                '“Acho que somos eu e você agora, minha cara. Vamos.”'
        ]
    ]

DIALOGS['first_caves'] = [
        [
                'Sua mão toca o batente da porta principal, e você sente',
                'seu corpo ser atirado para trás, um oceano de cores',
                'invade seus olhos enquanto você cai, sem saber onde',
                'fica o chão.'

        ],
        [
                '“Argh, droga de portal, Onde…? Estreito. E gelado.',
                'Ótimo. Que isso seja apenas um semi-plano, ou vai',
                'demorar até eu voltar para o Templo.”'
        ],
        [
                '“Espera, o gerador do portal deve estar por perto,',
                'Se eu encontrá-lo, consigo voltar. Com sorte.”'
        ]
    ]

DIALOGS['snow_caves'] = [
        [
                '“O que são essas criaturas? Vou ter que lutar caverna',
                'à dentro. Argh...”,
                '“De qualquer maneira, vigilância constante.”'
        ]
    ]

DIALOGS['caves_last'] = [
        [
                '“Achei você, geradorzinho. Infelizmente não tenho tempo',
                'pra te estudar, mas destruir deve dar conta.”'
        ]
    ]

DIALOGS['first_door_end'] = [
        [
                'O cristal arcano se parte em suas mãos, e você sente',
                'seu corpo ficar mais leve, enquanto o terreno ao seu',
                'redor muda, e em alguns momentos você se encontra de',
                'volta na porta do templo.'
        ],
        [
                '“Ótimo, agora para lidar com aquela coisa. Parece que',
                'foi mais fundo no Templo. O que ela quer? E melhor,',
                'o que ela é?”'
        ]
    ]

DIALOGS['castle_first'] = [
        [
                'Ao se aproximar da porta você sente sua respiração',
                'esfriar,  e sua cabeça começa a girar. Quando seus',
                'olhos se abrem, percebe que não está mais no mesmo',
                'lugar que estava antes.',
        [
                '“Mas o que…? De novo? Tá, você gosta de brincar, vou',
                'lembrar disso quando te alcançar...”'
        ],
        [
                '“Tomara que o pessoal daqui costume deixar esses túmulos',
                'abertos espalhados por aí, ou vou ter problemas muito',
                'em breve. É, lá vamos nós de novo.”'
        ]
    ]

    DIALOGS['castle_last'] = [
        [
                '“Meio labiritiano, mas não importa, encontrei o',
                'cristal. Agora para voltar...”'
        ]
    ]

DIALOGS['second_door_end'] = [
        [
                'A coloração roxa das paredes começa ser substituída',
                'pelo cinza do templo, e a porta materializada à sua',
                'frente se abre.'
        ],
        [
                '“Chega de jogos, criatura! Apareça e declare suas',
                'intenções!”'
        ],
        [
                '“Tudo bem, eu jogo o seu jogo. Só está',
                'adiando o inevitável.”'
        ]
    ]

DIALOGS['palace_first'] = [
        [
                'A porta parece tremer com seu toque e você fecha os',
                'olhos, preparada para o que vai acontecer em seguir.'
        [
                '“Pode continuar, já não surpreende mais! Tô ficando até',
                'boa nisso. Certo, esse lugar não parece tão ruim quanto',
                'os outros.”'
        ]
        [
                '“Por favor, não me amaldiçoe por ter dito',
                'isso em voz alta”''
        ]
    ]

DIALOGS['third_door_end'] = [
        [
                'Ao quebrar o cristal o portal se fecha, te levando',
                'de volta.'

        ],
        [
                '“Aquilo era sua casa? Desculpe pelo estrago. Se bem que',
                'não mudou em muito aquela bagunça. Eu posso te ouvir aí',
                'dentro, sabia? E acho que você pode me ouvir também.”',
        ]
    ]

DIALOGS['dungeon_first'] = [
        [
                'Um sentimento familiar percorre seus braços quando você',
                'encosta na porta. Algo que seca sua garganta e te faz',
                'suar frio, e você reconhece como sendo desespero.',
        [
                '“Ah, que encantador… Masmorras. Acredite ou não, eu sou',
                'bem acostumada a elas. É o que acontece quando seus',
                'piores inimigos são bruxos insanos, reis psicóticos, e',
                'habitantes da segunda camada do inferno.”'
        ],
        [
                '“Dito isso… Luar, não me deixe morrer numa masmorra.”'
        ]
    ]

DIALOGS['fourth_door_end'] = [
        [
                'As duas realidades se misturam, e as paredes do templo',
                'sobrepõem a masmorra.'
        ],
        [
                '“Quantos portais você tem, hein? Ah, não importa agora…',
                'Nenhum manipulador de realidade poderia mexer tanto com',
                'o véu sem causar rupturas indesejadas.”'
        ],
        [
                '"Então, se eu estiver certa, seus truques acabaram.'
                'Agora somos só eu e você.”'
        ]
    ]

DIALOGS['final_battle'] = [
        [
                '“Pelos poderes investidos em mim pelo Luar, eu te exilo!'
                'Volte para o buraco de onde veio e nunca mais saia!”'
        ]
    ]

# Game settings
WINDOW_RESOLUTION = (1280, 720)

# Player settings
PLAYER_VELOCITY = [0, 0]
PLAYER_MOVE_SPEED = 150
HP = 10
INVENTARY = {}
INVENTARY['weapons'] = []
INVENTARY['shields'] = []
