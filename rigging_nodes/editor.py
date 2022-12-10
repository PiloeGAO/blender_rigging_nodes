from bpy.types import NodeTree

class RiggingNodesTree(NodeTree):
    '''The Rigging Nodes editor'''
    bl_idname = 'RiggingNodesTreeType'
    bl_label = "Rigging Nodes"
    bl_icon = 'NODETREE'