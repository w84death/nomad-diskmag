import compileall
import re
compileall.compile_dir('Mag/sources/', rx=re.compile(r'[/\\][.]ssh'), force=True)