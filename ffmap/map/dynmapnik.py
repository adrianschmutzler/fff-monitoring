#!/usr/bin/python3

import os
import logging
import TileStache.Mapnik

logger = logging.getLogger(__name__)

class DynMapnik(TileStache.Mapnik.ImageProvider):
	def __init__(self, *args, **kwargs):
		print("#"*80)
		self.mapfile_mtime = 0
		TileStache.Providers.Mapnik.__init__(self, *args, **kwargs)
	def renderArea(self, *args, **kwargs):
		cur_mapfile_mtime = os.path.getmtime(self.mapfile)
		if cur_mapfile_mtime > self.mapfile_mtime:
			self.mapfile_mtime = cur_mapfile_mtime
			if self.mapnik is not None:
				self.mapnik = None
				logger.info('TileStache.DynMapnik.ImageProvider.renderArea() detected mapfile change')
		return super().renderArea(*args, **kwargs)
