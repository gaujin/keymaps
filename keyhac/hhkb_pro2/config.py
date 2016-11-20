import functools

def configure(keymap):
    """Keyhac Configuration for HHKB Pro2 (US Layout) on Mac OS Sierra

          .------.------.------.------.------.------.------.------.------.------.------.------.------.------.------.
Alt+Shift |      |      |      |      |      |      |      |   |  |   ~  |   {  |   }  |      |      |      |      |
Alt       |      |      |      |      |      |      |      |   \  |   `  |   [  |   ]  |      |      |      |      |
Shift     |      |   !  |   @  |   #  |   $  |   %  |   ^  |   &  |   *  |   (  |   )  |   _  |   +  |   |  |   ~  |
          |  Esc |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |   -  |   =  |   \  |   `  |
           ------^------^------^------^------^------^------^------^------^------^------^------^------^------^------ 
Alt+Shift |        |      |      |      |      |      |      |      |      |      |      |      |      |           |
Alt       |        |      |      |      |      |      |      |      |      |      |      |      |      |           |
Shift     |        |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |   {  |   }  |           |
          |  Tab   |   q  |   w  |   e  |   r  |   t  |   y  |   u  |   i  |   o  |   p  |   [  |   ]  | Backspace |
           --------^------^------^------^------^------^------^------^------^------^------^------^------^----------- 
Alt+Shift |            |      |      |      |      |      |      |      |      |      |   "  |      |              |
Alt       |            |      |      |      | PgDn |      | Left | Down |  Up  | Rght |   '  |      |              |
Shift     |            |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |   "  |              |
          |  LCtrl     |   a  |   s  |   d  |   f  |   g  |   h  |   j  |   k  |   l  |   :  |   '  |      Return  |
           ------------^------^------^------^------^------^------^------^------^------^------^------^-------------- 
Alt+Shift |               |      |      |      |      |      |      |      |      |      |      |           |      |
Alt       |               |      |      |      |      | PgUp |      |      |      |      |      |           |      |
Shift     |               |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   <  |   >  |   ?  |           |      |
          |  LShift       |   z  |   x  |   c  |   v  |   b  |   n  |   m  |   ,  |   .  |   /  |   RShift  |  Fn  |
          `---------------^------^------^------^------^------^------^------^------^------^------^-----------^------'
Alt+Shift            |      |         |                                         |         |      |
Alt                  |      |         |                                         |         |      |
Shift                |      |         |           Toggle Input Source           |         |      |
                     | LAlt |   LGui  |                  Space                  |   RGui  | RAlt |
                     `------^---------^-----------------------------------------^---------^------'
SW1:OFF
SW2:ON
SW3:ON
SW4:OFF
SW5:OFF
SW6:ON
    """

    def GUI(kc, pos=""):
        return "{0}Cmd-{1}".format(pos, kc)

    def ALT(kc, pos=""):
        return "{0}Alt-{1}".format(pos, kc)

    def SFT(kc, pos=""):
        return "{0}Shift-{1}".format(pos, kc)

    def CTL(kc, pos=""):
        return "{0}Ctrl-{1}".format(pos, kc)

    LGUI = functools.partial(GUI, pos="L")
    RGUI = functools.partial(GUI, pos="R")
    LALT = functools.partial(ALT, pos="L")
    RALT = functools.partial(ALT, pos="R")
    LSFT = functools.partial(SFT, pos="L")
    RSFT = functools.partial(SFT, pos="R")

    def LASFT(kc):
        return ALT(SFT(kc, pos="L"), pos="L")

    def RASFT(kc):
        return ALT(SFT(kc, pos="R"), pos="R")

    def remap(_keymap):

        keymap_global = keymap.defineWindowKeymap()

        for _key, _rekey in _keymap.items():

            _mod = "D-"

            if _key in ["LAlt", "RAlt", "Alt", "RCmd", "RCmd", "Cmd"]:
                _mod = "O-"

            keymap_global[_mod + _key] = _rekey

    KC_6 = "6"
    KC_7 = "7"
    KC_8 = "8"
    KC_9 = "9"
    KC_0 = "0"
    KC_F = "F"
    KC_B = "B"
    KC_H = "H"
    KC_J = "J"
    KC_K = "K"
    KC_L = "L"
    KC_EQL = "Plus"  # =
    KC_PLUS = LSFT(KC_EQL)  # +
    KC_GRV = "BackQuote"  # `
    KC_TILD = LSFT(KC_GRV)  # ~
    KC_BSLS = "Backslash",  # \
    KC_PIPE = LSFT(KC_BSLS),  # |
    KC_LBRC = "OpenBracket"  # [
    KC_RBRC = "CloseBracket"  # ]
    KC_LCBR = LSFT(KC_LBRC)  # {
    KC_RCBR = LSFT(KC_RBRC)  # }
    KC_QUOT = "Quote"  # '
    KC_SCLN = "Semicolon"  # ;
    KC_COLN = LSFT(KC_SCLN)  # :
    KC_TAB = "Tab"
    KC_LEFT = "Left"
    KC_UP = "Up"
    KC_DOWN = "Down"
    KC_RGHT = "Right"
    KC_PGUP = "PageUp"
    KC_PGDN = "PageDown"
    KC_SPC = "Space"
    KC_LANG1 = SFT(CTL(KC_J))  # Japanese Kana
    KC_LANG2 = SFT(CTL(KC_SCLN))  # Alphabet
    KC_LALT = "LAlt"
    KC_RALT = "RAlt"
    KC_LGUI = "LCmd"
    KC_RGUI = "RCmd"
    
    remap({

        LASFT(KC_7): KC_PIPE,  # |
        LALT(KC_7): KC_BSLS,  # \
        LASFT(KC_8): KC_TILD,  # ~
        LALT(KC_8): KC_GRV,  # `
        LASFT(KC_9): KC_LCBR,  # {
        LALT(KC_9): KC_LBRC,  # [
        LASFT(KC_0): KC_RCBR,  # }
        LALT(KC_0): KC_RBRC,  # ]

        RASFT(KC_F): LSFT(KC_PGDN),
        RALT(KC_F): KC_PGDN,
        LASFT(KC_H): LSFT(KC_LEFT),
        LALT(KC_H): KC_LEFT,
        LASFT(KC_J): LSFT(KC_DOWN),
        LALT(KC_J): KC_DOWN,
        LASFT(KC_K): LSFT(KC_UP),
        LALT(KC_K): KC_UP,
        LASFT(KC_L): LSFT(KC_RGHT),
        LALT(KC_L): KC_RGHT,
        LALT(KC_SCLN): KC_QUOT,
        LASFT(KC_SCLN): LSFT(KC_QUOT),

        KC_SCLN: KC_COLN,
        KC_COLN: KC_SCLN,

        RASFT(KC_B): LSFT(KC_PGUP),
        RALT(KC_B): KC_PGUP,

        SFT(KC_SPC): KC_LANG1,
    })

