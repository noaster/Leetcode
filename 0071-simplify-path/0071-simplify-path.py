class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        pathList = [item for item in pathList if item != ""]
        
        result = []
        for item in pathList:
            if item == ".":
                continue
            elif item == "..":
                if result:
                    result.pop()
            else:
                result.append(item)
                
        #print(f"{result}")
        return "/" + "/".join(result)
        