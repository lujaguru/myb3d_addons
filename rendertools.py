bl_info = {
    "name": "Render Tools",
    "description": "Useful and time-saving tools for rendering workflow",
    "author": "Aditia A. Pratama",
    "version": (0, 3),
    "blender": (2, 66,1),
    "location": "3D View > Property Region (N-key)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/aditiapratama/myb3d_addons",
    "category": "3D View"}

import bpy

class SubsurfToggle(bpy.types.Operator):
    'Toggle subsurf visibility'
    bl_idname='subsurf.toggle'
    bl_label='Subsurf Toggle'
       
    def execute(self,context):
        state = bpy.context.active_object.modifiers['Subsurf'].show_viewport
        for e in bpy.context.selected_objects:
            try:
                if state==False:
                    e.modifiers['Subsurf'].show_viewport = True
                else:
                    e.modifiers['Subsurf'].show_viewport = False
            except KeyError:
                print ("No subsurf on "+e.name+" or it is not named Subsurf")
        return {'FINISHED'}
            
class Visibility(bpy.types.Panel):
    bl_label = "Render Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
       
    def draw (self, context):
        layout=self.layout
                                                   
        col=layout.column()
        col.operator("subsurf.toggle",  text="On/Off", icon="MOD_SUBSURF")
        
        col.separator()            
        
        view = context.scene.render
          
        col.prop(view, "use_simplify", text="Simplify")
        sub = col.column()
        sub.active = view.use_simplify
        sub.prop(view, "simplify_subdivision", text="Subdivision")
        
        col.separator()
        
        ob = context.object
        
        layout.prop(ob, "dupli_group", text="Group")

def register():
   bpy.utils.register_module(__name__)
   
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()
