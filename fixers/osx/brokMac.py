import os
improt xattr

from fixers import Fixer
from tools import FLogger
from cfg import ATTRIBUT_KEY

class BrokMac():
    """This module fixes issue related to OSX files with
    the extended attribut 'Brok'. This issue often raise an error
    'item is used by OSX'
    """

    def __init__(self, folder):

        self.folder = folder

        self.nbr_brokMac = 0
 
    def list_brok_file(self,):
        """Returns list of 
        """
        brok_list = []
        
        for root, subdirs, files in os.walk(self.folder):
            for f in files :
                xf = xattr.xattr(f)
                if xf.get[ATTRIBUT_KEY] :
                    pass
                
                
        