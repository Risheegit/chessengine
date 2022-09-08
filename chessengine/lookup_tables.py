"""
Lookup tables are bitboards that allow us to mask or clear specific ranks, files, or positions of the chessboard
"""

pos_to_coords = {
    0: "A1",
    1: "B1",
    2: "C1",
    3: "D1",
    4: "E1",
    5: "F1",
    6: "G1",
    7: "H1",
    8: "A2",
    9: "B2",
    10: "C2",
    11: "D2",
    12: "E2",
    13: "F2",
    14: "G2",
    15: "H2",
    16: "A3",
    17: "B3",
    18: "C3",
    19: "D3",
    20: "E3",
    21: "F3",
    22: "G3",
    23: "H3",
    24: "A4",
    25: "B4",
    26: "C4",
    27: "D4",
    28: "E4",
    29: "F4",
    30: "G4",
    31: "H4",
    32: "A5",
    33: "B5",
    34: "C5",
    35: "D5",
    36: "E5",
    37: "F5",
    38: "G5",
    39: "H5",
    40: "A6",
    41: "B6",
    42: "C6",
    43: "D6",
    44: "E6",
    45: "F6",
    46: "G6",
    47: "H6",
    48: "A7",
    49: "B7",
    50: "C7",
    51: "D7",
    52: "E7",
    53: "F7",
    54: "G7",
    55: "H7",
    56: "A8",
    57: "B8",
    58: "C8",
    59: "D8",
    60: "E8",
    61: "F8",
    62: "G8",
    63: "H8",
}

coords_to_pos = {
    "A1": 0,
    "B1": 1,
    "C1": 2,
    "D1": 3,
    "E1": 4,
    "F1": 5,
    "G1": 6,
    "H1": 7,
    "A2": 8,
    "B2": 9,
    "C2": 10,
    "D2": 11,
    "E2": 12,
    "F2": 13,
    "G2": 14,
    "H2": 15,
    "A3": 16,
    "B3": 17,
    "C3": 18,
    "D3": 19,
    "E3": 20,
    "F3": 21,
    "G3": 22,
    "H3": 23,
    "A4": 24,
    "B4": 25,
    "C4": 26,
    "D4": 27,
    "E4": 28,
    "F4": 29,
    "G4": 30,
    "H4": 31,
    "A5": 32,
    "B5": 33,
    "C5": 34,
    "D5": 35,
    "E5": 36,
    "F5": 37,
    "G5": 38,
    "H5": 39,
    "A6": 40,
    "B6": 41,
    "C6": 42,
    "D6": 43,
    "E6": 44,
    "F6": 45,
    "G6": 46,
    "H6": 47,
    "A7": 48,
    "B7": 49,
    "C7": 50,
    "D7": 51,
    "E7": 52,
    "F7": 53,
    "G7": 54,
    "H7": 55,
    "A8": 56,
    "B8": 57,
    "C8": 58,
    "D8": 59,
    "E8": 60,
    "F8": 61,
    "G8": 62,
    "H8": 63,
}

clear_rank = {
    1: 18446744073709551360,
    2: 18446744073709486335,
    3: 18446744073692839935,
    4: 18446744069431361535,
    5: 18446742978492891135,
    6: 18446463698244468735,
    7: 18374967954648334335,
    8: 72057594037927935,
}

mask_rank = {
    1: 255,
    2: 65280,
    3: 16711680,
    4: 4278190080,
    5: 1095216660480,
    6: 280375465082880,
    7: 71776119061217280,
    8: 18374686479671623680,
}

clear_file = {
    1: 9187201950435737471,
    2: 13816973012072644543,
    3: 16131858542891098079,
    4: 17289301308300324847,
    5: 17868022691004938231,
    6: 18157383382357244923,
    7: 18302063728033398269,
    8: 18374403900871474942,
}

mask_file = {
    8: 9259542123273814144,
    7: 4629771061636907072,
    6: 2314885530818453536,
    5: 1157442765409226768,
    4: 578721382704613384,
    3: 289360691352306692,
    2: 144680345676153346,
    1: 72340172838076673,
}

# Maps a board position with a binary number only having a 1 at that position
# Used to check if a particular position on a bitboard is 1 or 0
mask_position = {
    2**0: 1,
    2**1: 2,
    2**2: 4,
    2**3: 8,
    2**4: 16,
    2**5: 32,
    2**6: 64,
    2**7: 128,
    2**8: 256,
    2**9: 512,
    2**10: 1024,
    2**11: 2048,
    2**12: 4096,
    2**13: 8192,
    2**14: 16384,
    2**15: 32768,
    2**16: 65536,
    2**17: 131072,
    2**18: 262144,
    2**19: 524288,
    2**20: 1048576,
    2**21: 2097152,
    2**22: 4194304,
    2**23: 8388608,
    2**24: 16777216,
    2**25: 33554432,
    2**26: 67108864,
    2**27: 134217728,
    2**28: 268435456,
    2**29: 536870912,
    2**30: 1073741824,
    2**31: 2147483648,
    2**32: 4294967296,
    2**33: 8589934592,
    2**34: 17179869184,
    2**35: 34359738368,
    2**36: 68719476736,
    2**37: 137438953472,
    2**38: 274877906944,
    2**39: 549755813888,
    2**40: 1099511627776,
    2**41: 2199023255552,
    2**42: 4398046511104,
    2**43: 8796093022208,
    2**44: 17592186044416,
    2**45: 35184372088832,
    2**46: 70368744177664,
    2**47: 140737488355328,
    2**48: 281474976710656,
    2**49: 562949953421312,
    2**50: 1125899906842624,
    2**51: 2251799813685248,
    2**52: 4503599627370496,
    2**53: 9007199254740992,
    2**54: 18014398509481984,
    2**55: 36028797018963968,
    2**56: 72057594037927936,
    2**57: 144115188075855872,
    2**58: 288230376151711744,
    2**59: 576460752303423488,
    2**60: 1152921504606846976,
    2**61: 2305843009213693952,
    2**62: 4611686018427387904,
    2**63: 9223372036854775808,
}

# Maps a board position with a binary number only having a 0 at that position.
# Used to set a particular position on a bitboard to 0
clear_position = {
    2**0: 36893488147419103230,
    2**1: 36893488147419103229,
    2**2: 36893488147419103227,
    2**3: 36893488147419103223,
    2**4: 36893488147419103215,
    2**5: 36893488147419103199,
    2**6: 36893488147419103167,
    2**7: 36893488147419103103,
    2**8: 36893488147419102975,
    2**9: 36893488147419102719,
    2**10: 36893488147419102207,
    2**11: 36893488147419101183,
    2**12: 36893488147419099135,
    2**13: 36893488147419095039,
    2**14: 36893488147419086847,
    2**15: 36893488147419070463,
    2**16: 36893488147419037695,
    2**17: 36893488147418972159,
    2**18: 36893488147418841087,
    2**19: 36893488147418578943,
    2**20: 36893488147418054655,
    2**21: 36893488147417006079,
    2**22: 36893488147414908927,
    2**23: 36893488147410714623,
    2**24: 36893488147402326015,
    2**25: 36893488147385548799,
    2**26: 36893488147351994367,
    2**27: 36893488147284885503,
    2**28: 36893488147150667775,
    2**29: 36893488146882232319,
    2**30: 36893488146345361407,
    2**31: 36893488145271619583,
    2**32: 36893488143124135935,
    2**33: 36893488138829168639,
    2**34: 36893488130239234047,
    2**35: 36893488113059364863,
    2**36: 36893488078699626495,
    2**37: 36893488009980149759,
    2**38: 36893487872541196287,
    2**39: 36893487597663289343,
    2**40: 36893487047907475455,
    2**41: 36893485948395847679,
    2**42: 36893483749372592127,
    2**43: 36893479351326081023,
    2**44: 36893470555233058815,
    2**45: 36893452963047014399,
    2**46: 36893417778674925567,
    2**47: 36893347409930747903,
    2**48: 36893206672442392575,
    2**49: 36892925197465681919,
    2**50: 36892362247512260607,
    2**51: 36891236347605417983,
    2**52: 36888984547791732735,
    2**53: 36884480948164362239,
    2**54: 36875473748909621247,
    2**55: 36857459350400139263,
    2**56: 36821430553381175295,
    2**57: 36749372959343247359,
    2**58: 36605257771267391487,
    2**59: 36317027395115679743,
    2**60: 35740566642812256255,
    2**61: 34587645138205409279,
    2**62: 32281802128991715327,
    2**63: 27670116110564327423,
}

san_piece_map = {
    'P': 'pawns',
    'K': 'kings',
    'Q': 'queens',
    'B': 'bishops',
    'N': 'knights',
    'R': 'rooks',
}
