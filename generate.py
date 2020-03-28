import csv
import json
from argparse import ArgumentParser
from sys import stdout
from typing import Tuple

from generator.api import generate_events


def _get_args() -> Tuple[int, int, int]:
    parser = ArgumentParser()
    parser.add_argument('n', help='number of events to generate', type=int)
    parser.add_argument('-t', help='time of first event [OPTIONAL]', type=int)
    parser.add_argument('-f', help='format of output [OPTIONAL]', type=str, default='csv')
    args = parser.parse_args()
    return args.n, args.t, args.f


if __name__ == '__main__':
    n, start_time, out_format = _get_args()

    if start_time is not None:
        events = generate_events(n, start_time)
    else:
        events = generate_events(n)

    if out_format == 'csv':
        with stdout as f:
            writer = csv.writer(f)
            writer.writerows(map(lambda ev: ev.__dict__.values(), events))
    elif out_format == 'json':
        for e in events:
            stdout.write(f'{json.dumps(e.__dict__)}\n')
    else:
        print('invalid out format')
