import os
import tarfile

from fixers import Fixer
from settings import HOME_CONFIG

class HomeConfig(Fixer):
    """Backup and restore home directory config files
    """

    def __init__(self):

        super(HomeConfig, self).__init__(__name__)
        self.src = HOME_CONFIG['src']
        self.dest = os.path.join(HOME_CONFIG['dest'],HOME_CONFIG['archive']) 

    def save(self,):
        """Saves config files
        """

        tar = tarfile.open(self.dest,'w:gz')
        for f in HOME_CONFIG['files'] :
            file_path = os.path.join(self.src, f)
            try:
                tar.add(file_path)
                self.logger.info("File {0} saved in archive {1}".format(f, self.dest))
            except Exception, e:
                print(e)
                self.log_error.error(e)
        tar.close()
            
    def restore(self,):
        """Restores config files
        """
        with tarfile.open(self.dest, 'r:*') as tar:
            try:
                self.logger.info("Extraction files")
                tar.extractall()
            except Exception, e:
                self.log_error.error(e)

    def get_archived_files(self):
        """Returns list of archived files
        """
        with tarfile.open(self.dest, 'r:*') as tar :
            for f in tar.getnames():
                print f

            return tar.getnames()
        
        
