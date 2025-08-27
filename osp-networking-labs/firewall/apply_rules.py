#!/usr/bin/env python3
import argparse, json, pathlib, sys, yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / 'firewall' / 'firewall.schema.json'

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate(data, schema):
    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    if errors:
        print('Validation failed:')
        for e in errors:
            path = '.'.join(str(p) for p in e.path) or '<root>'
            print(f' - {path}: {e.message}')
        sys.exit(1)

def main():
    ap = argparse.ArgumentParser(description='Validate and preview-apply firewall rules.')
    ap.add_argument('--rules', required=True, type=pathlib.Path)
    args = ap.parse_args()

    rules = load_yaml(args.rules)
    schema = load_json(SCHEMA)
    validate(rules, schema)

    print('Rules are valid. Preview JSON payload:')
    print(json.dumps(rules, indent=2))
    print('# TODO: POST to your firewall API (Cisco/Palo Alto/UFW wrapper).')

if __name__ == '__main__':
    main()
