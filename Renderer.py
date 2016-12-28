import os


class Renderer:

    def __init__(self):
        self.command_path = "/Applications/Adobe\ After\ Effects\ CC\ 2017/aerender"
        self.project_path = "/Users/nogalavi/Documents/MikiProject/try.aep"
        self.comp_name = "mikmik"
        self.output_path = "/Users/nogalavi/Documents/MikiProject/result"
        self.command_structure = "%s -project %s -comp %s -output %s"

    def render(self):
        cmd = self.command_structure %(self.command_path, self.project_path, self.comp_name, self.output_path)
        print "running: %s" %cmd
        os.system(cmd)
        print "Finished"



