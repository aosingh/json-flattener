import logging
import json
import sys

import click

from pathlib import Path
from jflat.flattener import JSONFlattener

LOG = logging.getLogger(__name__)
LOG_FORMAT = '%(asctime)s - %(message)s'


@click.command()
@click.argument('json_string', required=False)
@click.option('--log-level', default='NOTSET', help='Log level', type=click.Choice(list(logging._nameToLevel.keys())))
@click.option('--out-file', help='Path to the output JSON file', default=None, show_default=True, type=str)
@click.option('--sort-keys/--no-sort-keys', default=False, show_default=True)
def main(json_string, log_level, out_file, sort_keys):

    logging.basicConfig(format=LOG_FORMAT, level=log_level)

    if not json_string:
        json_string = click.get_text_stream('stdin').read().strip()


    data = json.loads(json_string)

    flattener = JSONFlattener(data=data)
    flattened_data = flattener()

    if out_file is None:
        LOG.warning("Outfile is None")
        sys.stdout.write(json.dumps(flattened_data, indent=2, sort_keys=sort_keys))
    else:
        out_file = Path(out_file)
        if not out_file.parent.exists():
            raise FileNotFoundError(f"Directory {out_file.parent}")
        LOG.info("Output file is %s", out_file)
        with open(out_file, 'w') as fp:
            json.dump(flattened_data, fp, indent=2, sort_keys=sort_keys)




