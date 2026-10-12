import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()


keyboard.row_pins = (
    board.GP0,  
    board.GP1,  
    board.GP2, 
    board.GP3,  
    board.GP4,  
    board.GP5,  
    board.GP6,  
    board.GP7   
)

keyboard.col_pins = (
    board.GP8,   
    board.GP9,   
    board.GP10,  
    board.GP11, 
    board.GP12,  
    board.GP13,  
    board.GP14,  
    board.GP15   
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        # ROW 0 (Left Top)
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,
        
        # ROW 1 (Left Mid-Top)
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        
        # ROW 2 (Left Mid-Bottom)
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        
        # ROW 3 (Left Bottom)
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
        
        # ROW 4 (Right Top)
        KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.NO,   KC.MPRV, # ◁ (Prev Track)
        
        # ROW 5 (Right Mid-Top)
        KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.NO,   KC.MPLY, # ▷|| (Play/Pause)
        
        # ROW 6 (Right Mid-Bottom)
        KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,   KC.MNXT, # ▷ (Next Track)
        
        # ROW 7 (Right Bottom)
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,  KC.RALT, KC.RGUI, KC.APP,  KC.RCTL
    ]
]

if __name__ == '__main__':
    keyboard.go()
