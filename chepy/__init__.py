from .modules.aritmeticlogic import AritmeticLogic
from .modules.codetidy import CodeTidy
from .modules.compression import Compression
from .modules.dataformat import DataFormat
from .modules.datetimemodule import DateTime
from .modules.encryptionencoding import EncryptionEncoding
from .modules.extractors import Extractors
from .modules.forensics import Forensics
from .modules.hashing import Hashing
from .modules.language import Language
from .modules.multimedia import Multimedia
from .modules.networking import Networking
from .modules.other import Other
from .modules.publickey import Publickey
from .modules.utils import Utils


class Chepy(
    AritmeticLogic,
    CodeTidy,
    Compression,
    DataFormat,
    DateTime,
    EncryptionEncoding,
    Extractors,
    Forensics,
    Hashing,
    Language,
    Multimedia,
    Networking,
    Other,
    Publickey,
    Utils,
):
    pass