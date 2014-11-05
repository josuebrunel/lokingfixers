import argparse

from fixers import BrokMac

class BrokMacAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        print '%r %r %r' % (namespace, values, option_string)

        bkm = BrokMac(values)

    
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