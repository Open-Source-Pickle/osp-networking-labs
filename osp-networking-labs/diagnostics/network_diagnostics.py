#!/usr/bin/env python3
import subprocess, socket, json, sys

def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return {'ok': out.returncode == 0, 'stdout': out.stdout.strip(), 'stderr': out.stderr.strip(), 'code': out.returncode}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def ping(host='8.8.8.8', count='3'):
    return run(['ping', '-c', count, host])

def traceroute(host='8.8.8.8'):
    return run(['traceroute', host])

def dns_lookup(domain='adyen.com'):
    try:
        ip = socket.gethostbyname(domain)
        return {'ok': True, 'ip': ip}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def port_check(host='adyen.com', port=443):
    import socket as s
    try:
        with s.create_connection((host, port), timeout=5):
            return {'ok': True}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) > 1 else '8.8.8.8'
    data = {
        'ping': ping(host),
        'traceroute': traceroute(host),
        'dns': dns_lookup('adyen.com'),
        'port_443': port_check('adyen.com', 443)
    }
    print(json.dumps(data, indent=2))
