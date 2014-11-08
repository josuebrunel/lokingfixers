import os
import tarfile

from fixers import Fixer
from settings import HOME_CONFIG

class HomeConfig(Fixer):
    """Backup and restore home directory config files
    """

    def __init__(self):

        super(HomeConfig, self).__init__(__name__)


    def save(self,):
        """Saves config files
        """
        dest = os.path.join(HOME_CONFIG['dest'],HOME_CONFIG['archive'])
        tar = tarfile.open(dest,'w:gz')
        for f in HOME_CONFIG['files'] :
            file_path = os.path.join(HOME_CONFIG['src'], f)
            try:
                tar.add(file_path)
                self.logger.info("File {0} saved in archive {1}".format(f, dest))
            except Exception, e:
                print(e)
                self.log_error.error(e)
        tar.close()
            
    def restore(self,):
        """Restores config files
        """
        
        
