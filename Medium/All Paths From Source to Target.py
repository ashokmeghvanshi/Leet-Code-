class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        graph1={}
        for i in range(len(graph)):
            if i not in graph:
                graph1[i]=graph[i]
        
        def AllPath(graph1,start,end,path):
            path=path+[start]
            if start==end:
                return [path]
            all_paths=[]
            for node in graph1[start]:
                if node not in path:
                    new_path=AllPath(graph1,node,end,path)
                for new_node in new_path:
                    all_paths.append(new_node)
            return all_paths

        return AllPath(graph1,0,len(graph)-1,path=[])
    
