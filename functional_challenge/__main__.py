import unittest,os,re,sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open('functional_challenge.py', 'r')
m=re.search(r'(\b_{0,2}import_{0,2}\b|\b_{0,2}builtins?_{0,2}\b|'
            r'globals|locals|__subclasses__|\bexec\s{0,}\(|\beval\b\s{0,}\()', f.read())
if m:
    print('Keyword',m.group(1),'not allowed')
    sys.exit(1)
f.close()

from test import TestAll

unittest.main(verbosity=2)
