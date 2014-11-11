import os
import argparse

from lokingfixers import BrokMac
from lokingfixers import HomeConfig

class BrokMacAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):

        folder = values

        if not folder :
            folder = namespace.folder

        folder = os.path.realpath(folder)

        if not os.path.isdir(folder):
            print("The argument isn't a valid directory")
            return 1
        bkm = BrokMac(folder)

        bkm.check_file()

        print("{0} files fixed (^_^)".format(bkm.nbr))


class HomeConfigAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):

        hc = HomeConfig()
        
        if self.dest == 'restore':
            if values:
                files = values
            hc.restore()
        else:
            hc.save()
            
                    
if __name__ == '__main__':

    parser = argparse.ArgumentParser("OS (Linux/OSX)) trouble fixers")
    # brokMac parser
    parser.add_argument(
        '-b',
        '--fix-brokmac',
        action=BrokMacAction,
        dest='folder',
        #nargs= '?',
        default = '.',
        help="Fix OSX issues 'item is used by OSX'"
    )
    
    # homeConfig parsers
    parser.add_argument(
        '-s',
        '--home-config-save',
        action=HomeConfigAction,
        nargs= 0,
        default= True,
        dest='save',
        help="Backup home directory config files"
    )

    parser.add_argument(
        '-r',
        '--home-config-restore',
        action=HomeConfigAction,
        dest='restore',
        nargs= '?',
        default= True,
        help="Restore home directory config files"
    )
 
    args = vars(parser.parse_args()) 