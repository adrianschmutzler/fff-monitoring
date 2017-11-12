import argparse


def webapp(args):
	from .map.__main__ import get_app as get_app_tiles
	from .web.application import app as app_web
	from werkzeug.wsgi import DispatcherMiddleware
	from werkzeug.serving import run_simple
	app = DispatcherMiddleware(app_web, {
		'/tiles': get_app_tiles(args),
	})
	if args.debug:
		run_simple(args.bind, args.port, app)
	else:
		raise NotImplementedError


def main():
	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers()

	p_map = subparser.add_parser('webapp')
	p_map.add_argument('--debug', action='store_true')
	p_map.add_argument('--bind', default='127.0.0.1')
	p_map.add_argument('--port', default=5000, type=int)
	p_map.set_defaults(func=webapp)

	args = parser.parse_args()
	args.func(args)
