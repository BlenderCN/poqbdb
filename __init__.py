bl_info = {
    'name': 'poqbdb',
    'description': 'process or query by database',
    'author': 'Fofight',
    'license': 'GPL',
    'version': (1, 0, 0),
    'blender': (2, 80, 0),
    'location': 'View3D > Tools > poqbdb',
    'warning': '',
    'wiki_url': 'https://github.com/BlenderCN/poqbdb/wiki',
    'tracker_url': 'https://github.com/BlenderCN/poqbdb/issues',
    'link': 'https://github.com/BlenderCN/poqbdb',
    'support': 'COMMUNITY',
    'category': 'Add Mesh'
    }



from . import poqbdb





def register():
	poqbdb.register()

def unregister():
	poqbdb.unregister()

if __name__ == '__main__':
	register()


