import os
import argparse

from fixers import BrokMac

class BrokMacAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        print '%r %r %r' % (namespace, values, option_string)

        folder = values
        
        if not folder :
            folder = namespace.brok_mac

        folder = os.path.realpath(folder)

        if not os.path.isdir(folder):
            print("The argument isn't a valid directory")
            return 0
        bkm = BrokMac(folder)

        bkm.check_file()

        print("{0} files fixed (^_^)".format(bkm.nbr))

        
if __name__ == '__main__':

    parser = argparse.ArgumentParser("OS (Linux/OSX)) trouble fixers")

    parser.add_argument(
        '-b',
        '--fix-brokmac',
        action=BrokMacAction,
        nargs= '?',
        default = '.',
        help="Fix OSX issues 'item is used by OSX'"
    )

    args = vars(parser.parse_args()) 