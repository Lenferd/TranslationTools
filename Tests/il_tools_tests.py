import unittest
import sys
import os

# sys.path.insert(0, os.path.pardir)

from Tools.Ill_handler.il_packer import *
from Tools.Ill_handler.il_unpacker import *

class DLLPackTests(unittest.TestCase):
    def test_replacing(self):
        test_text = '''    IL_000d:  stloc.1
            IL_000e:  ldloc.1
            IL_000f:  brfalse.s  IL_001c

            IL_0011:  ldstr      "Target is null"
            IL_0016:  newobj     instance void [mscorlib]System.InvalidOperationException::.ctor(string)
            IL_001b:  throw
        '''
        expected_text = '''    IL_000d:  stloc.1
            IL_000e:  ldloc.1
            IL_000f:  brfalse.s  IL_001c

            IL_0011:  ldstr      "Тархет из нулл"
            IL_0016:  newobj     instance void [mscorlib]System.InvalidOperationException::.ctor(string)
            IL_001b:  throw
        '''
        original = [["IL_0011:"], ["ldstr"], ["Target is null"]]
        translation = [["IL_0011:"], ["ldstr"], ["Тархет из нулл"]]
        self.assertEqual(replace_translation(test_text.split('\n'), original, translation), expected_text.split('\n'))

class DLLUnpackTests(unittest.TestCase):
    def test_got_right_data_from_unpack(self):
        test_text = '''IL_009c:  ldstr      "Packsize Failure"
        IL_00a1:  call       void [UnityEngine]UnityEngine.Debug::Log(object)
        IL_00a6:  nop
        IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the"
        + " wrong version of Steamworks.NET is being run in this platform."'''

        self.assertEqual(len(unpackText(test_text)), 2)
        self.assertEqual(unpackText(test_text)[0][2], '"Packsize Failure"')
        self.assertEqual(unpackText(test_text)[1][2], '"[Steamworks.NET] Packsize Test returned false, the wrong version of Steamworks.NET is being run in this platform."')

    def test_plus_replace(self):
        test_text = '''IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the"
        + " wrong version of Steamworks.NET is being run in this platform."'''
        expected_result= '''IL_00a7:  ldstr      "[Steamworks.NET] Packsize Test returned false, the wrong version of Steamworks.NET is being run in this platform."'''
        self.assertEqual(replacePlus(test_text), expected_result)

    def test_replace_multiple_time(self):
        test_text = ''' "some text"
        + " some add text"
        "some another text"
        "some new text"
           + " another text"'''
        expected_result =  ''' "some text some add text"
        "some another text"
        "some new text another text"'''
        self.assertEqual(replacePlus(test_text), expected_result)

if __name__ == '__main__':
    unittest.main()
