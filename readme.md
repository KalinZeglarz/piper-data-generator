# piper-data-generator
## overview
Utility for generating random data to be used in further ml

## usage
### cli
command:
```shell script
python generate.py NUMBER_OF_EVENTS_TO_GENERATE [-t TIME_OF_FIRST_EVENT] [-f FORMAT_OF_OUTPUT]
```
sample:
```shell script
> python generate.py 10
1585416047,bathroom_light_2_switch,light_on
1585416300,corridor_1_light_1_sensor,light_on
1585416969,gate_2_remote_1,gate_open
1585418052,gate_1_remote_1,gate_open
1585418294,corridor_1_light_1_sensor,light_off
1585418342,bathroom_light_2_switch,light_off
1585418777,gate_1_remote_1,gate_close
1585419560,gate_2_remote_1,gate_close
1585420294,bathroom_light_2_switch,light_on
1585420995,bathroom_light_2_switch,

> python generate.py 10 -f json
{"time": 1585416155, "trigger": "bathroom_light_1_switch", "name": "light_on"}
{"time": 1585416948, "trigger": "corridor_1_light_1_sensor", "name": "light_on"}
{"time": 1585416984, "trigger": "bathroom_light_1_switch", "name": "light_off"}
{"time": 1585417430, "trigger": "gate_2_remote_1", "name": "gate_open"}
{"time": 1585417801, "trigger": "corridor_1_light_1_sensor", "name": "light_off"}
{"time": 1585420203, "trigger": "gate_2_remote_1", "name": "gate_open"}
{"time": 1585420635, "trigger": "gate_2_remote_1", "name": "gate_close"}
{"time": 1585420656, "trigger": "gate_2_remote_2", "name": "gate_open"}
{"time": 1585420727, "trigger": "gate_2_remote_2", "name": "gate_close"}
{"time": 1585422518, "trigger": "gate_2_remote_1", "name": "gate_close"}

```
### python api
tba 
```python
from generator.api import generate_events

generate_events(100)
```