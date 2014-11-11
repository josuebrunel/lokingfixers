import os
import sys
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
            sys.exit(1)
        bkm = BrokMac(folder)

        bkm.check_file()

        print("{0} files fixed (^_^)".format(bkm.nbr))
        sys.exit(0)


class HomeConfigAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):

        hc = HomeConfig()
        
        if self.dest == 'restore':
            if not os.path.isdir(values):
                hc.log_error.info("{0} isn't  a valid directory".format(values))
                print("{0} is not a valid directory".format(values))
                sys.exit(1)
            hc.restore(values)
        elif self.dest == 'save':
            hc.save()
        else:
            hc.get_archived_files()

        sys.exit(0)
                      
                    
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
        help="Restore home directory config files to the location provided. If no path, restore in the current directory"
    )

    parser.add_argument(
        '-l',
        '--home-config-list-files',
        action=HomeConfigAction,
        dest='list',
        nargs=0,
        default=True,
        help="List home directory config files"
    )
    args = vars(parser.parse_args()) 