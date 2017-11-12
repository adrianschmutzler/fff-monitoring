import os

from TileStache import WSGITileServer
from TileStache.Config import buildConfiguration

config = {
	'map': {
		'cache_path': '.tilestache_cache'
	}
}


def find_xml(filename):
	return os.path.join(os.path.dirname(__file__), 'static', filename)


def get_config():
	buildConfiguration({
		"cache": {
			"name": "Disk",
			"path": config['map']['cache_path'],
		},
		"layers": {
			"links_and_routers": {
				"provider": {
					"class": "ffmap.map.dynmapnik:DynMapnik",
					"kwargs": {
						"mapfile": find_xml("links_and_routers.xml")
					}
				},
				"metatile": {"buffer": 128},
				"cache lifespan": 300
			},
			"hoods": {
				"provider": {
					"class": "ffmap.map.dynmapnik:DynMapnik",
					"kwargs": {
						"mapfile": find_xml("hoods.xml")
					}
				},
				"metatile": {"buffer": 128},
				"cache lifespan": 300
			}
		},
		"logging": "info"
	})


def get_app(args):
	return WSGITileServer(config=get_config())


def debug(args):  # TODO: remove me!
	from werkzeug.serving import run_simple
	app = get_app(args)
	run_simple(args.bind, args.port, app)
