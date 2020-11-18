import os
import shutil
import time

class Terminator():
    def __init__(self,initialDirectoryPath = "C://",folderName="node_modules",recusrive=False):
        self.initialDirectory = initialDirectoryPath
        self.folderName = folderName
        self.recursive = recusrive
        self.time = time.time()
        self.notHit = ["node_modules",".git","env","__pycache__","build"]
    def delete_this_directory(self,directory):
        try:
            shutil.rmtree(directory)
            print("Deleted {} folder at {}".format(self.folderName,directory))
        except OSError as e:
            print("Error occured while deleting {} folder at {} \n{} {}".format(self.folderName,directory,e.filename,e.strerror))

    def match_dir(self,directory,notHit):
        for each in notHit:
            if each in directory:
                return True
        return False
    def check_path_exists(self,data,path):
        for each in data:
            if path.endswith(each):
                return True
        return False
    def find_all_folder(self,startingPoint):
        allNames = []
        for each in os.listdir(startingPoint):            
            eachName = os.path.join(startingPoint,each)
            if os.path.isdir(eachName) :
                if self.folderName in eachName and not eachName.endswith(self.folderName):
                    allNames.append(eachName)
                    continue
                allNames.extend(self.find_all_folder(eachName))
        return allNames
    def terminate(self):
        if self.recursive:

            data = self.find_all_folder(self.initialDirectory)
            output = set()
            for each in data:
                if self.folderName in each:
                    if not each.endswith(self.folderName):
                        each = each[:each.rindex("\\")]
                    output.add(each)
            for each in output:
                self.delete_this_directory(each)
        else:
            self.delete_this_directory(self.initialDirectory+"\\"+self.folderName)
        print("Terminated in {}".format(self.time - time.time()))
            

if __name__ == "__main__":
    bot1 = Terminator(initialDirectoryPath="E:\Web",recusrive=True)
    bot1.terminate()