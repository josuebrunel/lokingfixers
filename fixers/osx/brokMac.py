import os
import xattr
import pdb
from fixers import Fixer
from cfg import ATTRIBUT_KEY

class BrokMac(Fixer):
    """This module fixes issue related to OSX files with
    the extended attribut 'Brok'. This issue often raise an error
    'item is used by OSX'
    """

    def __init__(self, folder):

        super(BrokMac, self).__init__()
        self.folder = folder

        self.nbr = 0
        self.lst = []
 
    def check_file(self, fix=False):
        """Returns list of 
        """
        
        for root, subdirs, files in os.walk(self.folder):
            for f in files :
                fpath = os.path.join(root, f)
                try:
                    xf = xattr.xattr(fpath)
                    if xf.get(ATTRIBUT_KEY).startswith('brokMACS') :
                        print fpath
                        if fix:
                            xf.remove(ATTRIBUT_KEY)
                        self.lst.append(fpath)
                        self.nbr_brokMac += 1
                        self.logger.debug(fpath)
                except:
                    pass
        
        return self.lst


