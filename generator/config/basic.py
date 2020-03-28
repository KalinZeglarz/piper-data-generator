_events = {
    'lights': [('light_on', 'light_off')],
    'gates': [('gate_open', 'gate_close')],
    'ac': ['temp_up', 'temp_down']
}

triggers = {
    'gate_1_remote_1': _events['gates'],
    'gate_2_remote_1': _events['gates'],
    'gate_1_remote_2': _events['gates'],
    'gate_2_remote_2': _events['gates'],
    'bathroom_light_1_switch': _events['lights'],
    'bathroom_light_2_switch': _events['lights'],
    'corridor_1_light_1_sensor': _events['lights'],
    'ac': _events['ac']
}
