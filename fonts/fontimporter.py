# 20251115


fontlines = """^^p.AssassinS-ttf {font-family: 'AssassinS-ttf';}^^p.bilbobold-ttf {font-family: 'bilbobold-ttf';}^^p.bilbofine-ttf {font-family: '';}^^p.bilboregular-ttf {font-family: '';}^^p.BTTF-ttf {font-family: '';}^^p.Clicky-Bricks-otf {font-family: '';}^^p.clicky-bricks-2-outlines-ttf {font-family: '';}^^p.clicky-bricks-2-ttf {font-family: '';}^^p.Daedra-Bold-Italic-otf {font-family: '';}^^p.Daedra-Bold-otf {font-family: '';}^^p.Daedra-Italic-otf {font-family: '';}^^p.Daedra-otf {font-family: 'Daedra-otf';}^^p.Dovahkiin-Bold-Italic-otf {font-family: '';}^^p.Dovahkiin-Bold-otf {font-family: '';}^^p.Dovahkiin-Italic-otf {font-family: '';}^^p.Dovahkiin-otf {font-family: '';}^^p.Dune_Rise-otf {font-family: '';}^^p.Dune_Rise-ttf {font-family: '';}^^p.Game-Of-Squids-otf {font-family: '';}^^p.Game-Of-Squids-ttf {font-family: '';}^^p.Halo-Outline-ttf {font-family: '';}^^p.Halo-ttf {font-family: '';}^^p.HandwrittenSheikahRunes-Regular_MAC-ttf {font-family: '';}^^p.HandwrittenSheikahRunes-Regular-otf {font-family: '';}^^p.HandwrittenSheikahRunes-Regular-ttf {font-family: '';}^^p.harry_potter_and_the_dingbat_font-ttf {font-family: '';}^^p.HARRYP__-TTF {font-family: '';}^^p.hobbitonbrushhand-ttf {font-family: '';}^^p.Indiana-Jonas-48ip-otf {font-family: '';}^^p.Indiana-Jonas-48p-otf {font-family: '';}^^p.Medieval-Scroll-of-Wisdom-ttf {font-family: '';}^^p.Nasalization-Rg-otf {font-family: '';}^^p.Overseer-Bold-Italic-otf {font-family: '';}^^p.Overseer-Bold-otf {font-family: '';}^^p.Overseer-Italic-otf {font-family: '';}^^p.Overseer-otf {font-family: '';}^^p.Pirate-Scroll-otf {font-family: '';}^^p.SEGA-TTF {font-family: '';}^^p.SoleSurvivor-ttf {font-family: '';}^^p.SoleSurvivorRegular-ttf {font-family: '';}^^p.space-age-ttf {font-family: '';}^^p.Square-Game-otf {font-family: '';}^^p.Star-Trek-Enterprise-Future-ttf {font-family: '';}^^p.Star-Trek_future-ttf {font-family: '';}^^p.tngan-ttf {font-family: '';}^^p.tnganb-ttf {font-family: '';}^^p.tnganbi-ttf {font-family: '';}^^p.tngani-ttf {font-family: '';}^^p.Transformers-Movie-ttf {font-family: '';}^^p.VIKING-N-TTF {font-family: '';}"""

fontlines = fontlines.split('^^')

for q in fontlines:
    dot = q.find('.')
    space = q.find(' ')
    font_name = q[dot+1:space]
    insertion_point = q.find("'") + 1

    new_q = q[:insertion_point] + font_name + "';}\n"

    #importation
    font_url = font_name[:-4]+'.'+font_name[-3:]
    
    importation = '@font-face {\n  font-family: ' + f"'{font_name}';\n  src: url('/fonts/{font_url}') format('truetype'" + ');}'

    print(importation)
    print(new_q)