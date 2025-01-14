from scalpel.call_graph.pycg import CallGraphGenerator
from scalpel.call_graph.pycg import formats
import json

cg_generator = CallGraphGenerator(["./cg_example_pkg/main.py"], "cg_example_pkg")
cg_generator.analyze()
cg = cg_generator.output()
formatter = formats.Simple(cg)
with open("example_results.json", "w+") as f:
    f.write(json.dumps(formatter.generate()))