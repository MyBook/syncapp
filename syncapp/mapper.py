#!/usr/bin/env python
import sys
from lxml import html
from aeneas.executetask import ExecuteTask
from aeneas.language import Language
from aeneas.syncmap import SyncMapFormat
from aeneas.task import Task
from aeneas.task import TaskConfiguration
from aeneas.textfile import TextFragment, TextFile, TextFileFormat
import aeneas.globalconstants as gc
from aeneas.logger import Logger


def get_maps(text_content_file, audio_path):
    parsed = html.fromstring(text_content_file)
    map_table = []
    id_to_xpath = {}
    for i, z in enumerate(parsed.iter()):
        if z.text and z.tag == 'p':
            ident = unicode(i)
            map_table.append((ident, [z.text_content()]))
            id_to_xpath[ident] = z.getroottree().getpath(z)

    config = TaskConfiguration()
    config[gc.PPN_TASK_OS_FILE_FORMAT] = SyncMapFormat.JSON
    config[gc.PPN_TASK_IS_TEXT_FILE_FORMAT] = TextFileFormat.PARSED
    config[gc.PPN_TASK_LANGUAGE] = Language.RUS

    textfile = TextFile()
    for identifier, frag_text in map_table:
        textfile.add_fragment(TextFragment(identifier, Language.RUS, frag_text, frag_text))

    task = Task(logger=Logger())
    task.configuration = config
    task.text_file = textfile
    task.audio_file_path_absolute = audio_path

    ExecuteTask(task).execute()
    return task.sync_map.json_string, id_to_xpath
