# Build Order: you are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent
# on the first project). All of a project's dependencies must be build before
# the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

from queue import *

class ProjectNode:
    def __init__(self, val):
        self.val = val
        self.dependents = []
        self.numDependencies = 0

    def append(self, proj):
        self.dependents.append(proj)
        proj.numDependencies += 1

    def decrementDependents(self):
        for dep in self.dependents:
            dep.numDependencies -= 1


def buildOrder(projectsStrings, dependenciesStrings):
    d = {}
    projects = []
    for projectString in projectsStrings:
        project = ProjectNode(projectString)
        d[projectString] = project
        projects.append(project)


    for [dependencyString, dependentString] in dependenciesStrings:
        dependent = d[dependentString]
        dependency = d[dependencyString]
        dependency.append(dependent)

    numLeft = len(projects)
    q = Queue()
    buildOrder = []
    for project in projects:
        if (project.numDependencies == 0):
            q.add(project)

    while not q.isEmpty():
        curr = q.remove()
        buildOrder.append(curr.val)
        numLeft -= 1
        curr.decrementDependents()
        for dep in curr.dependents:
            if dep.numDependencies == 0:
                q.add(dep)

    if numLeft != 0: print("ERROR")
    else: print(buildOrder)


if (__name__ == "__main__"):
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [["a", "b"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
    print("Buildable Test:")
    buildOrder(projects, dependencies)

    dependencies = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"], ["e", "f"], ["f", "a"]]
    print("Nonbuildable Test:")
    buildOrder(projects, dependencies)
