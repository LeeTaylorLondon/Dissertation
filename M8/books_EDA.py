"""
Author Lee Taylor
"""
import os
import xml.etree.ElementTree as ET


def list_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        filenames.append(directory + filename)
    return filenames


def print_list(arr, limit=None):
    # Out number of items contained to user
    print(f"\nList contains {len(arr)} items.\n[")
    # Out each item & it's item type i.e. int, str, etc.etc
    for item in arr[:limit]:
        print(f"    {str(type(item)).split(' ')[1][1:-2]}: '{item}',")
    # Close content outed from list
    print("]")
    # State number of items (if user specified) outed
    if limit is not None:
        print(f"First {limit} items shown above this line.")


def read_xml(fn):
    # Load the XML file
    tree = ET.parse(fn)
    root = tree.getroot()
    # Initialize the list
    text_list = []
    # Iterate through the 's' elements and add the text to the list
    for s in root.iter('s'):
        text_list.append(s.text)
    # Return sentences
    return text_list


if __name__ == '__main__':
    # Write code here
    ...

    # # Test function list_filenames
    # print_list(list_filenames("opus.nlpl.eu.books.php/books_xml"), 10)
    # # >>> <list of book names in the specified folder>
    #
    # # Test function read_xml
    # print_list(read_xml(list_filenames("opus.nlpl.eu.books.php/books_xml")[0]), 10)
    # # >>> <list of sentences from the specified book>

    xml_data = """
    <root>
      <s id="s1">
       <chunk type="NP" id="c1-1">
        <w hun="NN" tree="NN" lem="translation" pos="NN" id="w1.1">Translation</w>
       </chunk>
       <w hun=":" tree=":" lem=":" pos=":" id="w1.2">:</w>
       <chunk type="NP" id="c1-3">
        <w hun="NNP" tree="NP" pos="NNP" id="w1.3">Françoise</w>
        <w hun="NNP" tree="NP" lem="Delisle" pos="NNP" id="w1.4">Delisle</w>
       </chunk>
      </s>

      <s id="s2">
       <chunk type="NP" id="c2-1">
        <w hun="DT" tree="DT" lem="the" pos="DT" id="w2.1">The</w>
        <w hun="NNP" tree="NP" pos="NNP" id="w2.2">Wanderer</w>
       </chunk>
      </s>

      <!-- ... -->
    </root>
    """

    root = ET.fromstring(xml_data)
    s_elements = root.findall("./s")

    result = []
    for s in s_elements:
        s_dict = {"id": s.attrib["id"], "chunks": []}
        chunk_elements = s.findall("./chunk")
        for chunk in chunk_elements:
            chunk_dict = {"type": chunk.attrib["type"], "id": chunk.attrib["id"], "words": []}
            word_elements = chunk.findall("./w")
            for word in word_elements:
                word_dict = {"hun": word.attrib["hun"], "tree": word.attrib["tree"], "lem": word.attrib.get("lem", ""),
                             "pos": word.attrib["pos"], "id": word.attrib["id"], "text": word.text}
                chunk_dict["words"].append(word_dict)
            s_dict["chunks"].append(chunk_dict)
        result.append(s_dict)

    print(result)

    print_list(result)

    print()
    print(result[0])

    # Mark EO-if-name-main section
    pass
