from enum import Enum
from typing import Union
from htmlnodes import LeafNode

class TextType(Enum):
    NORMAL = 'NORMAL'
    BOLD   = 'BOLD'
    ITALIC = 'ITALIC'
    CODE   = 'CODE'
    LINK   = 'LINK'
    IMAGE  = 'IMAGE'

class TextNode:
    def __init__(self,
                 text:      str,
                 text_type: TextType,
                 url:       Union[str,None]=None
                 ):
        if not isinstance(text,str):
            raise TypeError(f'Expected str; got {type(text).__name__}')
        if not isinstance(text_type,TextType):
            raise TypeError(f'Expected TextType; got {type(text_type).__name__}')
        if not isinstance(url,Union[str,None]):
            raise TypeError(f'Expected str or None; got {type(url).__name__}')
        
        self.text      : str             = text
        self.text_type : TextType        = text_type
        self.url       : Union[str,None] = url

    def __eq__(self,other):
        if  self.text      == other.text \
        and self.text_type == other.text_type \
        and self.url       == other.url:
            return True
        return False
    
    def __repr__(self):
        return f'TextNode({str(self.text)},{str(self.text_type)},{self.url})'
    
    def to_html(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(None,self.text).to_html()
            case TextType.BOLD:
                return LeafNode('b',self.text).to_html()
            case TextType.ITALIC:
                return LeafNode('i',self.text).to_html()
            case TextType.CODE:
                return LeafNode('code',self.text).to_html()
            case TextType.LINK:
                return LeafNode('a',self.text,href=self.url).to_html()
            case TextType.IMAGE:
                return LeafNode('img','',src=self.url,alt=self.text).to_html()
            case _:
                raise ValueError('Unknown TextType in TextNode! Cannot convert to HTML.')