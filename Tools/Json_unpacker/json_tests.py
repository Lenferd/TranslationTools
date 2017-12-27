import unittest
import sys
import os
import json

sys.path.insert(0, os.path.pardir)

from Tools.Json_unpacker.json_pack import JsonPack
from Tools.Json_unpacker.json_pack import pack_file


class TestPackJsonFiles(unittest.TestCase):

    pack = JsonPack()
    test_dir = "tests"
    name = "events"

    def setUp(self):
        self.pack.init(_dir_with_data=self.test_dir, _name=self.name)
        self.pack.read_files_to_pack()
        self.pack.read_json()

    def test_file_print_not_translated(self):
        self.pack.translate()
        self.pack.write_out_not_translated()
        self.pack.write_out()


class TestPackJsonModules(unittest.TestCase):
    json_obj = []
    flags = ['ButtonText', 'Description', 'Name', 'Teaser', 'MoveMessage']
    ignore = ['Always', 'Sometimes']
    lvl = 1
    json_text_orig = 0
    json_text_transl = 0

    test_dir = "tests"

    def test_retranslate(self):
        json_pack = JsonPack()
        self.json_obj = json.loads("""
        [{"Teaser": "He's hard to read, with those glasses, but he reads the summary intently..."}]
        """)
        self.json_text_orig = [['>'], ['Teaser'],
                               ['He\'s hard to read, with those glasses, but he reads the summary intently...']]
        self.json_text_transl = [['>'], ['Teaser'],
                                 ['Ему трудно читать, с такими очками, но он читает сводку внимательно...']]
        json_pack.init_data(self.json_obj, self.flags, self.ignore, self.json_text_orig, self.json_text_transl)

        json_pack.translate()

        expected = [{'Teaser': 'Ему трудно читать, с такими очками, но он читает сводку внимательно...'}]
        self.assertEqual(json_pack.j_obj, expected)

    def test_not_add_additional_slash(self):
        json_pack = JsonPack()
        self.json_obj = json.loads("""
                [{"Teaser": "AAA \\"BBB\\" CCC"}]
                """)
        self.json_text_orig = [['>'], ['Teaser'],
                               ['AAA \"BBB\" CCC']]
        self.json_text_transl = [['>'], ['Teaser'],
                                 ['ААА \"БББ\" ЦЦЦ']]
        json_pack.init_data(self.json_obj, self.flags, self.ignore, self.json_text_orig, self.json_text_transl)

        json_pack.translate()

        expected = [{'Teaser': 'ААА \"БББ\" ЦЦЦ'}]
        self.assertEqual(json_pack.j_obj, expected)

    def test_after_load_dont_add_additional_slash(self):

        filename = "test_readfile.txt"
        data = JsonPack.read_file_full_strip(os.path.join(self.test_dir, filename))
        self.assertTrue(data[2][0].find("\\\"") == -1)

    # this test may not show some activity, but the main thing - test to replace str with control char at end
    # at most, this should be done on read_file_full_strip and read_file
    def test_pack_with_control_characters_at_end(self):
        json_pack = JsonPack()
        self.json_obj = json.loads("""[{"Description": "Seven diving suits take up the Investigator's room. \\"We're exploring the space between Temtum and its city-shell. But we'll need another five divers.\\"\\r\\n "}]""")
        self.json_text_orig = [['>'], ['Description'],
                               ["""Seven diving suits take up the Investigator's room. "We're exploring the space between Temtum and its city-shell. But we'll need another five divers."\r\n """]]
        self.json_text_transl = [['>'], ['Description'],
                                 ["""Семь подводных костюмов в комнате Следователя, готовых для погружения. \"Мы исследуем пространство между Темтумом и его панцирем-городом. Но нам понадобятся ещё пять ныряльщиков.\"\r\n"""]]

        # main thing
        self.json_text_orig[2][0] = self.json_text_orig[2][0].rstrip()

        json_pack.init_data(self.json_obj, self.flags, self.ignore, self.json_text_orig, self.json_text_transl)
        json_pack.translate()

        expected = [{'Description': 'Семь подводных костюмов в комнате Следователя, готовых для погружения. \"Мы исследуем пространство между Темтумом и его панцирем-городом. Но нам понадобятся ещё пять ныряльщиков.\"\r\n'}]
        self.assertEqual(json_pack.j_obj, expected)


    # def test_pack_1(self):
    #     json_pack = JsonPack()
    #     self.json_obj = json.loads(
    #         """[{"Description": "The zee opens out beneath a high cliff -"}]""")
    #     self.json_text_orig = [['>'], ['Description'],
    #                            ["""The zee opens out beneath a high cliff -"""]]
    #     self.json_text_transl = [['>'], ['Description'],
    #                              ["""Вид на море открывается из-под высокой скалы..."""]]
    #
    #     # main thing
    #     # self.json_text_orig[2][0] = self.json_text_orig[2][0].rstrip()
    #
    #     json_pack.init_data(self.json_obj, self.flags, self.ignore, self.json_text_orig, self.json_text_transl)
    #     json_pack.translate()
    #
    #     expected = [{
    #                     'Description': 'Семь подводных костюмов в комнате Следователя, готовых для погружения. \"Мы исследуем пространство между Темтумом и его панцирем-городом. Но нам понадобятся ещё пять ныряльщиков.\"\r\n'}]
    #     self.assertEqual(json_pack.j_obj, expected)
    #

    """
     required:
        j_obj - json to translate
        flags 
        ignore
        lvl - lvl, which we start 
        json_text_orig - vect with orig
        json_text_transl - vect with transl
    """
    # def test_translate(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
