from nodeitems_utils import NodeCategory

class RiggingNodeTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'RiggingNodesTreeType'

class RiggingNodesCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'RiggingNodesTreeType'