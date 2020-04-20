from typing import List, Tuple, Dict

_events = {
    'lights': [('light_on', 'light_off')],
    'gates': [('gate_open', 'gate_close')],
    'ac': ['temp_up', 'temp_down'],
    'blind': [('blind_up', 'blind_down')],
    'device': [('on', 'off')]
}


def _room(name: str, trigs: Dict[str, List[str]]) -> List[Tuple[str, List[str]]]:
    return [(f'{name if name is not None else "general"}_{n}', e) for n, e in trigs.items()]


def _triggers(*trigs: List[Tuple[str, List[str]]]) -> Dict[str, List[str]]:
    rooms = [(n, e) for trig in trigs for n, e in trig]
    return {n: e for n, e in rooms}


triggers = _triggers(
    _room(
        'outdoor',
        {
            'gate_1_remote_1': _events['gates'],
            'gate_2_remote_1': _events['gates'],
            'gate_1_remote_2': _events['gates'],
            'gate_2_remote_2': _events['gates'],
            'light_1_sensor': _events['lights'],
            'light_2_sensor': _events['lights']
        }
    ),
    _room(
        'general',
        {
            'ac': _events['ac'],
        }
    ),
    _room(
        'bathroom',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
        }
    ),
    _room(
        'corridor',
        {
            'light_1_sensor': _events['lights']
        }
    ),
    _room(
        'kitchen',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
            'light_3_switch': _events['lights'],
            'blind_1_switch': _events['blind'],
            'blind_2_switch': _events['blind']
        }
    ),
    _room(
        'bedroom_1',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
            'light_3_switch': _events['lights'],
            'blind_1_switch': _events['blind']
        }
    ),
    _room(
        'bedroom_2',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
            'blind_1_switch': _events['blind']
        }
    ),
    _room(
        'bedroom_3',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
            'blind_1_switch': _events['blind']
        }
    ),
    _room(
        'living_room',
        {
            'light_1_switch': _events['lights'],
            'light_2_switch': _events['lights'],
            'light_3_switch': _events['lights'],
            'blind_1_switch': _events['blind'],
            'blind_2_switch': _events['blind'],
            'blind_3_switch': _events['blind'],
            'tv': _events['device']
        }
    )
)
