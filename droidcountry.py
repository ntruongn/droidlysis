#!/usr/bin/env python

"""
__author__ = "Axelle Apvrille"
__status__ = "Alpha"
__license__ = "MIT License"
"""
country = {'af': 0,
           'ax': 1,
           'al': 2,
           'dz': 3,
           'as': 4,
           'ad': 5,
           'ao': 6,
           'ai': 7,
           'aq': 8,
           'ag': 9,
           'ar': 10,
           'am': 11,
           'aw': 12,
           'au': 13,
           'at': 14,
           'az': 15,
           'bs': 16,
           'bh': 17,
           'bd': 18,
           'bb': 19,
           'by': 20,
           'be': 21,
           'bz': 22,
           'bj': 23,
           'bm': 24,
           'bt': 25,
           'bo': 26,
           'bq': 27,
           'ba': 28,
           'bw': 29,
           'bv': 30,
           'br': 31,
           'io': 32,
           'bn': 33,
           'bg': 34,
           'bf': 35,
           'bi': 36,
           'kh': 37,
           'cm': 38,
           'ca': 39,
           'cv': 40,
           'ky': 41,
           'cf': 42,
           'td': 43,
           'cl': 44,
           'cn': 45,
           'cx': 46,
           'cc': 47,
           'co': 48,
           'km': 49,
           'cg': 50,
           'cd': 51,
           'ck': 52,
           'cr': 53,
           'ci': 54,
           'hr': 55,
           'cu': 56,
           'cw': 57,
           'cy': 58,
           'cz': 59,
           'dk': 60,
           'dj': 61,
           'dm': 62,
           'do': 63,
           'ec': 64,
           'eg': 65,
           'sv': 66,
           'gq': 67,
           'er': 68,
           'ee': 69,
           'et': 70,
           'fk': 71,
           'fo': 72,
           'fj': 73,
           'fi': 74,
           'fr': 75,
           'gf': 76,
           'pf': 77,
           'tf': 78,
           'ga': 79,
           'gm': 80,
           'ge': 81,
           'de': 82,
           'gh': 83,
           'gi': 84,
           'gr': 85,
           'gl': 86,
           'gd': 87,
           'gp': 88,
           'gu': 89,
           'gt': 90,
           'gg': 91,
           'gn': 92,
           'gw': 93,
           'gy': 94,
           'ht': 95,
           'hm': 96,
           'va': 97,
           'hn': 98,
           'hk': 99,
           'hu': 100,
           'is': 101,
           'in': 102,
           'id': 103,
           'ir': 104,
           'iq': 105,
           'ie': 106,
           'im': 107,
           'il': 108,
           'it': 109,
           'jm': 110,
           'jp': 111,
           'je': 112,
           'jo': 113,
           'kz': 114,
           'ke': 115,
           'ki': 116,
           'kp': 117,
           'kr': 118,
           'kw': 119,
           'kg': 120,
           'la': 121,
           'lv': 122,
           'lb': 123,
           'ls': 124,
           'lr': 125,
           'ly': 126,
           'li': 127,
           'lt': 128,
           'lu': 129,
           'mo': 130,
           'mk': 131,
           'mg': 132,
           'mw': 133,
           'my': 134,
           'mv': 135,
           'ml': 136,
           'mt': 137,
           'mh': 138,
           'mq': 139,
           'mr': 140,
           'mu': 141,
           'yt': 142,
           'mx': 143,
           'fm': 144,
           'md': 145,
           'mc': 146,
           'mn': 147,
           'me': 148,
           'ms': 149,
           'ma': 150,
           'mz': 151,
           'mm': 152,
           'na': 153,
           'nr': 154,
           'np': 155,
           'nl': 156,
           'nc': 157,
           'nz': 158,
           'ni': 159,
           'ne': 160,
           'ng': 161,
           'nu': 162,
           'nf': 163,
           'mp': 164,
           'no': 165,
           'om': 166,
           'pk': 167,
           'pw': 168,
           'ps': 169,
           'pa': 170,
           'pg': 171,
           'py': 172,
           'pe': 173,
           'ph': 174,
           'pn': 175,
           'pl': 176,
           'pt': 177,
           'pr': 178,
           'qa': 179,
           're': 180,
           'ro': 181,
           'ru': 182,
           'rw': 183,
           'bl': 184,
           'sh': 185,
           'kn': 186,
           'lc': 187,
           'mf': 188,
           'pm': 189,
           'vc': 190,
           'ws': 191,
           'sm': 192,
           'st': 193,
           'sa': 194,
           'sn': 195,
           'rs': 196,
           'sc': 197,
           'sl': 198,
           'sg': 199,
           'sx': 200,
           'sk': 201,
           'si': 202,
           'sb': 203,
           'so': 204,
           'za': 205,
           'gs': 206,
           'ss': 207,
           'es': 208,
           'lk': 209,
           'sd': 210,
           'sr': 211,
           'sj': 212,
           'sz': 213,
           'se': 214,
           'ch': 215,
           'sy': 216,
           'tw': 217,
           'tj': 218,
           'tz': 219,
           'th': 220,
           'tl': 221,
           'tg': 222,
           'tk': 223,
           'to': 224,
           'tt': 225,
           'tn': 226,
           'tr': 227,
           'tm': 228,
           'tc': 229,
           'tv': 230,
           'ug': 231,
           'ua': 232,
           'ae': 233,
           'gb': 234,
           'us': 235,
           'um': 236,
           'uy': 237,
           'uz': 238,
           'vu': 239,
           've': 240,
           'vn': 241,
           'vg': 242,
           'vi': 243,
           'wf': 244,
           'eh': 245,
           'ye': 246,
           'zm': 247,
           'zw': 248,
           'unknown': 500
           }


def to_int(country_string):
    """
    Converts a 2-letter country string like fr to the appropriate enum value
    If not found, returns the value for unknown
    """
    lowercase = country_string.lower()
    if lowercase in country.keys():
        return country[lowercase]
    else:
        return country['unknown']


def to_key(code):
    """Converts the enum value to a 2 letter country code. If not found,
    returns unknown"""
    for name, number in country.iteritems():
        if code == number:
            return name
    return "unknown"
