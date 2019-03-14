from snapcraft.plugins import cmake
import subprocess

class CMakeWithPpa(cmake.CMakePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['ppa'] = { 'type': 'string', 'default': 'mir-team/release' }
        return schema


    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        subprocess.run(["sudo", "apt", "--assume-yes", "install", "software-properties-common"])
        subprocess.run(["sudo", "add-apt-repository", "-yu", "ppa:"+self.options.ppa])
