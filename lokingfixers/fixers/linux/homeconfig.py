import os, imp
import tarfile

from lokingfixers.fixers import Fixer

settings = imp.load_source('', os.path.join(os.path.expanduser('~'), '.lokingfixers/settings.py'))
HOME_CONFIG = settings.HOME_CONFIG


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
        os.chdir(self.src)
        with tarfile.open(self.dest,'w:gz') as tar:
            for f in HOME_CONFIG['files'] :
                file_path = os.path.join(self.src, f)
                try:
                    print("Archiving {0}".format(file_path))
                    tar.add(f)
                    self.logger.info("File {0} saved in archive {1}".format(f, self.dest))
                except Exception, e:
                    print(e)
                    self.log_error.error(e)
            tar.close()
            
    def restore(self, path=None):
        """Restores config files
        """
        path = '.' if not path else path
        
        with tarfile.open(self.dest, 'r:*') as tar:
            try:
                print("Extracting files")
                tar.extractall(path)
                self.logger.info("Extracting files")
            except Exception, e:
                self.log_error.error(e)

            tar.close()

    def get_archived_files(self):
        """Returns list of archived files
        """
        with tarfile.open(self.dest, 'r:*') as tar :
            for f in tar.getnames():
                print f

            return tar.getnames()
        
