from course_tree import *
from full_tree_node import *
from access_log import *

class FullTree(object):

    def __init__(self):
        self.course_id = None
        self.root = FullTreeNode(0)
        self.seq = {}

    def __init__(self,course_tree,course_id):
        self.course_id = course_id
        self.root = course_tree.root.copy_to_FullNode()
        self.seq = {}


    def get_root(self):
        return self.root

    def add_access_log(self,access_record):
        node = self.root.find_node(access_record.get_id())
        if node is None:
            node = FullTreeNode(access_record.get_id())
            node.set_level(1)
            node.category = 'unknown'
            node.start = None
            self.root.children[access_record.get_id()] = node
        node.add_access_log(access_record)

    def print_tree(self):
        print "=======================================" + str(self.course_id)
        for id,child in self.root.children.items():
            if child is None:
                print '(' + id + ')'
            else:
                child.print_node_and_children()


    def print_tree_to_file(self,output):
        print >>output,"=======================================" + str(self.course_id)
        for id,child in self.root.children.items():
            if child is None:
                print >>output,'(' + id + ')'
            else:
                child.print_node_and_children_to_file(output)

    def  rectify_time(self):
        self.root.rectify_time(self.root.get_earliest())


    def add_insula_to_sequentials(self):
        self.update_seq()
        for id,child in self.root.get_children().items():
            if child.get_category() == "unknown":
                parent_seq = self.find_nearest_seq(child.get_start())
                parent_seq.get_children()[id] = child
                child.adjust_category()
                child.set_level(4)
                del self.root.children[id]



    def update_seq(self):
        self.root.find_seq(self.seq)

    def print_seq(self):
        keys = self.seq.keys()
        keys.sort()
        for key in keys:
            print str(key)+ " : " + str(self.seq[key].get_id())


    def find_nearest_seq(self,time):
        self.update_seq()
        keys = self.seq.keys()
        keys.sort()

        last = None
        nearest = self.root
        for timestamp in keys:
            if timestamp > time:
                nearest = self.seq[last]
                break
            last = timestamp
        return nearest













