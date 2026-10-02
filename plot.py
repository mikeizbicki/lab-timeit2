#!/usr/bin/env python3
"""Plot a CSV as a log-log chart."""
import argparse, csv
import matplotlib.pyplot as plt


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv_file', help='CSV file produced by measure.py')
    p.add_argument('-o', '--output', default='output.png',
                   help='PNG output file (default: %(default)s)')
    return p.parse_args()


def load(fname):
    """Return (ns, {column_name: [values]})."""
    with open(fname) as f:
        rows = list(csv.DictReader(f))
    ns = [int(r['n']) for r in rows]
    # Every column other than 'n' is a function's timing series.
    series = {col: [float(r[col]) for r in rows]
              for col in rows[0] if col != 'n'}
    return ns, series


def main():
    args = parse_args()
    ns, series = load(args.csv_file)

    for name, ts in series.items():
        plt.plot(ns, ts, marker='o', label=name)

    # Log-log axes make the asymptotic slopes easy to read:
    # sequential search -> slope 1, binary search -> nearly flat.
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('seconds per call')
    plt.legend()
    plt.savefig(args.output, dpi=150, bbox_inches='tight')
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
