
class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,**properties):
        self.tag = tag
        self.value = value
        self.children = children
        self.properties = properties

    def __repr__(self):
        return f'HTMLNode({self.tag},{self.value},{self.children},{self.properties})'

    def to_html(self):
        raise NotImplementedError('to_html must be used in the LeafNode or ParentNode subclasses')
    
    def props_to_html(self):
        if not self.properties:
            return ''
        return ' ' + ' '.join([f'{k}="{str(v)}"' for k,v in self.properties.items()])
    
class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,**properties):
        if value == None:
            raise ValueError('LeafNodes must have a value')
        if tag==None and properties:
            raise Exception('LeafNode cannot have properties without a tag!')
        super().__init__(tag,value,**properties)

    def to_html(self):
        if not self.tag:
            return self.value
        return f'''<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'''

class ParentNode(HTMLNode):
    def __init__(self,tag,children,**properties):
        super().__init__(tag,children=children,**properties)

    def to_html(self):
        if not self.tag:
            raise ValueError('ParentNode must have a tag')
        if not self.children:
            raise ValueError('ParentNode must have children')
        children_text = ''.join([child.to_html() for child in self.children])
        return f'''<{self.tag}{self.props_to_html()}>{children_text}</{self.tag}>'''

# print(HTMLNode('a',href='https://example.com', target='_blank'))