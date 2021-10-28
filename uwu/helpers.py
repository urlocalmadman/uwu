import re


class TokenType:
    LETTERS = 'LETTERS'
    PUNCTUATION = 'PUNCTUATION'
    SPACE = 'SPACE'
    UNKNOWN = 'UNKNOWN'


class Token:

    def __init__(self, val: str, token_type: str) -> None:
        self.val = val
        self.token_type = token_type

    def __len__(self) -> int:
        return len(self.val)

    def __repr__(self) -> str:
        return f"({self.token_type}: '{self.val}')"


TOKEN_MAP = {
    TokenType.LETTERS: re.compile(r'[a-zA-Z0-9\'\"\:\-\<\>\@\!]+'),
    # escape everything because I'm too lazy to check
    TokenType.PUNCTUATION: re.compile(
        r'[\`\~\#\$\%\^\&\*\(\)\_\+\=\[\]\{\}\,\.\/\?\;\|\\]+'
    ),
    TokenType.SPACE: re.compile(r'\s+')
}


REPLACE_WORDS_MAP = {
    "small": "smol",
    "smaller": "smoller",
    "smallest": "smollest",
    "cute": "uwu",
    "cuter": "uwuwer",
    "cutest": "uwuwest",
    "fluff": "floof",
    "fluffy": "floofy",
    "fluffier": "floofier",
    "fluffiest": "floofiest",
    "love": "luv",
    "stupid": "baka",
    "meow": "nya",
    "wow": "owo",
    "kek": "kekw",
    "nani": "nyani",
    "daddy": "dawwy",
}

# to add after punctuation
RANDOM_INSERTS = [
    " rawr x3",
    " OwO",
    " UwU",
    " o.O",
    " -.-",
    " >w<",
    " (⑅˘꒳˘)",
    " (ꈍᴗꈍ)",
    " (˘ω˘)",
    " (U ᵕ U❁)",
    " σωσ",
    " òωó",
    " (///ˬ///✿)",
    " (U ﹏ U)",
    " ( ͡o ω ͡o )",
    " ʘwʘ",
    " :3",
    " :3",
    " nyaa~~",
    " mya",
    " >_<",
    " 😳",
    " 🥺",
    " 😳😳😳",
    " rawr",
    " ^^",
    " ^^;;",
    " (ˆ ﻌ ˆ)♡",
    " ^•ﻌ•^",
    " /(^•ω•^)",
    " (✿oωo)",
    " ヾ(•ω•`)o ",
    " （＾∀＾●）ﾉｼ ",
    " (＾Ｕ＾)ノ~ ",
    " o(*°▽°*)o ",
    " ✪ ω ✪ ",
    " ＜（＾－＾）＞ ",
    " o(*￣▽￣*)o ",
    " (o゜▽゜)o☆ ",
    " ＜（＾－＾）＞ ",
    " (╯▽╰ ) ",
    " ヽ(✿ﾟ▽ﾟ)ノ ",
    " ( •̀ .̫ •́ )✧ ",
    " (^^ゞ ",
    " (＠＾０＾) ",
    " （。＾▽＾） ",
    " （；´д｀）ゞ ",
    " ＞﹏＜ ",
    " (っ °Д °;)っ ",
    " ＞︿＜ ",
    " o(￣┰￣*)ゞ ",
    " （＞人＜；） ",
    " ヽ(*。>Д<)o゜ ",
    " (；′⌒`) ",
    " ≧ ﹏ ≦ ",
    " ( ≧Д≦) ",
    " (；￣Д￣） ",
    " (｡+･`ω･´) ",
    " ｡゜(｀Д´)゜｡ ",
    " (>_<) ",
    " （＞д＜） ",
    " (≧σ≦) ",
    " (」゜ロ゜)」 ",
    " (/ﾟДﾟ)/ ",
    " ＼( ｀.∀´)／ ",
    " ＼(>o<)ノ ",
    " ヾ( ･`⌓´･)ﾉﾞ ",
    " ヾ(。◣∀◢。)ﾉ ",
    " ヾ(｡｀Д´｡)ﾉ彡☆ ",
    " ヽ(o｀Д´o)ﾉ ",
    " ｏ( ><)o ",
    " ( ꒪Д꒪)ノ ",
    " ⁽͑˙˚̀བ̇˚́˙⁾̉ ",
    " ⁽͑˙˚̀⚐˚́˙⁾̉ ",
    " ｍ（｡≧ _ ≦｡）ｍ ",
    " o(´д｀o) ",
    " ヾ(_ _*) ",
    " _:(´□`」 ∠):_ ",
    " （ﾉ´д｀） ",
    " へ(´д｀へ) ",
]
