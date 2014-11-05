import os
import xattr
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
 
    def check_file(self, fix=True):
        """Returns list of 
        """
        self.logger.info("CHECKING FILES")
        print("CHECKING FILES ...")
        for root, subdirs, files in os.walk(self.folder):
            for f in files :
                fpath = os.path.join(root, f)
                try:
                    xf = xattr.xattr(fpath)
                    if xf.get(ATTRIBUT_KEY).startswith('brokMACS') :
                        print(fpath + " is used by OSX")
                        self.logger.info(fpath)
                        if fix:
                            xf.remove(ATTRIBUT_KEY)
                        self.lst.append(fpath)
                        self.nbr += 1
                        
                except Exception, e:
                    #self.log_error.error(e)
                    continue
        self.reporter.info("{0} files fixed (^_^)".format(self.nbr))
        return self.lst


