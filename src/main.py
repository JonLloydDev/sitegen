from textnode import TextNode,TextType

def main():
    text = TextNode(
        'Anchor text test',
        TextType.LINK,
        'https://example.com'
    )
    print(text)

main()