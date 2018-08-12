from numbers_to_text.constants import (
    NUMBER_CHUNK_SIZE,
    SINGLE,
    PLURAL2TO4,
    PLURAL5TO0,
)

from numbers_to_text.lang_configs.ru_lang import ru_lang_config

from numbers_to_text.utils import reversed_split_into_chunks


def prepare_num_string(num_string: str) -> str:
    formatting_zeros = (NUMBER_CHUNK_SIZE - len(num_string)) * '0'
    return formatting_zeros + num_string


def _number_chunk_to_words(num_string: str, unit_case: int) -> str:
    """
    :param num_string: string representation of number to transform into text
                       SHOULD BE not longer then 3 chars
    :return: text representation of num_string
    """

    if len(num_string) > NUMBER_CHUNK_SIZE:
        raise Exception('num_string should contain 3 chars or less')

    if not num_string.isdigit():
        raise Exception('num_string should contain only digits')

    hundred, ten, unit = prepare_num_string(num_string)

    hundred_text = ''
    ten_text = ''
    unit_text = ''

    if hundred is not '0':
        hundred_text = ru_lang_config['hundreds'][hundred]

    if ten is not '0':
        if ten is '1' and unit is not '0':
            ten_text = ru_lang_config['non_zero_ending_tens'][ten + unit]
        else:
            ten_text = ru_lang_config['zero_ending_tens'][ten]

    if ten is not '1' and unit is not '0':
        unit_text = ru_lang_config['units'][unit][unit_case]

    return ' '.join((hundred_text, ten_text, unit_text))


def get_chunk_name(chunk_config: dict, chunk_num_string: str):
    last_number = chunk_num_string[-1]
    if last_number is '1':
        return chunk_config['names'][SINGLE]
    elif last_number in ['2', '3', '4']:
        return chunk_config['names'][PLURAL2TO4]
    return chunk_config['names'][PLURAL5TO0]


def number_to_words(num_string: str) -> str:
    if not num_string.isdigit():
        raise Exception('num_string should contain only digits')

    chunks = reversed_split_into_chunks(num_string, NUMBER_CHUNK_SIZE)
    words = []
    for i, chunk in enumerate(list(chunks)):
        chunk_config = ru_lang_config['chunk_names'][i]
        chunk_text = _number_chunk_to_words(chunk, chunk_config['case'])
        chunk_name = get_chunk_name(chunk_config, chunk)
        words.append(f'{chunk_text} {chunk_name}')

    return ' '.join(reversed([word.strip() for word in words if word.strip()]))