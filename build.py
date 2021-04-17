import compileall
import re
compileall.compile_dir('Mag/', rx=re.compile(r'[/\\][.]ssh'), force=True)